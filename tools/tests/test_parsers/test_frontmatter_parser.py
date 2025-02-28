import unittest
from pathlib import Path
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from parsers.frontmatter_parser import FrontmatterParser

class TestFrontmatterParser(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.test_data_dir = Path(__file__).parent / 'test_data'
        self.parser = FrontmatterParser()
        
        # Create test data directory if it doesn't exist
        self.test_data_dir.mkdir(exist_ok=True)
        
    def test_basic_frontmatter(self):
        """Test parsing of basic frontmatter with common fields."""
        test_content = """---
title: Test Note
date: 2024-02-26
tags: [test, example]
---
# Content
"""
        expected = {
            'title': 'Test Note',
            'date': '2024-02-26',
            'tags': ['test', 'example']
        }
        
        # Write test file
        test_file = self.test_data_dir / 'basic_frontmatter.md'
        test_file.write_text(test_content)
        
        result = self.parser.parse(test_file)
        self.assertEqual(result, expected)
        
    def test_invalid_frontmatter(self):
        """Test handling of invalid frontmatter."""
        test_content = """---
invalid: yaml:
  - unclosed
# Content
"""
        test_file = self.test_data_dir / 'invalid_frontmatter.md'
        test_file.write_text(test_content)
        
        with self.assertRaises(ValueError):
            self.parser.parse(test_file)
            
    def test_no_frontmatter(self):
        """Test handling of files without frontmatter."""
        test_content = "# Just a regular note\nNo frontmatter here."
        test_file = self.test_data_dir / 'no_frontmatter.md'
        test_file.write_text(test_content)
        
        result = self.parser.parse(test_file)
        self.assertEqual(result, {})
        
    def test_complex_frontmatter(self):
        """Test parsing of complex nested frontmatter."""
        test_content = """---
metadata:
  created: 2024-02-26
  modified: 2024-02-26
  status: in-progress
aliases: 
  - First Test
  - Example Test
relationships:
  parent: Parent Note
  children:
    - Child Note 1
    - Child Note 2
---
# Content
"""
        test_file = self.test_data_dir / 'complex_frontmatter.md'
        test_file.write_text(test_content)
        
        result = self.parser.parse(test_file)
        self.assertIsInstance(result['metadata'], dict)
        self.assertIsInstance(result['aliases'], list)
        self.assertEqual(len(result['aliases']), 2)
        self.assertIsInstance(result['relationships']['children'], list)
        
    def tearDown(self):
        """Clean up test files."""
        for file in self.test_data_dir.glob('*.md'):
            file.unlink()
            
if __name__ == '__main__':
    unittest.main() 