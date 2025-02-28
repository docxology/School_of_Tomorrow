#!/usr/bin/env python3

import os
import json
import logging
import urllib.request
import re
import html
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime
import time

class BlogScraper:
    def __init__(self, blog_config):
        self.blog_config = blog_config
        self.setup_logging()
        self.setup_directories()
        self.posts_scraped = 0
        self.max_retries = 3
        self.delay = 2  # seconds between requests
        self.total_posts = None  # Will be set after first fetch
    
    def setup_logging(self):
        """Setup logging with both file and detailed console output"""
        log_dir = Path('fonds/blogs/logs')
        log_dir.mkdir(parents=True, exist_ok=True)
        
        # Create formatters
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_formatter = logging.Formatter(
            '%(asctime)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        
        # File handler
        file_handler = logging.FileHandler(
            log_dir / f'blog_scrape_{datetime.now().strftime("%Y%m%d")}.log'
        )
        file_handler.setFormatter(file_formatter)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(console_formatter)
        
        # Setup logger
        self.logger = logging.getLogger(f"BlogScraper-{self.blog_config['name']}")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def setup_directories(self):
        """Create necessary directories in fonds/blogs"""
        self.base_dir = Path('fonds/blogs')
        self.blog_dir = self.base_dir / self.blog_config['name'].lower().replace(' ', '_')
        
        for dir_path in ['posts', 'metadata', 'archive']:
            dir_full_path = self.blog_dir / dir_path
            dir_full_path.mkdir(parents=True, exist_ok=True)
            self.logger.info(f"Ensuring directory exists: {dir_full_path.absolute()}")

    def fetch_feed(self, url, start_index=1):
        """Fetch feed with pagination support"""
        feed_url = f"{url}?start-index={start_index}&max-results=25"
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/atom+xml'
        }
        
        for attempt in range(self.max_retries):
            try:
                self.logger.info(f"Fetching page {(start_index-1)//25 + 1} (posts {start_index}-{start_index+24})")
                request = urllib.request.Request(feed_url, headers=headers)
                with urllib.request.urlopen(request) as response:
                    content = response.read().decode('utf-8')
                    
                    # Try to get total posts count from first fetch
                    if self.total_posts is None and '<openSearch:totalResults>' in content:
                        total_match = re.search(r'<openSearch:totalResults>(\d+)</openSearch:totalResults>', content)
                        if total_match:
                            self.total_posts = int(total_match.group(1))
                            self.logger.info(f"Total posts to scrape: {self.total_posts}")
                    
                    return content
            except Exception as e:
                self.logger.error(f"Attempt {attempt + 1} failed to fetch {feed_url}: {str(e)}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.delay * (attempt + 1))
                else:
                    raise
        
        return None

    def clean_html_content(self, content):
        """Clean HTML content while preserving structure"""
        if not content:
            return ""
            
        # Remove script tags and their contents
        content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
        
        # Convert HTML entities
        content = html.unescape(content)
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        # Convert common HTML elements to markdown
        for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            level = int(tag.name[1])
            tag.replace_with(f"\n{'#' * level} {tag.get_text()}\n")
            
        for tag in soup.find_all('p'):
            tag.replace_with(f"\n{tag.get_text()}\n")
            
        for tag in soup.find_all('a'):
            url = tag.get('href', '')
            text = tag.get_text()
            tag.replace_with(f"[{text}]({url})")
            
        for tag in soup.find_all(['ul', 'ol']):
            items = []
            for li in tag.find_all('li'):
                items.append(f"- {li.get_text()}")
            tag.replace_with('\n' + '\n'.join(items) + '\n')
        
        # Clean up whitespace
        text = soup.get_text()
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = text.strip()
        
        return text

    def extract_post_data(self, entry_xml):
        """Extract post data from entry XML"""
        try:
            # Extract post ID
            post_id = re.search(r'<id>.*?\.post-(\d+)</id>', entry_xml).group(1)
            
            # Extract title
            title_match = re.search(r'<title type=\'text\'>(.*?)</title>', entry_xml)
            title = html.unescape(title_match.group(1)) if title_match else 'Untitled'
            
            # Extract dates
            published = re.search(r'<published>(.*?)</published>', entry_xml).group(1)
            updated = re.search(r'<updated>(.*?)</updated>', entry_xml).group(1)
            
            # Extract content
            content_match = re.search(r'<content type=\'html\'>(.*?)</content>', entry_xml, re.DOTALL)
            content = self.clean_html_content(content_match.group(1)) if content_match else ''
            
            # Extract categories/labels
            categories = []
            for cat_match in re.finditer(r'<category.*?term=\'(.*?)\'', entry_xml):
                categories.append(cat_match.group(1))
            
            # Extract author
            author_match = re.search(r'<author><name>(.*?)</name>', entry_xml)
            author = author_match.group(1) if author_match else 'Unknown'
            
            return {
                'id': post_id,
                'title': title,
                'published': published,
                'updated': updated,
                'content': content,
                'categories': categories,
                'author': author,
                'blog_name': self.blog_config['name']
            }
        except Exception as e:
            self.logger.error(f"Error extracting post data: {str(e)}")
            return None

    def save_post(self, post_data):
        """Save post content and metadata"""
        try:
            # Create slug from title
            slug = re.sub(r'[^a-z0-9]+', '-', post_data['title'].lower()).strip('-')
            
            # Save content as markdown
            post_file = self.blog_dir / 'posts' / f"{slug}.md"
            with open(post_file, 'w', encoding='utf-8') as f:
                f.write('---\n')
                f.write(f"title: {post_data['title']}\n")
                f.write(f"id: {post_data['id']}\n")
                f.write(f"author: {post_data['author']}\n")
                f.write(f"published: {post_data['published']}\n")
                f.write(f"updated: {post_data['updated']}\n")
                f.write(f"blog: {post_data['blog_name']}\n")
                f.write(f"tags: {', '.join(post_data['categories'])}\n")
                f.write('---\n\n')
                f.write(post_data['content'])
            
            # Save metadata as JSON
            metadata_file = self.blog_dir / 'metadata' / f"{slug}.json"
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(post_data, f, indent=2)
            
            self.posts_scraped += 1
            progress = (self.posts_scraped / self.total_posts * 100) if self.total_posts else 0
            self.logger.info(
                f"[{progress:3.1f}%] Saved post {self.posts_scraped}/{self.total_posts or '?'}: "
                f"{post_file.absolute()}"
            )
            
        except Exception as e:
            self.logger.error(f"Error saving post: {str(e)}")

    def scrape(self):
        """Main scraping function with pagination support"""
        feed_url = self.blog_config['feed_url']
        self.logger.info(f"Starting scrape of {self.blog_config['name']}")
        self.logger.info(f"Feed URL: {feed_url}")
        self.logger.info(f"Output directory: {self.blog_dir.absolute()}")
        
        start_index = 1
        total_posts = 0
        has_more = True
        
        while has_more:
            try:
                feed_content = self.fetch_feed(feed_url, start_index)
                if not feed_content:
                    break
                
                # Save raw feed
                archive_file = self.blog_dir / 'archive' / f"feed_{start_index}.xml"
                with open(archive_file, 'w', encoding='utf-8') as f:
                    f.write(feed_content)
                    self.logger.debug(f"Saved raw feed to: {archive_file.absolute()}")
                
                # Extract and process entries
                entries = re.findall(r'<entry>(.*?)</entry>', feed_content, re.DOTALL)
                if not entries:
                    has_more = False
                    continue
                
                for entry in entries:
                    post_data = self.extract_post_data(entry)
                    if post_data:
                        self.save_post(post_data)
                        total_posts += 1
                
                start_index += len(entries)
                time.sleep(self.delay)  # Be nice to the server
                
            except Exception as e:
                self.logger.error(f"Error processing page {(start_index-1)//25 + 1}: {str(e)}")
                break
        
        self.logger.info(f"Completed scraping {total_posts} posts from {self.blog_config['name']}")
        self.logger.info(f"Posts are saved in: {self.blog_dir.absolute()}")
        return total_posts

def load_blog_configs():
    """Load blog configurations from blogs_index.md"""
    try:
        blogs_index_path = Path('fonds/blogs/blogs_index.md')
        with open(blogs_index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract YAML block
        yaml_match = re.search(r'```yaml\s*blogs:\s*(.*?)\s*```', content, re.DOTALL)
        if not yaml_match:
            raise ValueError("Could not find blogs configuration in blogs_index.md")
            
        yaml_content = yaml_match.group(1)
        
        # Parse blog configurations
        blogs = []
        current_blog = None
        blog_data = {}
        
        for line in yaml_content.split('\n'):
            line = line.strip()
            if not line:
                continue
                
            if line.endswith(':') and not line.startswith(' '):
                if current_blog and blog_data:
                    blogs.append(blog_data)
                current_blog = line[:-1].strip()
                blog_data = {'name': current_blog}
            elif ':' in line and current_blog:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"')
                if key == 'url':
                    # Convert blog URL to feed URL
                    blog_data['feed_url'] = value.rstrip('/') + '/feeds/posts/default'
                blog_data[key] = value
        
        if current_blog and blog_data:
            blogs.append(blog_data)
            
        return blogs
        
    except Exception as e:
        logging.error(f"Error loading blog configs: {str(e)}")
        return []

def main():
    """Main function"""
    # Setup root logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(Path('fonds/blogs/logs/scraper.log')),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger("BlogScraper")
    
    logger.info("Starting Fuller blogs scraping process")
    start_time = time.time()
    
    blog_configs = load_blog_configs()
    total_posts = 0
    
    for i, config in enumerate(blog_configs, 1):
        try:
            logger.info(f"\nProcessing blog {i}/{len(blog_configs)}: {config['name']}")
            logger.info("=" * 80)
            
            scraper = BlogScraper(config)
            posts = scraper.scrape()
            total_posts += posts
            
            logger.info("-" * 80)
            
        except Exception as e:
            logger.error(f"Error processing {config['name']}: {str(e)}")
            continue
    
    duration = time.time() - start_time
    logger.info("=" * 80)
    logger.info(f"Completed Fuller blogs scraping process in {duration:.1f} seconds")
    logger.info(f"Total posts scraped: {total_posts}")
    logger.info(f"Output directory: {Path('fonds/blogs').absolute()}")

if __name__ == '__main__':
    main() 