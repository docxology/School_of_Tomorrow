"""
Blog Visualization Module
Generates visual insights from scraped blog data with comprehensive logging and verification
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import matplotlib
matplotlib.use('Agg')  # Set the backend before importing pyplot
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from wordcloud import WordCloud
import networkx as nx
from collections import Counter, defaultdict
from textblob import TextBlob
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import calendar
import sys
import hashlib
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import imghdr
import uuid
import colorlog
import time
import statistics

# Configure logging with colors and enhanced formatting
handler = colorlog.StreamHandler(sys.stdout)
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s [%(levelname)s] %(name)s: %(message)s%(reset)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
))

# Also add a file handler for persistent logging
file_handler = logging.FileHandler('blog_visualizer.log')
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
))

logger = colorlog.getLogger('blog_visualizer')
logger.addHandler(handler)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

class Timer:
    """Context manager for timing operations"""
    def __init__(self, description: str, logger=None):
        self.description = description
        self.logger = logger or logging.getLogger(__name__)

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        elapsed = time.time() - self.start
        self.logger.info(f"{self.description} completed in {elapsed:.2f} seconds")

def validate_png(filepath: Path) -> bool:
    """Validate that a file is a valid PNG image"""
    try:
        if not filepath.exists():
            return False
        if imghdr.what(filepath) != 'png':
            return False
        return True
    except Exception:
        return False

def save_plot(plt, filepath: Path, dpi: int = 300) -> bool:
    """Save plot with validation and error handling"""
    try:
        # Create parent directory if it doesn't exist
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        # Save with high DPI for better quality
        plt.savefig(filepath, dpi=dpi, bbox_inches='tight')
        plt.close('all')  # Close all figures after saving
        
        # Validate the saved PNG
        if not validate_png(filepath):
            logger.error(f"Generated invalid PNG file: {filepath}")
            return False
            
        logger.info(f"Successfully saved and validated: {filepath}")
        return True
    except Exception as e:
        logger.error(f"Error saving plot to {filepath}: {str(e)}")
        plt.close('all')  # Ensure figures are closed even if save fails
        return False

class BlogVisualizer:
    """Generates comprehensive visualizations from scraped blog data with verification"""
    
    def __init__(self, blog_dir: Path, verification_enabled: bool = True):
        """
        Initialize visualizer with blog directory
        
        Args:
            blog_dir: Path to blog output directory
            verification_enabled: Whether to perform verification checks
        """
        self.blog_dir = Path(blog_dir)
        self.posts_dir = self.blog_dir / 'posts'
        self.metadata_dir = self.blog_dir / 'metadata'
        self.viz_dir = self.blog_dir / 'visualizations'
        self.verification_enabled = verification_enabled
        self.stats = defaultdict(int)
        self._metadata_cache = None  # Add metadata cache
        
        # Set Matplotlib backend to Agg for non-interactive environments
        plt.switch_backend('Agg')
        
        # Set style for better-looking visualizations
        plt.style.use('seaborn')
        
        # Create visualization subdirectories
        self.temporal_dir = self.viz_dir / 'temporal'
        self.content_dir = self.viz_dir / 'content'
        self.network_dir = self.viz_dir / 'network'
        self.engagement_dir = self.viz_dir / 'engagement'
        self.verification_dir = self.viz_dir / 'verification'
        
        for dir_path in [self.viz_dir, self.temporal_dir, self.content_dir, 
                        self.network_dir, self.engagement_dir, self.verification_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
            
        logger.info(f"Initialized BlogVisualizer for directory: {blog_dir}")
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

    def _verify_data_integrity(self):
        """Verify data integrity and generate verification report"""
        try:
            metadata = self.load_metadata()
            contents = self.load_post_contents()
            
            verification_data = {
                'total_posts': len(metadata),
                'posts_with_dates': sum(1 for post in metadata if post.get('published') or post.get('date')),
                'posts_with_content': sum(1 for post in metadata if post.get('content')),
                'posts_with_links': sum(1 for post in metadata if post.get('links')),
                'invalid_dates': [],
                'empty_content': [],
                'data_completeness': 0.0,
                'total_words': sum(len(str(post.get('content', '')).split()) for post in metadata),
                'total_links': sum(len(post.get('links', [])) for post in metadata),
                'total_comments': sum(post.get('comments', 0) for post in metadata),
                'total_shares': sum(post.get('shares', 0) for post in metadata)
            }
            
            # Check for invalid dates
            for post in metadata:
                if post.get('published') or post.get('date'):
                    try:
                        date_str = post.get('published') or post.get('date')
                        pd.to_datetime(date_str)
                    except (ValueError, TypeError):
                        verification_data['invalid_dates'].append(post.get('id', 'unknown'))
                
                # Check for empty content
                if not post.get('content'):
                    verification_data['empty_content'].append(post.get('id', 'unknown'))
            
            # Calculate data completeness
            required_fields = ['title', 'content', 'published', 'links']
            completeness_scores = []
            for post in metadata:
                score = sum(1 for field in required_fields if post.get(field)) / len(required_fields)
                completeness_scores.append(score)
            verification_data['data_completeness'] = statistics.mean(completeness_scores) if completeness_scores else 0.0
            
            # Save verification data
            verification_file = self.verification_dir / 'data_verification.json'
            with open(verification_file, 'w') as f:
                json.dump(verification_data, f, indent=2)
            
            # Save content hashes separately
            content_hashes = {
                f'content_hash_{post.get("id", "unknown")}': hashlib.sha256(
                    str(post.get('content', '')).encode()
                ).hexdigest()
                for post in metadata
            }
            
            hash_file = self.verification_dir / 'blog_statistics.json'
            with open(hash_file, 'w') as f:
                json.dump(content_hashes, f, indent=2)
            
            logger.info(f"Data verification complete. Results saved to {verification_file}")
            return verification_data
            
        except Exception as e:
            logger.error(f"Error during data verification: {str(e)}")
            return None

    def load_metadata(self) -> List[Dict]:
        """Load all post metadata with verification"""
        if self._metadata_cache is not None:
            logger.debug("Using cached metadata")
            return self._metadata_cache
            
        with Timer("Metadata loading", logger):
            metadata = []
            total_files = len(list(self.metadata_dir.glob('*.json')))
            
            # Reset stats before processing metadata
            self.stats = defaultdict(int)
            
            logger.info(f"Loading metadata from {total_files} files")
            
            successful_loads = 0
            failed_loads = 0
            
            for meta_file in tqdm(self.metadata_dir.glob('*.json'), 
                                total=total_files, 
                                desc="Loading metadata",
                                unit="files"):
                try:
                    with open(meta_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # Convert the blog's date format to our expected format
                        if 'published' in data:
                            data['date'] = data['published']
                        if 'content' not in data or not data['content']:
                            # Try to load content from posts directory
                            post_file = self.posts_dir / f"{meta_file.stem}.md"
                            if post_file.exists():
                                with open(post_file, 'r', encoding='utf-8') as pf:
                                    data['content'] = pf.read()
                        # Add links field if not present
                        if 'links' not in data:
                            data['links'] = []
                        metadata.append(data)
                        self._update_stats(data)
                        successful_loads += 1
                except json.JSONDecodeError:
                    logger.error(f"Invalid JSON in file: {meta_file}")
                    failed_loads += 1
                except Exception as e:
                    logger.error(f"Error loading metadata file {meta_file}: {str(e)}")
                    failed_loads += 1
            
            logger.info(f"Metadata loading summary:")
            logger.info(f"  - Successfully loaded: {successful_loads} files")
            logger.info(f"  - Failed to load: {failed_loads} files")
            logger.info(f"  - Total files processed: {total_files}")
            
            if self.verification_enabled:
                with Timer("Data verification", logger):
                    verification_data = self._verify_data_integrity()
                    if verification_data:
                        logger.info(f"Data verification results:")
                        logger.info(f"  - Total posts: {verification_data['total_posts']}")
                        logger.info(f"  - Posts with dates: {verification_data['posts_with_dates']}")
                        logger.info(f"  - Posts with content: {verification_data['posts_with_content']}")
                        logger.info(f"  - Data completeness: {verification_data['data_completeness']:.2%}")
            
            self._metadata_cache = metadata
            return metadata

    def _update_stats(self, post_data: Dict):
        """Update running statistics for the blog"""
        self.stats['total_posts'] += 1
        self.stats['total_words'] += len(str(post_data.get('content', '')).split())
        self.stats['total_links'] += len(post_data.get('links', []))
        # Add blog-specific stats
        self.stats['blog_name'] = post_data.get('blog_name', 'unknown')
        self.stats['author'] = post_data.get('author', 'unknown')
        # Track post dates
        if 'published' in post_data:
            date = pd.to_datetime(post_data['published'])
            if 'first_post_date' not in self.stats or date < pd.to_datetime(self.stats['first_post_date']):
                self.stats['first_post_date'] = post_data['published']
            if 'last_post_date' not in self.stats or date > pd.to_datetime(self.stats['last_post_date']):
                self.stats['last_post_date'] = post_data['published']

    def load_post_contents(self) -> Dict[str, str]:
        """Load all post contents with verification"""
        contents = {}
        total_files = len(list(self.posts_dir.glob('*.md')))
        
        logger.info(f"Loading post contents from {total_files} files")
        
        for post_file in tqdm(self.posts_dir.glob('*.md'), total=total_files, desc="Loading posts"):
            try:
                with open(post_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    contents[post_file.stem] = content
                    
                    # Calculate and store content hash for verification
                    content_hash = hashlib.md5(content.encode()).hexdigest()
                    self.stats[f'content_hash_{post_file.stem}'] = content_hash
            except Exception as e:
                logger.error(f"Error loading post file {post_file}: {str(e)}")
        
        return contents

    def generate_temporal_visualizations(self):
        """Generate comprehensive temporal visualizations"""
        try:
            metadata = self.load_metadata()
            df = pd.DataFrame(metadata)
            
            # Ensure we have date information
            if 'published' not in df.columns and 'date' not in df.columns:
                logger.warning("No date information found in metadata")
                return
                
            # Convert published dates to datetime with UTC
            df['date'] = pd.to_datetime(df['published'].fillna(df.get('date')), utc=True)
            df = df.set_index('date')
            df = df.sort_index()  # Sort by date
            
            if len(df) == 0:
                logger.warning("No valid dates found in metadata")
                return
            
            # Posts per month
            plt.figure(figsize=(15, 6))
            monthly_posts = df.resample('M').size()
            monthly_posts.plot(kind='bar')
            plt.title('Posts per Month')
            plt.xlabel('Month')
            plt.ylabel('Number of Posts')
            plt.xticks(rotation=45)
            plt.tight_layout()
            if not save_plot(plt, self.temporal_dir / 'posts_per_month.png'):
                raise Exception("Failed to save posts_per_month.png")
            
            # Posts by day of week
            plt.figure(figsize=(10, 6))
            df['day_of_week'] = df.index.day_name()
            day_order = list(calendar.day_name)
            day_counts = df['day_of_week'].value_counts().reindex(day_order)
            day_counts.plot(kind='bar')
            plt.title('Posts by Day of Week')
            plt.xlabel('Day of Week')
            plt.ylabel('Number of Posts')
            plt.xticks(rotation=45)
            plt.tight_layout()
            if not save_plot(plt, self.temporal_dir / 'posts_by_weekday.png'):
                raise Exception("Failed to save posts_by_weekday.png")
            
            logger.info("Generated temporal visualizations")
            
        except Exception as e:
            logger.error(f"Error generating temporal visualizations: {str(e)}")
            plt.close('all')

    def generate_content_analysis(self):
        """Generate content analysis visualizations"""
        try:
            contents = self.load_post_contents()
            
            # Advanced word cloud with custom styling
            text = " ".join(contents.values())
            wordcloud = WordCloud(
                width=1920,
                height=1080,
                background_color='white',
                colormap='viridis',
                max_words=200,
                contour_width=3,
                contour_color='steelblue'
            ).generate(text)
            
            plt.figure(figsize=(24, 13.5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.tight_layout(pad=0)
            plt.savefig(self.content_dir / 'advanced_wordcloud.png', dpi=300)
            plt.close()
            
            # Sentiment analysis
            sentiments = []
            for content in contents.values():
                blob = TextBlob(content)
                sentiments.append(blob.sentiment.polarity)
            
            plt.figure(figsize=(12, 6))
            plt.hist(sentiments, bins=30, color='skyblue', edgecolor='black')
            plt.title('Content Sentiment Distribution')
            plt.xlabel('Sentiment Polarity (-1 to 1)')
            plt.ylabel('Number of Posts')
            plt.tight_layout()
            plt.savefig(self.content_dir / 'sentiment_distribution.png')
            plt.close()
            
            # Top keywords using TF-IDF
            vectorizer = TfidfVectorizer(max_features=20, stop_words='english')
            tfidf_matrix = vectorizer.fit_transform(contents.values())
            feature_names = vectorizer.get_feature_names_out()
            tfidf_scores = tfidf_matrix.sum(axis=0).A1
            
            plt.figure(figsize=(12, 6))
            plt.bar(feature_names, tfidf_scores)
            plt.title('Top Keywords by TF-IDF Score')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(self.content_dir / 'keyword_importance.png')
            plt.close()
            
            logger.info("Generated content analysis visualizations")
            
        except Exception as e:
            logger.error(f"Error generating content analysis: {str(e)}")

    def generate_network_visualizations(self):
        """Generate network visualizations"""
        try:
            metadata = self.load_metadata()
            
            # Create graph
            G = nx.Graph()
            
            # Add nodes and edges
            for post in metadata:
                post_id = post.get('id', str(uuid.uuid4()))
                G.add_node(post_id, title=post.get('title', 'Unknown'))
                
                # Add edges for links between posts
                for link in post.get('links', []):
                    if link in [p.get('id') for p in metadata]:
                        G.add_edge(post_id, link)
            
            if len(G.nodes()) == 0:
                logger.warning("No nodes found for network visualization")
                return
                
            if len(G.edges()) == 0:
                logger.warning("No edges found for network visualization")
                return
            
            # Network visualization
            plt.figure(figsize=(20, 20))
            pos = nx.spring_layout(G)
            nx.draw(G, pos, 
                   node_color='lightblue',
                   node_size=1000,
                   with_labels=True,
                   font_size=8,
                   font_weight='bold',
                   edge_color='gray',
                   alpha=0.7)
            plt.title('Blog Post Link Network')
            plt.tight_layout()
            save_plot(plt, self.network_dir / 'post_network.png')
            
            # Network metrics
            metrics = {
                'Density': nx.density(G),
                'Average Clustering': nx.average_clustering(G) if len(G.nodes()) > 1 else 0,
                'Number of Connected Components': nx.number_connected_components(G),
                'Number of Nodes': len(G.nodes()),
                'Number of Edges': len(G.edges())
            }
            
            with open(self.network_dir / 'network_metrics.json', 'w') as f:
                json.dump(metrics, f, indent=2)
            
            logger.info("Generated network visualizations")
            
        except Exception as e:
            logger.error(f"Error generating network visualizations: {str(e)}")
            plt.close('all')

    def generate_engagement_metrics(self):
        """Generate engagement-related visualizations"""
        try:
            metadata = self.load_metadata()
            df = pd.DataFrame(metadata)
            
            if 'comments' in df.columns and 'shares' in df.columns:
                # Engagement over time
                plt.figure(figsize=(15, 6))
                df['date'] = pd.to_datetime(df['date'])
                df.plot(x='date', y=['comments', 'shares'], kind='line', marker='o')
                plt.title('Engagement Metrics Over Time')
                plt.xlabel('Date')
                plt.ylabel('Count')
                plt.legend(['Comments', 'Shares'])
                plt.tight_layout()
                plt.savefig(self.engagement_dir / 'engagement_timeline.png')
                plt.close()
                
                # Engagement correlation
                plt.figure(figsize=(8, 8))
                sns.scatterplot(data=df, x='comments', y='shares')
                plt.title('Comments vs Shares Correlation')
                plt.tight_layout()
                plt.savefig(self.engagement_dir / 'engagement_correlation.png')
                plt.close()
            
            logger.info("Generated engagement visualizations")
            
        except Exception as e:
            logger.error(f"Error generating engagement visualizations: {str(e)}")

    def generate_all_visualizations(self):
        """Generate all available visualizations with comprehensive logging"""
        logger.info("Starting comprehensive visualization generation")
        logger.info("=" * 80)
        
        start_time = datetime.now()
        
        try:
            with Timer("Temporal visualizations", logger):
                self.generate_temporal_visualizations()
                
            with Timer("Content analysis", logger):
                self.generate_content_analysis()
                
            with Timer("Network visualizations", logger):
                self.generate_network_visualizations()
                
            with Timer("Engagement metrics", logger):
                self.generate_engagement_metrics()
            
            # Generate and save overall statistics
            with Timer("Statistics generation", logger):
                stats_file = self.verification_dir / 'blog_statistics.json'
                with open(stats_file, 'w') as f:
                    json.dump(self.stats, f, indent=2)
                
                # Generate summary visualization
                self._generate_summary_visualization()
            
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            logger.info("=" * 80)
            logger.info("Visualization Generation Summary")
            logger.info("-" * 80)
            logger.info(f"Total time: {duration:.2f} seconds")
            logger.info(f"Total posts processed: {self.stats['total_posts']:,}")
            logger.info(f"Total words analyzed: {self.stats['total_words']:,}")
            logger.info(f"Total links processed: {self.stats['total_links']:,}")
            logger.info(f"Average words per post: {self.stats['total_words']/self.stats['total_posts']:.1f}")
            logger.info("=" * 80)
            
        except Exception as e:
            logger.error(f"Error in visualization generation: {str(e)}")
            raise

    def _generate_summary_visualization(self):
        """Generate a summary visualization of all metrics"""
        try:
            plt.figure(figsize=(15, 10))
            
            # Update stats with date information
            metadata = self.load_metadata()
            df = pd.DataFrame(metadata)
            df['date'] = pd.to_datetime(df['published'].fillna(df.get('date')), utc=True)
            self.stats['first_post_date'] = df['date'].min().isoformat()
            self.stats['last_post_date'] = df['date'].max().isoformat()
            
            metrics = {
                'Posts': self.stats['total_posts'],
                'Words': self.stats['total_words'] / 1000,  # Show in thousands
                'Links': self.stats['total_links'],
                'Comments': self.stats.get('total_comments', 0),
                'Shares': self.stats.get('total_shares', 0)
            }
            
            plt.bar(metrics.keys(), metrics.values(), color='skyblue')
            plt.title('Blog Overview Metrics')
            plt.ylabel('Count (Words in thousands)')
            plt.xticks(rotation=45)
            
            # Add value labels on top of each bar
            for i, v in enumerate(metrics.values()):
                plt.text(i, v, f'{v:,.0f}', ha='center', va='bottom')
            
            plt.tight_layout()
            save_plot(plt, self.verification_dir / 'summary_metrics.png')
            plt.close()
            
            # Save blog statistics
            stats_file = self.verification_dir / 'blog_statistics.json'
            with open(stats_file, 'w') as f:
                json.dump(self.stats, f, indent=2)
            
            logger.info("Generated summary visualization and saved statistics")
            
        except Exception as e:
            logger.error(f"Error generating summary visualization: {str(e)}")

def generate_comparative_visualizations(all_stats: Dict):
    """Generate comparative visualizations across all blogs"""
    try:
        logger.info("Starting comparative visualization generation")
        logger.info("=" * 80)
        
        with Timer("Comparative visualizations", logger):
            # Set the Agg backend for non-interactive environments
            plt.switch_backend('Agg')
            
            comparative_dir = Path("fonds/blogs/comparative_analysis")
            comparative_dir.mkdir(parents=True, exist_ok=True)
            
            # Clear existing files
            for file in comparative_dir.glob("*"):
                try:
                    file.unlink()
                except Exception as e:
                    logger.error(f"Error removing file {file}: {str(e)}")
            
            # Filter out any stats without required numerical data
            valid_stats = {
                name: stats for name, stats in all_stats.items() 
                if 'total_posts' in stats and 'total_words' in stats and stats['total_posts'] > 0
            }
            
            if not valid_stats:
                logger.error("No valid statistics found for comparative visualizations")
                return
            
            logger.info(f"Processing comparative statistics for {len(valid_stats)} blogs")
            
            # Compare post counts
            plt.figure(figsize=(12, 6))
            post_counts = {name: stats['total_posts'] for name, stats in valid_stats.items()}
            plt.bar(list(post_counts.keys()), list(post_counts.values()))
            plt.title('Post Count Comparison Across Blogs')
            plt.xticks(rotation=45, ha='right')
            plt.ylabel('Number of Posts')
            plt.tight_layout()
            save_plot(plt, comparative_dir / 'post_counts_comparison.png')
            plt.close('all')
            
            # Compare word counts
            plt.figure(figsize=(12, 6))
            word_counts = {name: stats['total_words'] for name, stats in valid_stats.items()}
            plt.bar(list(word_counts.keys()), list(word_counts.values()))
            plt.title('Total Words Comparison Across Blogs')
            plt.xticks(rotation=45, ha='right')
            plt.ylabel('Total Words')
            plt.tight_layout()
            save_plot(plt, comparative_dir / 'word_counts_comparison.png')
            plt.close('all')
            
            # Create blog timeline
            plt.figure(figsize=(15, 6))
            timeline_data = {}
            for name, stats in valid_stats.items():
                if 'first_post_date' in stats and 'last_post_date' in stats:
                    try:
                        start = pd.to_datetime(stats['first_post_date'])
                        end = pd.to_datetime(stats['last_post_date'])
                        timeline_data[name] = (start, end)
                    except (ValueError, TypeError):
                        logger.warning(f"Invalid date format for blog {name}")
                        continue
            
            if timeline_data:
                for name, (start, end) in timeline_data.items():
                    plt.hlines(y=name, xmin=start, xmax=end, linewidth=4)
                plt.title('Blog Timeline Comparison')
                plt.xlabel('Date')
                plt.grid(True)
                plt.tight_layout()
                save_plot(plt, comparative_dir / 'blog_timeline.png')
                plt.close('all')
            
            # Average post length comparison
            plt.figure(figsize=(12, 6))
            avg_lengths = {}
            for name, stats in valid_stats.items():
                if stats['total_posts'] > 0:
                    avg_lengths[name] = stats['total_words'] / stats['total_posts']
            
            if avg_lengths:
                plt.bar(list(avg_lengths.keys()), list(avg_lengths.values()))
                plt.title('Average Post Length Comparison')
                plt.xticks(rotation=45, ha='right')
                plt.ylabel('Average Words per Post')
                plt.tight_layout()
                save_plot(plt, comparative_dir / 'avg_post_length_comparison.png')
                plt.close('all')
            
            # Save comparative statistics
            comparative_stats = {
                'total_posts_all_blogs': sum(stats['total_posts'] for stats in valid_stats.values()),
                'total_words_all_blogs': sum(stats['total_words'] for stats in valid_stats.values()),
                'posts_per_blog': post_counts,
                'words_per_blog': word_counts,
                'average_post_length': avg_lengths,
                'blog_date_ranges': {
                    name: {
                        'first_post': stats.get('first_post_date', 'unknown'),
                        'last_post': stats.get('last_post_date', 'unknown')
                    } for name, stats in valid_stats.items()
                }
            }
            
            with open(comparative_dir / 'comparative_stats.json', 'w') as f:
                json.dump(comparative_stats, f, indent=2)
            
            logger.info("Comparative Visualization Summary")
            logger.info("-" * 80)
            logger.info(f"Total blogs processed: {len(valid_stats)}")
            logger.info(f"Total posts across all blogs: {sum(stats['total_posts'] for stats in valid_stats.values()):,}")
            logger.info(f"Total words across all blogs: {sum(stats['total_words'] for stats in valid_stats.values()):,}")
            logger.info("=" * 80)
            
    except Exception as e:
        logger.error(f"Error generating comparative visualizations: {str(e)}")
        plt.close('all')  # Ensure all figures are closed even if there's an error

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate visualizations from blog data')
    parser.add_argument('--blog_dir', type=str,
                      help='Path to a specific blog directory to process')
    parser.add_argument('--verify', action='store_true',
                      help='Enable verification checks')
    
    args = parser.parse_args()
    
    try:
        # Set the Agg backend for non-interactive environments
        plt.switch_backend('Agg')
        
        if args.blog_dir:
            # Process single blog
            visualizer = BlogVisualizer(Path(args.blog_dir), verification_enabled=args.verify)
            visualizer.generate_all_visualizations()
            logger.info("Single blog visualization completed successfully")
        else:
            # Process all blogs in fonds/blogs directory
            blogs_root = Path("fonds/blogs")
            blog_dirs = [
                d for d in blogs_root.iterdir() 
                if d.is_dir() and d.name not in ['logs', 'comparative_analysis']
            ]
            
            if not blog_dirs:
                logger.error("No blog directories found in fonds/blogs/")
                sys.exit(1)
                
            logger.info(f"Found {len(blog_dirs)} blog directories")
            
            # First process all blogs and collect stats
            all_stats = {}
            successful_blogs = 0
            
            # Process each blog
            for blog_dir in blog_dirs:
                try:
                    logger.info(f"Processing blog: {blog_dir.name}")
                    visualizer = BlogVisualizer(blog_dir)
                    visualizer.generate_all_visualizations()
                    
                    # Load the statistics file - changed from blog_statistics.json to data_verification.json
                    stats_file = blog_dir / 'visualizations' / 'verification' / 'data_verification.json'
                    if stats_file.exists():
                        with open(stats_file, 'r') as f:
                            all_stats[blog_dir.name] = json.load(f)
                        successful_blogs += 1
                        logger.info(f"Successfully processed blog: {blog_dir.name}")
                    else:
                        logger.error(f"Statistics file not found for blog: {blog_dir.name}")
                except Exception as e:
                    logger.error(f"Error processing blog {blog_dir}: {str(e)}")
                finally:
                    plt.close('all')  # Ensure figures are closed after each blog
            
            logger.info(f"Successfully processed {successful_blogs} out of {len(blog_dirs)} blogs")
            
            # Generate comparative visualizations only after all blogs are processed
            if successful_blogs > 0:
                try:
                    logger.info("Starting comparative visualization generation...")
                    generate_comparative_visualizations(all_stats)
                    logger.info("Successfully generated comparative visualizations")
                except Exception as e:
                    logger.error(f"Error generating comparative visualizations: {str(e)}")
                    raise
                finally:
                    plt.close('all')  # Ensure all figures are closed
            else:
                logger.error("No blogs were successfully processed")
                sys.exit(1)
            
    except Exception as e:
        logger.error(f"Error during visualization: {str(e)}")
        plt.close('all')  # Ensure all figures are closed in case of error
        sys.exit(1) 