#!/usr/bin/env python3

import yaml
from pathlib import Path
from typing import Dict, Any, Optional

class FrontmatterParser:
    """Parser for YAML frontmatter in Obsidian markdown files."""
    
    def __init__(self):
        self.frontmatter_delimiter = "---"
        
    def parse(self, file_path: Path) -> Dict[str, Any]:
        """
        Parse YAML frontmatter from an Obsidian markdown file.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            Dict containing the parsed frontmatter, or empty dict if no frontmatter
            
        Raises:
            ValueError: If frontmatter is malformed
            FileNotFoundError: If file doesn't exist
        """
        content = file_path.read_text()
        return self.parse_string(content)
        
    def parse_string(self, content: str) -> Dict[str, Any]:
        """
        Parse YAML frontmatter from a string.
        
        Args:
            content: String containing markdown content with optional frontmatter
            
        Returns:
            Dict containing the parsed frontmatter, or empty dict if no frontmatter
            
        Raises:
            ValueError: If frontmatter is malformed
        """
        # Check if content starts with frontmatter delimiter
        if not content.startswith(self.frontmatter_delimiter):
            return {}
            
        # Find the end of frontmatter
        lines = content.split('\n')
        if len(lines) < 2:
            return {}
            
        end_delimiter_index = -1
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == self.frontmatter_delimiter:
                end_delimiter_index = i
                break
                
        if end_delimiter_index == -1:
            raise ValueError("Unclosed frontmatter block")
            
        # Extract and parse frontmatter
        frontmatter_lines = lines[1:end_delimiter_index]
        frontmatter_text = '\n'.join(frontmatter_lines)
        
        try:
            return yaml.safe_load(frontmatter_text) or {}
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in frontmatter: {str(e)}")
            
    def extract_tags(self, frontmatter: Dict[str, Any]) -> set:
        """
        Extract tags from frontmatter, handling various tag formats.
        
        Args:
            frontmatter: Parsed frontmatter dictionary
            
        Returns:
            Set of unique tags
        """
        tags = set()
        
        # Handle direct tags field
        if 'tags' in frontmatter:
            tag_data = frontmatter['tags']
            if isinstance(tag_data, list):
                tags.update(tag_data)
            elif isinstance(tag_data, str):
                tags.add(tag_data)
                
        # Handle nested tags
        if 'metadata' in frontmatter and isinstance(frontmatter['metadata'], dict):
            if 'tags' in frontmatter['metadata']:
                meta_tags = frontmatter['metadata']['tags']
                if isinstance(meta_tags, list):
                    tags.update(meta_tags)
                elif isinstance(meta_tags, str):
                    tags.add(meta_tags)
                    
        return tags 