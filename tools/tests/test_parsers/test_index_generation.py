#!/usr/bin/env python3

import unittest
import os
import sys
from pathlib import Path
import shutil
import tempfile
import yaml
from datetime import datetime

# Add parent directory to path to import parsers
sys.path.append(str(Path(__file__).parent.parent.parent))

from parsers.obsidian_indexer import ObsidianIndexer, FileMetadata

class TestObsidianIndexer(unittest.TestCase):
    """Test suite for ObsidianIndexer class."""

    def setUp(self):
        """Set up test environment before each test."""
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.indexer = ObsidianIndexer(self.test_dir)
        
        # Create test folder structure
        self.folders = ['books', 'mathematics', 'formalisms', 'people', 'places']
        for folder in self.folders:
            os.makedirs(os.path.join(self.test_dir, folder))

    def tearDown(self):
        """Clean up test environment after each test."""
        shutil.rmtree(self.test_dir)

    def create_test_file(self, folder: str, filename: str, content: str) -> None:
        """Create a test markdown file."""
        filepath = os.path.join(self.test_dir, folder, f"{filename}.md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    def test_folder_metadata(self):
        """Test folder metadata assignment and retrieval."""
        test_metadata = {
            'books': ('📚', 'Books and publications'),
            'mathematics': ('🔢', 'Mathematical concepts'),
            'formalisms': ('📏', 'Formal systems and notations')
        }
        
        for folder, (emoji, desc) in test_metadata.items():
            self.indexer.set_folder_metadata(folder, emoji, desc)
            self.assertEqual(
                self.indexer.folder_metadata[folder],
                (emoji, desc)
            )

    def test_index_generation(self):
        """Test index file generation for different folder types."""
        # Create test files with known locations
        test_files = {
            'books': [
                ('test_book', '# Test Book\nContent'),
                ('another_book', '# Another Book\n[[test_book]]')
            ],
            'mathematics': [
                ('vector_math', '# Vector Math\nContent'),
                ('geometry', '# Geometry\n[[vector_math]]')
            ]
        }
        
        # Create all test files
        for folder, files in test_files.items():
            for filename, content in files:
                self.create_test_file(folder, filename, content)
        
        # Set metadata
        self.indexer.set_folder_metadata('books', '📚', 'Test books')
        self.indexer.set_folder_metadata('mathematics', '🔢', 'Test math')
        
        # Generate indices
        self.indexer.scan_directory(Path(self.test_dir))
        self.indexer.generate_clean_index_files()
        
        # Verify index files and their contents
        for folder, files in test_files.items():
            index_path = os.path.join(self.test_dir, folder, f"{folder}_index.md")
            self.assertTrue(os.path.exists(index_path))
            
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Check basic structure
                self.assertIn('title:', content)
                self.assertIn('emoji:', content)
                self.assertIn('## Contents', content)
                
                # Verify file count in frontmatter
                self.assertIn(f'total_files: {len(files)}', content)
                
                # Check that all files are linked
                for filename, _ in files:
                    self.assertIn(f'[[{filename}]]', content)
                
                # Verify folder stats were updated
                folder_stats = self.indexer.folder_stats.get(folder)
                self.assertIsNotNone(folder_stats)
                self.assertEqual(folder_stats.total_files, len(files))
                self.assertEqual(len(folder_stats.files), len(files))

    def test_empty_folder_handling(self):
        """Test handling of empty folders."""
        # Set metadata for empty folder
        self.indexer.set_folder_metadata('formalisms', '📏', 'Test formalisms')
        
        # Generate indices
        self.indexer.scan_directory(Path(self.test_dir))
        self.indexer.generate_clean_index_files()
        
        # Verify empty folder index
        index_path = os.path.join(self.test_dir, 'formalisms', 'formalisms_index.md')
        self.assertTrue(os.path.exists(index_path))
        
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn('title: Formalisms Index', content)
            self.assertIn('## Contents', content)
            self.assertIn('total_files: 0', content)
            # Empty folders should just have the header and no file listings
            self.assertNotIn('[[', content)
            
        # Verify folder stats for empty folder
        folder_stats = self.indexer.folder_stats.get('formalisms')
        self.assertIsNotNone(folder_stats)
        self.assertEqual(folder_stats.total_files, 0)
        self.assertEqual(len(folder_stats.files), 0)

    def test_link_extraction(self):
        """Test extraction of Obsidian links."""
        content = """
        # Test File
        [[Link1]]
        Some text with [[Link2|Alias]] and [[Link3]]
        """
        
        self.create_test_file('books', 'test_links', content)
        self.indexer.scan_directory(Path(self.test_dir))
        
        # Verify links were extracted
        file_links = self.indexer.file_links.get('test_links', [])
        self.assertIn('Link1', file_links)
        self.assertIn('Link2', file_links)
        self.assertIn('Link3', file_links)

    def test_frontmatter_handling(self):
        """Test handling of YAML frontmatter."""
        content = """---
        title: Test File
        tags:
          - test
          - example
        related:
          - Related1
          - Related2
        ---
        # Content
        """
        
        self.create_test_file('books', 'test_frontmatter', content)
        self.indexer.scan_directory(Path(self.test_dir))
        
        metadata = self.indexer.file_metadata.get('test_frontmatter')
        self.assertIsNotNone(metadata)
        self.assertIn('test', metadata.tags)
        self.assertIn('example', metadata.tags)

    def test_statistics_generation(self):
        """Test generation of folder statistics."""
        # Create test files with links
        content1 = "[[Link1]] [[Link2]]"
        content2 = "[[Link3]]"
        
        self.create_test_file('books', 'file1', content1)
        self.create_test_file('books', 'file2', content2)
        
        self.indexer.scan_directory(Path(self.test_dir))
        self.indexer.update_folder_stats()
        
        stats = self.indexer.folder_stats.get('books')
        self.assertIsNotNone(stats)
        self.assertEqual(stats.total_files, 2)

def run_tests():
    """Run the test suite and generate a test report."""
    # Create test result directory
    result_dir = Path(__file__).parent.parent / 'test_results'
    result_dir.mkdir(exist_ok=True)
    
    # Run tests with custom test runner
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(unittest.TestLoader().loadTestsFromTestCase(TestObsidianIndexer))
    
    # Generate test report
    report = {
        'timestamp': datetime.now().isoformat(),
        'tests_run': result.testsRun,
        'failures': len(result.failures),
        'errors': len(result.errors),
        'skipped': len(result.skipped),
        'success': result.wasSuccessful()
    }
    
    # Save report
    report_path = result_dir / f'test_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.yaml'
    with open(report_path, 'w') as f:
        yaml.dump(report, f)
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1) 