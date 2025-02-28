#!/usr/bin/env python3

import os
import sys
from pathlib import Path

# Add parent directory to path to import parsers
sys.path.append(str(Path(__file__).parent.parent))

from parsers.obsidian_indexer import ObsidianIndexer

def get_folder_metadata():
    """Define folder-specific metadata with emojis and descriptions."""
    return {
        'people': ('👥', 'Profiles and biographies of individuals'),
        'places': ('📍', 'Geographic locations and spaces'),
        'concepts': ('🧠', 'Core ideas and theoretical frameworks'),
        'books': ('📚', 'Books and publications'),
        'guides': ('🎯', 'Instructions and guidelines'),
        'meta': ('🔄', 'Meta-documentation and structure'),
        'mathematics': ('🔢', 'Mathematical concepts and applications'),
        'numbers': ('🔢', 'Numerical concepts and sequences'),
        'systems': ('⚙️', 'Systems and organizational structures'),
        'documentation': ('📖', 'Project documentation and notes'),
        'prompts': ('💭', 'AI and system prompts'),
        'workflows': ('🔄', 'Process and task workflows'),
        'schemas': ('📐', 'Data structures and schemas'),
        'streams': ('🌊', 'Data and information flows'),
        'repos': ('📁', 'Code repositories and projects'),
        'formalisms': ('📏', 'Formal systems and notations'),
        'examples': ('💡', 'Examples and demonstrations'),
        'templates': ('📋', 'Template files and structures')
    }

def main():
    # Get the root directory (fuller-obsidian)
    root_dir = Path(__file__).parent.parent.parent
    
    # Initialize indexer
    indexer = ObsidianIndexer(str(root_dir))
    
    # Set metadata for all folders
    folder_metadata = get_folder_metadata()
    for folder, (emoji, desc) in folder_metadata.items():
        indexer.set_folder_metadata(folder, emoji, desc)
    
    # Configure indexer to only include same-folder links
    indexer.same_folder_links_only = True
    
    # Scan the vault
    indexer.scan_directory(root_dir)
    
    # Generate clean index files
    indexer.generate_clean_index_files()
    
    print("Index files have been updated successfully!")

if __name__ == "__main__":
    main() 