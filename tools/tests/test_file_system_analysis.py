#!/usr/bin/env python3

import unittest
import sys
import os
from pathlib import Path
import json
import logging
from datetime import datetime
import shutil

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from file_systems.enhanced_file_analysis import EnhancedFileAnalyzer

class TestFileSystemAnalysis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test environment and logging."""
        # Setup test output directory
        cls.test_output_dir = Path(__file__).parent / 'test_outputs'
        cls.test_output_dir.mkdir(exist_ok=True)
        
        # Setup logging
        log_dir = Path(__file__).parent / 'logs'
        log_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f'file_system_test_{timestamp}.log'
        
        cls.logger = logging.getLogger(__name__)
        cls.logger.setLevel(logging.DEBUG)
        
        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        ))
        cls.logger.addHandler(file_handler)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter(
            '%(levelname)s: %(message)s'
        ))
        cls.logger.addHandler(console_handler)
        
        # Initialize analyzer
        cls.repo_root = Path(__file__).parent.parent.parent
        cls.analyzer = EnhancedFileAnalyzer(cls.repo_root)
        cls.timestamp = timestamp

    def setUp(self):
        """Log the start of each test."""
        self.logger.info(f"\nStarting test: {self._testMethodName}")

    def test_tree_generation(self):
        """Test tree visualization generation with different formats and depths."""
        self.logger.info("Testing tree generation...")
        
        # Test text format with different depths
        for depth in [2, 3, 5]:
            tree = self.analyzer.generate_tree(format='text', max_depth=depth)
            self.assertIsNotNone(tree)
            
            output_file = self.test_output_dir / f'tree_depth_{depth}_{self.timestamp}.txt'
            output_file.write_text(tree)
            self.logger.info(f"Generated text tree with depth {depth}")
            
            # Verify content
            self.assertTrue(output_file.exists())
            content = output_file.read_text()
            self.assertIn(str(self.repo_root.name), content)
        
        # Test markdown format
        md_tree = self.analyzer.generate_tree(format='markdown')
        self.assertIsNotNone(md_tree)
        
        md_output = self.test_output_dir / f'tree_{self.timestamp}.md'
        md_output.write_text(md_tree)
        self.logger.info("Generated markdown tree")

    def test_directory_statistics(self):
        """Test directory statistics generation and visualization."""
        self.logger.info("Testing directory statistics...")
        
        important_dirs = ['tools', 'tests', 'docs']
        stats_file = self.test_output_dir / f'directory_stats_{self.timestamp}.md'
        
        with open(stats_file, 'w') as f:
            f.write("# Directory Statistics Report\n\n")
            
            for dirname in important_dirs:
                dir_path = self.repo_root / dirname
                if dir_path.exists():
                    f.write(f"## {dirname}\n\n")
                    stats = self.analyzer._get_directory_stats(dir_path)
                    
                    # Log and verify basic stats
                    self.logger.info(f"Analyzing directory: {dirname}")
                    self.logger.debug(f"Stats for {dirname}: {stats}")
                    
                    self.assertIsInstance(stats, dict)
                    self.assertIn('file_count', stats)
                    self.assertIn('dir_count', stats)
                    self.assertIn('total_size', stats)
                    
                    # Write stats to report
                    f.write(f"- Files: {stats['file_count']}\n")
                    f.write(f"- Directories: {stats['dir_count']}\n")
                    f.write(f"- Total size: {self.analyzer._format_size(stats['total_size'])}\n\n")
                    
                    if stats['extensions']:
                        f.write("### File Types\n")
                        for ext, count in sorted(stats['extensions'].items(), 
                                              key=lambda x: x[1], reverse=True):
                            f.write(f"- {ext}: {count}\n")
                    f.write("\n")

    def test_file_type_analysis(self):
        """Test file type analysis and visualization."""
        self.logger.info("Testing file type analysis...")
        
        summary_file = self.test_output_dir / f'file_type_summary_{self.timestamp}.md'
        all_files = list(self.repo_root.rglob('*'))
        type_stats = {}
        
        for file_path in all_files:
            if file_path.is_file() and not any(ignored in str(file_path) 
                                             for ignored in self.analyzer.ignored_patterns):
                stats = self.analyzer.get_file_stats(file_path)
                mime_type = stats['mime_type']
                
                if mime_type not in type_stats:
                    type_stats[mime_type] = {
                        'count': 0,
                        'total_size': 0,
                        'examples': []
                    }
                
                type_stats[mime_type]['count'] += 1
                type_stats[mime_type]['total_size'] += stats['size']
                
                if len(type_stats[mime_type]['examples']) < 3:
                    type_stats[mime_type]['examples'].append(
                        str(file_path.relative_to(self.repo_root))
                    )
        
        # Write summary report
        with open(summary_file, 'w') as f:
            f.write("# File Type Summary\n\n")
            
            for mime_type, stats in sorted(type_stats.items(), 
                                         key=lambda x: x[1]['count'], reverse=True):
                icon = self.analyzer._get_file_icon({
                    'mime_type': mime_type, 
                    'is_dir': False, 
                    'is_symlink': False
                })
                
                f.write(f"## {icon} {mime_type}\n\n")
                f.write(f"- Count: {stats['count']}\n")
                f.write(f"- Total size: {self.analyzer._format_size(stats['total_size'])}\n")
                f.write("- Example files:\n")
                for example in stats['examples']:
                    f.write(f"  - `{example}`\n")
                f.write("\n")
                
                self.logger.info(f"Analyzed MIME type: {mime_type} "
                               f"(Count: {stats['count']})")

    def test_visualization_data_generation(self):
        """Test generation of visualization data in JSON format."""
        self.logger.info("Testing visualization data generation...")
        
        json_file = self.test_output_dir / f'visualization_data_{self.timestamp}.json'
        
        # Generate visualization data
        data = {
            'fileTypes': {},
            'directorySizes': {},
            'mimeTypes': {},
            'recentChanges': [],
            'largestFiles': []
        }
        
        # Collect file type statistics
        all_files = list(self.repo_root.rglob('*'))
        for file_path in all_files:
            if file_path.is_file() and not any(ignored in str(file_path) 
                                             for ignored in self.analyzer.ignored_patterns):
                stats = self.analyzer.get_file_stats(file_path)
                
                # Update file type counts
                ext = file_path.suffix
                if ext:
                    data['fileTypes'][ext] = data['fileTypes'].get(ext, 0) + 1
                
                # Update MIME type counts
                mime_type = stats['mime_type']
                data['mimeTypes'][mime_type] = data['mimeTypes'].get(mime_type, 0) + 1
                
                # Track recent changes
                if len(data['recentChanges']) < 10:
                    data['recentChanges'].append({
                        'path': str(file_path.relative_to(self.repo_root)),
                        'modified': stats['modified'].isoformat(),
                        'size': stats['size']
                    })
                
                # Track largest files
                data['largestFiles'].append({
                    'path': str(file_path.relative_to(self.repo_root)),
                    'size': stats['size']
                })
        
        # Sort and limit largest files
        data['largestFiles'].sort(key=lambda x: x['size'], reverse=True)
        data['largestFiles'] = data['largestFiles'][:10]
        
        # Write visualization data
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        self.logger.info(f"Generated visualization data: {json_file}")
        
        # Verify data
        with open(json_file) as f:
            loaded_data = json.load(f)
        
        self.assertIn('fileTypes', loaded_data)
        self.assertIn('directorySizes', loaded_data)
        self.assertIn('mimeTypes', loaded_data)
        self.assertIn('recentChanges', loaded_data)
        self.assertIn('largestFiles', loaded_data)

    @classmethod
    def tearDownClass(cls):
        """Clean up test outputs if needed."""
        cls.logger.info("\nTest suite completed")

def run_file_system_tests():
    """Run the file system analysis test suite."""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFileSystemAnalysis)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()

if __name__ == '__main__':
    run_file_system_tests() 