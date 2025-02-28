#!/usr/bin/env python3

import os
from pathlib import Path
import mimetypes
import json
from datetime import datetime
import logging
from typing import Dict, List, Union, Optional
import yaml
import re

class EnhancedFileAnalyzer:
    """Enhanced file system analysis tool with visualization capabilities."""
    
    def __init__(self, root_dir: Union[str, Path]):
        """Initialize analyzer with root directory."""
        self.root_dir = Path(root_dir)
        self.ignored_patterns = ['.git', '__pycache__', 'node_modules', '.pytest_cache', 'venv']
        self.logger = logging.getLogger(__name__)
    
    def _safe_parse_frontmatter(self, content: str) -> Dict:
        """Safely parse YAML frontmatter from content."""
        try:
            # Find the frontmatter section between --- markers
            frontmatter_pattern = r'(?s)^---\s*\n(.*?)\n---\s*\n'
            match = re.search(frontmatter_pattern, content)
            
            if not match:
                return {}
                
            # Pre-process the frontmatter text
            frontmatter_text = match.group(1)
            
            # Convert to flow style YAML
            processed_lines = []
            current_dict = {}
            
            for line in frontmatter_text.split('\n'):
                line = line.strip()
                if not line:
                    continue
                    
                if ':' in line:
                    # Split only on the first colon
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Store in dictionary with proper escaping
                    if value:
                        # Escape special characters in value
                        value = value.replace('\\', '\\\\').replace('"', '\\"')
                        current_dict[key] = value
                    else:
                        current_dict[key] = ''
            
            # Convert dictionary to flow style YAML
            flow_style = '{'
            for key, value in current_dict.items():
                if value:
                    flow_style += f'"{key}": "{value}", '
                else:
                    flow_style += f'"{key}": "", '
            flow_style = flow_style.rstrip(', ') + '}'
            
            try:
                parsed = yaml.safe_load(flow_style)
                if parsed is None:
                    return {}
                
                # Clean up any trailing whitespace in the title
                if parsed and 'title' in parsed:
                    parsed['title'] = parsed['title'].strip()
                
                return parsed
            except yaml.YAMLError as e:
                self.logger.warning(f"YAML parsing error in frontmatter: {str(e)}\nProblematic frontmatter:\n\n{match.group(1)}\n")
                return {}
        except Exception as e:
            self.logger.warning(f"Error in frontmatter extraction: {str(e)}")
            return {}
    
    def _format_size(self, size_bytes: int) -> str:
        """Format size in bytes to human readable format."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.1f}{unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f}TB"
    
    def _get_file_icon(self, file_info: Dict) -> str:
        """Get appropriate icon for file type."""
        if file_info['is_dir']:
            return '📁'
        if file_info['is_symlink']:
            return '🔗'
            
        mime_type = file_info['mime_type']
        if 'text' in mime_type:
            return '📄'
        elif 'image' in mime_type:
            return '🖼️'
        elif 'audio' in mime_type:
            return '🎵'
        elif 'video' in mime_type:
            return '🎬'
        elif 'application' in mime_type:
            if 'pdf' in mime_type:
                return '📕'
            elif any(x in mime_type for x in ['zip', 'tar', 'gzip', 'compressed']):
                return '📦'
            elif 'json' in mime_type:
                return '📋'
            elif 'xml' in mime_type:
                return '📰'
        return '📎'
    
    def get_file_stats(self, file_path: Path) -> Dict:
        """Get detailed statistics for a file."""
        stats = file_path.stat()
        file_info = {
            'path': str(file_path),
            'size': stats.st_size,
            'created': datetime.fromtimestamp(stats.st_ctime),
            'modified': datetime.fromtimestamp(stats.st_mtime),
            'is_dir': file_path.is_dir(),
            'is_symlink': file_path.is_symlink(),
            'mime_type': mimetypes.guess_type(str(file_path))[0] or 'application/octet-stream'
        }
        
        # Handle markdown files with frontmatter
        if file_path.suffix.lower() == '.md':
            try:
                content = file_path.read_text(encoding='utf-8')
                frontmatter = self._safe_parse_frontmatter(content)
                if frontmatter:
                    file_info['metadata'] = frontmatter
            except Exception as e:
                self.logger.warning(f"Error reading markdown file {file_path}: {str(e)}")
                
        return file_info
    
    def _get_directory_stats(self, dir_path: Path) -> Dict:
        """Get statistics for a directory."""
        stats = {
            'file_count': 0,
            'dir_count': 0,
            'total_size': 0,
            'extensions': {},
            'newest_file': None
        }
        
        try:
            for item in dir_path.rglob('*'):
                if any(ignored in str(item) for ignored in self.ignored_patterns):
                    continue
                    
                if item.is_file():
                    file_stat = self.get_file_stats(item)
                    stats['file_count'] += 1
                    stats['total_size'] += file_stat['size']
                    
                    ext = item.suffix
                    if ext:
                        stats['extensions'][ext] = stats['extensions'].get(ext, 0) + 1
                        
                    if not stats['newest_file'] or file_stat['modified'] > stats['newest_file']['modified']:
                        stats['newest_file'] = {
                            'path': str(item),
                            'modified': file_stat['modified']
                        }
                elif item.is_dir():
                    stats['dir_count'] += 1
                    
        except Exception as e:
            self.logger.error(f"Error analyzing directory {dir_path}: {str(e)}")
            
        return stats
    
    def generate_tree(self, format: str = 'text', max_depth: Optional[int] = None) -> str:
        """Generate a tree visualization of the directory structure."""
        def _generate_tree_text(path: Path, prefix: str = '', depth: int = 0) -> List[str]:
            if max_depth is not None and depth > max_depth:
                return []
                
            if any(ignored in str(path) for ignored in self.ignored_patterns):
                return []
                
            lines = []
            entries = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))
            
            for i, entry in enumerate(entries):
                is_last = i == len(entries) - 1
                connector = '└── ' if is_last else '├── '
                
                stats = self.get_file_stats(entry)
                icon = self._get_file_icon(stats)
                
                lines.append(f"{prefix}{connector}{icon} {entry.name}")
                
                if entry.is_dir():
                    ext_prefix = prefix + ('    ' if is_last else '│   ')
                    lines.extend(_generate_tree_text(entry, ext_prefix, depth + 1))
                    
            return lines
        
        def _generate_tree_markdown(path: Path, depth: int = 0) -> List[str]:
            if max_depth is not None and depth > max_depth:
                return []
                
            if any(ignored in str(path) for ignored in self.ignored_patterns):
                return []
                
            lines = []
            entries = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))
            
            for entry in entries:
                stats = self.get_file_stats(entry)
                icon = self._get_file_icon(stats)
                indent = '  ' * depth
                
                if entry.is_dir():
                    lines.append(f"{indent}- {icon} **{entry.name}/**")
                    lines.extend(_generate_tree_markdown(entry, depth + 1))
                else:
                    size = self._format_size(stats['size'])
                    lines.append(f"{indent}- {icon} `{entry.name}` ({size})")
                    
            return lines
        
        if format == 'markdown':
            lines = _generate_tree_markdown(self.root_dir)
            return '\n'.join(['# Directory Structure', ''] + lines)
        else:
            lines = _generate_tree_text(self.root_dir)
            return '\n'.join([str(self.root_dir)] + lines)
    
    def generate_markdown_report(self, output_path: Path) -> None:
        """Generate a comprehensive Markdown report."""
        stats = self._get_directory_stats(self.root_dir)
        
        with open(output_path, 'w') as f:
            f.write("# Repository Analysis Report\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## Overview\n\n")
            f.write(f"- Total files: {stats['file_count']}\n")
            f.write(f"- Total directories: {stats['dir_count']}\n")
            f.write(f"- Repository size: {self._format_size(stats['total_size'])}\n\n")
            
            f.write("## File Types\n\n")
            if stats['extensions']:
                f.write("| Extension | Count |\n")
                f.write("|-----------|-------|\n")
                for ext, count in sorted(stats['extensions'].items(), key=lambda x: x[1], reverse=True):
                    f.write(f"| {ext} | {count} |\n")
            
            if stats['newest_file']:
                f.write("\n## Recent Changes\n\n")
                f.write(f"Most recent file: `{stats['newest_file']['path']}`\n")
                f.write(f"Modified: {stats['newest_file']['modified'].strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            f.write("\n## Directory Structure\n\n")
            f.write("```\n")
            f.write(self.generate_tree(max_depth=3))
            f.write("\n```\n") 