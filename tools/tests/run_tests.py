#!/usr/bin/env python3

import sys
import os
from pathlib import Path
import unittest
import yaml
from datetime import datetime
import logging

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

# Import test modules
from test_parsers.test_index_generation import TestObsidianIndexer, run_tests
from test_file_system_analysis import TestFileSystemAnalysis, run_file_system_tests
from parsers.obsidian_indexer import ObsidianIndexer

def setup_logging():
    """Configure logging for test execution."""
    log_dir = Path(__file__).parent / 'logs'
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / f'test_run_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

def get_folder_metadata():
    """Define folder-specific metadata with emojis and descriptions."""
    return {
        'books': ('📚', 'Books and publications by and about Fuller'),
        'mathematics': ('🔢', 'Mathematical concepts and applications in Fuller\'s work'),
        'formalisms': ('📏', 'Formal systems and mathematical notations in Fuller\'s work'),
        'people': ('👥', 'Profiles and biographies of individuals'),
        'places': ('📍', 'Geographic locations and spaces'),
        'concepts': ('🧠', 'Core ideas and theoretical frameworks'),
        'guides': ('🎯', 'Instructions and guidelines'),
        'meta': ('🔄', 'Meta-documentation and structure'),
        'systems': ('⚙️', 'Systems and organizational structures'),
        'documentation': ('📖', 'Project documentation and notes'),
        'prompts': ('💭', 'AI and system prompts'),
        'workflows': ('🔄', 'Process and task workflows'),
        'schemas': ('📐', 'Data structures and schemas'),
        'streams': ('🌊', 'Data and information flows'),
        'repos': ('📁', 'Code repositories and projects'),
        'examples': ('💡', 'Examples and demonstrations'),
        'templates': ('📋', 'Template files and structures')
    }

def generate_indices(root_dir: Path, logger: logging.Logger) -> bool:
    """Generate index files for all folders."""
    try:
        # Initialize indexer
        indexer = ObsidianIndexer(str(root_dir))
        
        # Set metadata for all folders
        folder_metadata = get_folder_metadata()
        for folder, (emoji, desc) in folder_metadata.items():
            indexer.set_folder_metadata(folder, emoji, desc)
        
        # Configure indexer
        indexer.same_folder_links_only = True
        
        # Scan and generate
        logger.info("Scanning vault directory...")
        indexer.scan_directory(root_dir)
        
        logger.info("Generating index files...")
        indexer.generate_clean_index_files()
        
        # Validate results
        logger.info("Validating generated files...")
        for folder in folder_metadata.keys():
            index_path = root_dir / folder / f"{folder}_index.md"
            if index_path.exists():
                logger.info(f"Successfully generated index for {folder}")
            else:
                logger.warning(f"Failed to generate index for {folder}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error generating indices: {str(e)}")
        return False

def main():
    """Main test runner function."""
    # Setup logging
    logger = setup_logging()
    logger.info("Starting test suite execution")
    
    # Run unit tests
    logger.info("Running unit tests...")
    test_success = run_tests()
    
    if not test_success:
        logger.error("Unit tests failed")
        return 1
    
    # Run file system tests
    logger.info("Running file system analysis tests...")
    fs_test_success = run_file_system_tests()
    
    if not fs_test_success:
        logger.error("File system tests failed")
        return 1
    
    # Generate indices
    logger.info("Starting index generation...")
    root_dir = Path(__file__).parent.parent.parent
    
    if not generate_indices(root_dir, logger):
        logger.error("Index generation failed")
        return 1
    
    logger.info("Test suite completed successfully")
    return 0

if __name__ == '__main__':
    sys.exit(main()) 