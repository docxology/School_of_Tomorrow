#!/usr/bin/env python3
"""
Test Suite for Enhanced File System Analysis
-----------------------------------------
Comprehensive tests for enhanced file system analysis functionality.
"""

import os
import json
import tempfile
import shutil
from pathlib import Path
import pytest
from datetime import datetime
import subprocess
from enhanced_file_analysis import EnhancedFileAnalyzer

class TestEnhancedFileAnalyzer:
    @pytest.fixture
    def temp_directory(self):
        """Create a temporary directory with a known structure for testing."""
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            
            # Create test directory structure
            (root / "docs").mkdir()
            (root / "docs" / "images").mkdir()
            (root / "src").mkdir()
            (root / "src" / "lib").mkdir()
            
            # Create various file types
            (root / "README.md").write_text("# Test Repository\nThis is a test.")
            (root / "docs" / "guide.md").write_text("# User Guide\nTest guide content.")
            (root / "src" / "main.py").write_text("print('Hello, World!')")
            (root / "src" / "lib" / "utils.py").write_text("def test(): pass")
            (root / "docs" / "images" / "diagram.png").write_bytes(b"fake png content")
            (root / "config.json").write_text('{"test": true}')
            (root / "data.txt").write_text("Test data")
            
            # Create a symlink
            os.symlink(root / "README.md", root / "README.link")
            
            # Initialize git repository
            subprocess.run(['git', 'init'], cwd=root, capture_output=True)
            subprocess.run(['git', 'config', 'user.name', 'test'], cwd=root)
            subprocess.run(['git', 'config', 'user.email', 'test@example.com'], cwd=root)
            subprocess.run(['git', 'add', '.'], cwd=root)
            subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=root)
            
            yield root
            
    def test_initialization(self, temp_directory):
        """Test analyzer initialization."""
        analyzer = EnhancedFileAnalyzer(temp_directory)
        assert analyzer.root_path == temp_directory
        assert '.git' in analyzer.ignored_patterns
        assert 'node_modules' in analyzer.ignored_patterns
        
    def test_file_stats(self, temp_directory):
        """Test comprehensive file statistics."""
        analyzer = EnhancedFileAnalyzer(temp_directory)
        stats = analyzer.get_file_stats(temp_directory / "README.md")
        
        assert isinstance(stats, dict)
        assert stats['extension'] == 'md'
        assert not stats['is_dir']
        assert stats['mime_type'].startswith('text/')
        assert stats['line_count'] == 2
        assert stats['word_count'] == 4
        assert not stats['is_symlink']
        assert len(stats['git_history']) > 0
        
    def test_symlink_stats(self, temp_directory):
        """Test symlink statistics."""
        analyzer = EnhancedFileAnalyzer(temp_directory)
        stats = analyzer.get_file_stats(temp_directory / "README.link")
        
        assert stats['is_symlink']
        assert stats['extension'] == 'link'
        
    def test_directory_stats(self, temp_directory):
        """Test directory statistics."""
        analyzer = EnhancedFileAnalyzer(temp_directory)
        stats = analyzer._get_directory_stats(temp_directory / "src")
        
        assert stats['file_count'] == 2
        assert stats['total_size'] > 0
        assert 'py' in stats['extensions']
        assert stats['extensions']['py'] == 2
        
    def test_tree_generation_text(self, temp_directory):
        """Test text tree generation."""
        analyzer = EnhancedFileAnalyzer(temp_directory)
        tree = analyzer.generate_tree(format='text')
        
        assert "📁 docs" in tree
        assert "📝 README.md" in tree
        assert "🐍 main.py" in tree
        assert "🔗 README.link" in tree
        
    def test_tree_generation_markdown(self, temp_directory):
        """Test markdown tree generation."""
        analyzer = EnhancedFileAnalyzer(temp_directory)
        tree = analyzer.generate_tree(format='markdown')
        
        assert "### 📁 docs" in tree
        assert "`README.md`" in tree
        assert "`main.py`" in tree
        
    def test_size_formatting(self, temp_directory):
        """Test file size formatting."""
        analyzer = EnhancedFileAnalyzer(temp_directory)
        
        assert analyzer._format_size(0) == "0B"
        assert analyzer._format_size(1024) == "1.0 KB"
        assert analyzer._format_size(1024 * 1024) == "1.0 MB"
        
    def test_markdown_report(self, temp_directory):
        """Test markdown report generation."""
        analyzer = EnhancedFileAnalyzer(temp_directory)
        report_path = temp_directory / "report.md"
        analyzer.generate_markdown_report(report_path)
        
        assert report_path.exists()
        content = report_path.read_text()
        
        assert "# Repository Analysis Report" in content
        assert "## File Types" in content
        assert "## Directory Structure" in content
        assert "## Recent Changes" in content
        assert "## Largest Files" in content
        
    def test_file_icons(self, temp_directory):
        """Test file icon selection."""
        analyzer = EnhancedFileAnalyzer(temp_directory)
        
        md_stats = analyzer.get_file_stats(temp_directory / "README.md")
        py_stats = analyzer.get_file_stats(temp_directory / "src/main.py")
        png_stats = analyzer.get_file_stats(temp_directory / "docs/images/diagram.png")
        
        assert analyzer._get_file_icon(md_stats) == "📝"
        assert analyzer._get_file_icon(py_stats) == "🐍"
        assert analyzer._get_file_icon(png_stats) == "🖼️"
        
    def test_error_handling(self, temp_directory):
        """Test error handling for inaccessible paths."""
        restricted_dir = temp_directory / "restricted"
        restricted_dir.mkdir()
        restricted_file = restricted_dir / "secret.txt"
        restricted_file.write_text("secret")
        
        try:
            os.chmod(restricted_dir, 0o000)
            
            analyzer = EnhancedFileAnalyzer(temp_directory)
            tree = analyzer.generate_tree()
            
            assert "🚫 restricted" in tree
            assert "secret.txt" not in tree
        finally:
            os.chmod(restricted_dir, 0o755)

if __name__ == "__main__":
    pytest.main([__file__]) 