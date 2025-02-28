"""
Blogspot Scraper Module for Fuller Blogs
Handles scraping, parsing, and storing content from Blogspot blogs
"""

import os
import logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from typing import Dict, List, Optional
import json
import yaml
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BlogspotScraper:
    """Scraper for Blogspot blogs with content storage and visualization capabilities"""
    
    def __init__(self, blog_config: Dict, output_dir: str):
        """
        Initialize scraper with blog configuration
        
        Args:
            blog_config: Dictionary containing blog metadata
            output_dir: Base directory for storing scraped content
        """
        self.blog_config = blog_config
        self.base_url = blog_config['url']
        self.blog_name = blog_config['title']
        self.output_dir = Path(output_dir) / self.blog_name.lower().replace(' ', '_')
        self.setup_directories()
        
    def setup_directories(self):
        """Create necessary directories for storing blog content"""
        dirs = ['posts', 'media', 'metadata', 'logs', 'visualizations']
        for dir_name in dirs:
            dir_path = self.output_dir / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)
            
    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """
        Fetch and parse a blog page
        
        Args:
            url: URL to fetch
            
        Returns:
            BeautifulSoup object or None if failed
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            logger.error(f"Error fetching {url}: {str(e)}")
            return None
            
    def extract_post_data(self, post_soup: BeautifulSoup) -> Dict:
        """
        Extract relevant data from a blog post
        
        Args:
            post_soup: BeautifulSoup object of post
            
        Returns:
            Dictionary containing post data
        """
        data = {
            'title': '',
            'date': '',
            'content': '',
            'tags': [],
            'links': [],
            'images': []
        }
        
        try:
            # Extract title
            title_elem = post_soup.find('h3', class_='post-title')
            if title_elem:
                data['title'] = title_elem.text.strip()
                
            # Extract date
            date_elem = post_soup.find('time')
            if date_elem:
                data['date'] = date_elem.get('datetime', '')
                
            # Extract content
            content_elem = post_soup.find('div', class_='post-body')
            if content_elem:
                data['content'] = content_elem.text.strip()
                
            # Extract links
            links = content_elem.find_all('a') if content_elem else []
            data['links'] = [{'text': a.text, 'href': a['href']} for a in links]
            
            # Extract images
            images = content_elem.find_all('img') if content_elem else []
            data['images'] = [img['src'] for img in images]
            
        except Exception as e:
            logger.error(f"Error extracting post data: {str(e)}")
            
        return data
        
    def save_post(self, post_data: Dict, post_id: str):
        """
        Save post data to files
        
        Args:
            post_data: Dictionary containing post data
            post_id: Unique identifier for the post
        """
        # Save post content
        post_path = self.output_dir / 'posts' / f"{post_id}.md"
        with open(post_path, 'w', encoding='utf-8') as f:
            f.write(f"# {post_data['title']}\n\n")
            f.write(f"Date: {post_data['date']}\n\n")
            f.write(post_data['content'])
            
        # Save metadata
        meta_path = self.output_dir / 'metadata' / f"{post_id}.json"
        with open(meta_path, 'w', encoding='utf-8') as f:
            json.dump(post_data, f, indent=2)
            
    def scrape_blog(self):
        """Scrape entire blog and save content"""
        logger.info(f"Starting scrape of {self.blog_name}")
        
        # Start with main page
        soup = self.fetch_page(self.base_url)
        if not soup:
            return
            
        # Find and process posts
        posts = soup.find_all('div', class_='post')
        for i, post in enumerate(posts):
            post_data = self.extract_post_data(post)
            post_id = f"post_{i:04d}"
            self.save_post(post_data, post_id)
            logger.info(f"Saved post: {post_data['title']}")
            
        logger.info(f"Completed scrape of {self.blog_name}")
        
    def generate_visualization(self):
        """Generate visualization of blog content and structure"""
        try:
            # Count posts by date
            posts_data = []
            posts_dir = self.output_dir / 'posts'
            for post_file in posts_dir.glob('*.md'):
                with open(post_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    date_line = [line for line in content.split('\n') if line.startswith('Date:')][0]
                    date_str = date_line.replace('Date:', '').strip()
                    posts_data.append(datetime.fromisoformat(date_str))
                    
            # Create visualization data
            viz_data = {
                'blog_name': self.blog_name,
                'total_posts': len(posts_data),
                'date_range': {
                    'start': min(posts_data).isoformat(),
                    'end': max(posts_data).isoformat()
                },
                'posts_by_year': {}
            }
            
            # Save visualization data
            viz_path = self.output_dir / 'visualizations' / 'blog_stats.json'
            with open(viz_path, 'w', encoding='utf-8') as f:
                json.dump(viz_data, f, indent=2)
                
            logger.info(f"Generated visualization for {self.blog_name}")
            
        except Exception as e:
            logger.error(f"Error generating visualization: {str(e)}") 