"""
Main script for scraping Fuller-related Blogspot blogs
"""

import os
import yaml
import logging
from pathlib import Path
from blogspot_scraper import BlogspotScraper

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

def load_blog_configs():
    """Load blog configurations from blogs_index.md"""
    try:
        blogs_index_path = Path(__file__).parents[2] / 'fonds' / 'blogs' / 'blogs_index.md'
        with open(blogs_index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract YAML block
            yaml_block = content.split('```yaml')[1].split('```')[0]
            return yaml.safe_load(yaml_block)['blogs']
    except Exception as e:
        logger.error(f"Error loading blog configs: {str(e)}")
        return {}

def main():
    """Main function to run blog scraping"""
    logger.info("Starting Fuller blogs scraping process")
    
    # Create output directory
    output_dir = Path(__file__).parents[2] / 'output' / 'blogs'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load blog configurations
    blog_configs = load_blog_configs()
    
    # Process each blog
    for blog_id, config in blog_configs.items():
        logger.info(f"Processing blog: {blog_id}")
        try:
            # Create scraper instance
            scraper = BlogspotScraper(
                blog_config={
                    'url': config['url'],
                    'title': blog_id.replace('_', ' ').title()
                },
                output_dir=str(output_dir)
            )
            
            # Run scraping
            scraper.scrape_blog()
            
            # Generate visualization
            scraper.generate_visualization()
            
            logger.info(f"Completed processing of {blog_id}")
            
        except Exception as e:
            logger.error(f"Error processing {blog_id}: {str(e)}")
            continue
            
    logger.info("Completed Fuller blogs scraping process")

if __name__ == '__main__':
    main() 