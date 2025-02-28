"""
Simplified Blog Visualization Module
Generates basic insights from scraped blog data
"""

import json
import logging
from pathlib import Path
from typing import Dict, List
from datetime import datetime
import statistics

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SimpleBlogVisualizer:
    """Generates basic visualizations and analytics from blog data"""
    
    def __init__(self, blog_dir: Path):
        """
        Initialize visualizer with blog directory
        
        Args:
            blog_dir: Path to blog output directory
        """
        self.blog_dir = Path(blog_dir)
        self.posts_dir = self.blog_dir / 'posts'
        self.metadata_dir = self.blog_dir / 'metadata'
        self.analysis_dir = self.blog_dir / 'analysis'
        self.analysis_dir.mkdir(exist_ok=True)
        
        logger.info(f"Initialized SimpleBlogVisualizer for directory: {blog_dir}")
        self._verify_directory_structure()

    def _verify_directory_structure(self) -> bool:
        """Verify the required directory structure exists"""
        required_dirs = [self.posts_dir, self.metadata_dir]
        missing_dirs = [d for d in required_dirs if not d.exists()]
        
        if missing_dirs:
            logger.error(f"Missing required directories: {missing_dirs}")
            return False
            
        logger.info("Directory structure verification passed")
        return True

    def load_metadata(self) -> List[Dict]:
        """Load all post metadata"""
        metadata = []
        for meta_file in self.metadata_dir.glob('*.json'):
            try:
                with open(meta_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    metadata.append(data)
            except Exception as e:
                logger.error(f"Error loading metadata file {meta_file}: {str(e)}")
        return metadata

    def load_post_contents(self) -> Dict[str, str]:
        """Load all post contents"""
        contents = {}
        for post_file in self.posts_dir.glob('*.md'):
            try:
                with open(post_file, 'r', encoding='utf-8') as f:
                    contents[post_file.stem] = f.read()
            except Exception as e:
                logger.error(f"Error loading post file {post_file}: {str(e)}")
        return contents

    def analyze_content(self):
        """Analyze blog content and generate statistics"""
        try:
            metadata = self.load_metadata()
            contents = self.load_post_contents()
            
            # Basic statistics
            stats = {
                'total_posts': len(metadata),
                'total_words': sum(len(str(post.get('content', '')).split()) for post in metadata),
                'avg_words_per_post': 0,
                'total_links': sum(len(post.get('links', [])) for post in metadata),
                'total_comments': sum(post.get('comments', 0) for post in metadata),
                'total_shares': sum(post.get('shares', 0) for post in metadata),
                'posts_by_month': {},
                'common_words': self._get_common_words(contents),
                'engagement_stats': {
                    'max_comments': 0,
                    'max_shares': 0,
                    'avg_comments': 0,
                    'avg_shares': 0
                }
            }
            
            # Calculate averages
            if stats['total_posts'] > 0:
                stats['avg_words_per_post'] = stats['total_words'] / stats['total_posts']
                
                comments = [post.get('comments', 0) for post in metadata]
                shares = [post.get('shares', 0) for post in metadata]
                
                stats['engagement_stats'].update({
                    'max_comments': max(comments),
                    'max_shares': max(shares),
                    'avg_comments': statistics.mean(comments),
                    'avg_shares': statistics.mean(shares)
                })
            
            # Analyze posting frequency by month
            for post in metadata:
                if 'date' in post:
                    try:
                        date = datetime.fromisoformat(post['date'])
                        month_key = f"{date.year}-{date.month:02d}"
                        stats['posts_by_month'][month_key] = stats['posts_by_month'].get(month_key, 0) + 1
                    except ValueError:
                        continue
            
            # Save analysis results
            analysis_file = self.analysis_dir / 'blog_analysis.json'
            with open(analysis_file, 'w', encoding='utf-8') as f:
                json.dump(stats, f, indent=2)
            
            logger.info(f"Analysis complete. Results saved to {analysis_file}")
            self._print_summary(stats)
            
        except Exception as e:
            logger.error(f"Error in content analysis: {str(e)}")

    def _get_common_words(self, contents: Dict[str, str], min_length: int = 4) -> List[tuple]:
        """Get most common words from all posts"""
        word_freq = {}
        
        for content in contents.values():
            # Simple word tokenization
            words = content.lower().split()
            words = [word.strip('.,!?()[]{}":;') for word in words]
            words = [word for word in words if len(word) >= min_length]
            
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
        
        # Sort by frequency
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:20]  # Return top 20 words

    def _print_summary(self, stats: Dict):
        """Print a human-readable summary of the analysis"""
        print("\n=== Blog Analysis Summary ===")
        print(f"Total Posts: {stats['total_posts']}")
        print(f"Total Words: {stats['total_words']}")
        print(f"Average Words per Post: {stats['avg_words_per_post']:.1f}")
        print(f"Total Links: {stats['total_links']}")
        print("\nEngagement Metrics:")
        print(f"Total Comments: {stats['total_comments']}")
        print(f"Total Shares: {stats['total_shares']}")
        print(f"Average Comments per Post: {stats['engagement_stats']['avg_comments']:.1f}")
        print(f"Average Shares per Post: {stats['engagement_stats']['avg_shares']:.1f}")
        print("\nTop 10 Most Common Words:")
        for word, count in stats['common_words'][:10]:
            print(f"  {word}: {count}")
        print("\nPosts by Month:")
        for month, count in sorted(stats['posts_by_month'].items()):
            print(f"  {month}: {count}")

def analyze_multiple_blogs(blog_dirs: List[Path]) -> Dict:
    """Analyze multiple blogs and generate comparative statistics"""
    logger.info(f"Processing {len(blog_dirs)} blogs")
    
    all_stats = {}
    
    for blog_dir in blog_dirs:
        try:
            visualizer = SimpleBlogVisualizer(blog_dir)
            visualizer.analyze_content()
            
            # Load the analysis results
            analysis_file = blog_dir / 'analysis' / 'blog_analysis.json'
            with open(analysis_file, 'r', encoding='utf-8') as f:
                all_stats[blog_dir.name] = json.load(f)
                
        except Exception as e:
            logger.error(f"Error processing blog {blog_dir}: {str(e)}")
    
    return all_stats 