"""
Minimal Blogspot Scraper for Fuller Blogs
Uses only essential dependencies for basic scraping functionality
"""

import os
import json
import logging
from pathlib import Path
from datetime import datetime
import urllib.request
from urllib.parse import urljoin
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fuller_blogs_scrape.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class MinimalBlogScraper:
    """Minimal scraper for Blogspot blogs"""
    
    def __init__(self, blog_config, output_dir):
        """Initialize scraper with configuration"""
        self.url = blog_config['url']
        self.blog_name = blog_config['title']
        self.output_dir = Path(output_dir) / self.blog_name.lower().replace(' ', '_')
        self.setup_directories()
        
    def setup_directories(self):
        """Create necessary directories"""
        dirs = ['posts', 'metadata', 'logs']
        for dir_name in dirs:
            dir_path = self.output_dir / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)
            
    def fetch_page(self, url):
        """Fetch page content"""
        try:
            with urllib.request.urlopen(url) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            logger.error(f"Error fetching {url}: {str(e)}")
            return None
            
    def extract_post_data(self, html):
        """Extract post data using regex patterns"""
        data = {
            'title': '',
            'date': '',
            'content': '',
            'links': []
        }
        
        try:
            # Extract title
            title_match = re.search(r'<h3 class="post-title[^>]*>(.*?)</h3>', html, re.DOTALL)
            if title_match:
                data['title'] = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
                
            # Extract date
            date_match = re.search(r'<time[^>]*datetime="([^"]*)"', html)
            if date_match:
                data['date'] = date_match.group(1)
                
            # Extract content
            content_match = re.search(r'<div class="post-body[^>]*>(.*?)</div>', html, re.DOTALL)
            if content_match:
                content = re.sub(r'<[^>]+>', '', content_match.group(1))
                data['content'] = content.strip()
                
            # Extract links
            links = re.findall(r'<a href="([^"]*)"[^>]*>(.*?)</a>', html)
            data['links'] = [{'url': url, 'text': re.sub(r'<[^>]+>', '', text)} 
                           for url, text in links]
                
        except Exception as e:
            logger.error(f"Error extracting data: {str(e)}")
            
        return data
        
    def save_post(self, post_data, post_id):
        """Save post content and metadata"""
        try:
            # Save content as markdown
            post_path = self.output_dir / 'posts' / f"{post_id}.md"
            with open(post_path, 'w', encoding='utf-8') as f:
                f.write(f"# {post_data['title']}\n\n")
                f.write(f"Date: {post_data['date']}\n\n")
                f.write(post_data['content'])
                
            # Save metadata
            meta_path = self.output_dir / 'metadata' / f"{post_id}.json"
            with open(meta_path, 'w', encoding='utf-8') as f:
                json.dump(post_data, f, indent=2)
                
            logger.info(f"Saved post: {post_data['title']}")
            
        except Exception as e:
            logger.error(f"Error saving post: {str(e)}")
            
    def scrape_blog(self):
        """Main scraping function"""
        logger.info(f"Starting scrape of {self.blog_name}")
        
        html = self.fetch_page(self.url)
        if not html:
            return
            
        # Extract posts using regex
        posts_html = re.findall(r'<div class="post"[^>]*>(.*?)</div>\s*</div>', html, re.DOTALL)
        
        for i, post_html in enumerate(posts_html):
            post_data = self.extract_post_data(post_html)
            post_id = f"post_{i:04d}"
            self.save_post(post_data, post_id)
            
        logger.info(f"Completed scrape of {self.blog_name}")

def load_blog_configs():
    """Load blog configurations"""
    try:
        blogs_index_path = Path(__file__).parents[2] / 'fonds' / 'blogs' / 'blogs_index.md'
        with open(blogs_index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            yaml_block = content.split('```yaml')[1].split('```')[0]
            # Simple YAML parsing
            blogs = {}
            current_blog = None
            for line in yaml_block.split('\n'):
                line = line.strip()
                if line.endswith(':'):
                    current_blog = line[:-1].strip()
                    blogs[current_blog] = {}
                elif ':' in line and current_blog:
                    key, value = line.split(':', 1)
                    blogs[current_blog][key.strip()] = value.strip().strip('"')
            return blogs
    except Exception as e:
        logger.error(f"Error loading blog configs: {str(e)}")
        return {}

def main():
    """Main function"""
    logger.info("Starting Fuller blogs scraping process")
    
    output_dir = Path(__file__).parents[2] / 'output' / 'blogs'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    blog_configs = load_blog_configs()
    
    for blog_id, config in blog_configs.items():
        logger.info(f"Processing blog: {blog_id}")
        try:
            scraper = MinimalBlogScraper(
                blog_config={
                    'url': config['url'],
                    'title': blog_id.replace('_', ' ').title()
                },
                output_dir=str(output_dir)
            )
            scraper.scrape_blog()
            
        except Exception as e:
            logger.error(f"Error processing {blog_id}: {str(e)}")
            continue
            
    logger.info("Completed Fuller blogs scraping process")

if __name__ == '__main__':
    main() 