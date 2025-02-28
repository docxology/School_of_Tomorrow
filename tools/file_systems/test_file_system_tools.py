#!/usr/bin/env python3
"""
Test Suite for File System Analysis Tools
---------------------------------------
Comprehensive tests for file system analysis functionality.
"""

import os
import json
import tempfile
import shutil
from pathlib import Path
import pytest
from datetime import datetime, timedelta
import pandas as pd
from file_system_tools import FileSystemAnalyzer

class TestFileSystemAnalyzer:
    @pytest.fixture
    def temp_directory(self):
        """Create a temporary directory with a known structure for testing."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a test directory structure
            root = Path(tmpdir)
            
            # Create some directories
            (root / "dir1").mkdir()
            (root / "dir1" / "subdir1").mkdir()
            (root / "dir2").mkdir()
            
            # Create some files
            (root / "file1.txt").write_text("Test file 1")
            (root / "dir1" / "file2.md").write_text("Test file 2")
            (root / "dir1" / "subdir1" / "file3.py").write_text("print('Test file 3')")
            
            yield root
            
    def test_initialization(self, temp_directory):
        """Test analyzer initialization."""
        analyzer = FileSystemAnalyzer(temp_directory)
        assert analyzer.root_path == temp_directory
        assert '.git' in analyzer.ignored_patterns
        
    def test_get_file_stats(self, temp_directory):
        """Test file statistics gathering."""
        analyzer = FileSystemAnalyzer(temp_directory)
        stats = analyzer.get_file_stats(temp_directory / "file1.txt")
        
        assert isinstance(stats, dict)
        assert all(key in stats for key in ['size', 'created', 'modified', 'is_dir', 'extension'])
        assert stats['extension'] == 'txt'
        assert not stats['is_dir']
        assert isinstance(stats['created'], datetime)
        
    def test_generate_tree_text(self, temp_directory):
        """Test text tree generation."""
        analyzer = FileSystemAnalyzer(temp_directory)
        tree = analyzer.generate_tree(format='text')
        
        assert isinstance(tree, str)
        assert "file1.txt" in tree
        assert "dir1" in tree
        assert "subdir1" in tree
        
    def test_generate_tree_obsidian(self, temp_directory):
        """Test Obsidian-compatible tree generation."""
        analyzer = FileSystemAnalyzer(temp_directory)
        tree = analyzer.generate_tree(format='obsidian')
        
        assert isinstance(tree, str)
        assert "[[file1.txt]]" in tree
        assert "[[dir1/file2.md]]" in tree
        
    def test_generate_tree_json(self, temp_directory):
        """Test JSON tree generation."""
        analyzer = FileSystemAnalyzer(temp_directory)
        tree = analyzer.generate_tree(format='json')
        
        parsed = json.loads(tree)
        assert isinstance(parsed, dict)
        assert 'type' in parsed
        assert 'name' in parsed
        assert 'contents' in parsed
        
    def test_generate_statistics(self, temp_directory):
        """Test statistics generation."""
        analyzer = FileSystemAnalyzer(temp_directory)
        stats = analyzer.generate_statistics()
        
        assert isinstance(stats, pd.DataFrame)
        assert not stats.empty
        assert all(col in stats.columns for col in ['path', 'type', 'size', 'extension'])
        
    def test_visualize_structure(self, temp_directory):
        """Test visualization generation."""
        analyzer = FileSystemAnalyzer(temp_directory)
        output_path = temp_directory / "test_viz.html"
        analyzer.visualize_structure(str(output_path))
        
        assert output_path.exists()
        assert output_path.stat().st_size > 0
        
    def test_max_depth_limit(self, temp_directory):
        """Test max depth limitation in tree generation."""
        analyzer = FileSystemAnalyzer(temp_directory)
        tree = analyzer.generate_tree(max_depth=1)
        
        assert isinstance(tree, str)
        assert "..." in tree  # Should show truncation
        assert "file3.py" not in tree  # Should not show deepest file
        
    def test_ignored_patterns(self, temp_directory):
        """Test ignored patterns functionality."""
        # Create a .git directory that should be ignored
        (temp_directory / ".git").mkdir()
        (temp_directory / ".git" / "config").write_text("test")
        
        analyzer = FileSystemAnalyzer(temp_directory)
        tree = analyzer.generate_tree()
        
        assert ".git" not in tree
        
    def test_include_stats(self, temp_directory):
        """Test inclusion of statistics in tree generation."""
        analyzer = FileSystemAnalyzer(temp_directory)
        tree = analyzer.generate_tree(include_stats=True)
        
        assert isinstance(tree, str)
        assert "bytes" in tree  # Should show file sizes
        
    def test_error_handling(self, temp_directory):
        """Test error handling for inaccessible paths."""
        restricted_dir = temp_directory / "restricted"
        restricted_dir.mkdir()
        restricted_file = restricted_dir / "secret.txt"
        restricted_file.write_text("secret")
        
        # Make directory inaccessible (platform-dependent)
        try:
            os.chmod(restricted_dir, 0o000)
            
            analyzer = FileSystemAnalyzer(temp_directory)
            tree = analyzer.generate_tree()
            
            assert isinstance(tree, str)
            assert "restricted" in tree  # Directory should be listed
            assert "secret.txt" not in tree  # But its contents should not be
        finally:
            os.chmod(restricted_dir, 0o755)  # Restore permissions

if __name__ == "__main__":
    pytest.main([__file__]) 