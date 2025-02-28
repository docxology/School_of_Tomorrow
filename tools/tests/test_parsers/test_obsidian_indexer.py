import unittest
from pathlib import Path
import sys
import os
import shutil
from datetime import datetime

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from parsers.obsidian_indexer import ObsidianIndexer

class TestObsidianIndexer(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.test_vault_dir = Path(__file__).parent / 'test_vault'
        self.test_vault_dir.mkdir(exist_ok=True)
        
        # Create test folder structure
        self.folders = {
            'projects': ['📁', 'Active projects and tasks'],
            'notes': ['📔', 'General notes and thoughts'],
            'research': ['🔬', 'Research materials and findings'],
            'archive': ['🗄️', 'Archived content']
        }
        
        for folder_name in self.folders:
            folder_path = self.test_vault_dir / folder_name
            folder_path.mkdir(exist_ok=True)
            
        self.indexer = ObsidianIndexer(str(self.test_vault_dir))
        
    def create_test_note(self, folder: str, name: str, content: str, links: list = None):
        """Helper to create test notes with frontmatter and content."""
        note_path = self.test_vault_dir / folder / f"{name}.md"
        
        frontmatter = "---\n"
        frontmatter += f"title: {name}\n"
        frontmatter += f"created: {datetime.now().strftime('%Y-%m-%d')}\n"
        if links:
            frontmatter += "links:\n"
            for link in links:
                frontmatter += f"  - {link}\n"
        frontmatter += "---\n\n"
        
        with open(note_path, 'w') as f:
            f.write(frontmatter + content)
            
        return note_path
        
    def test_basic_indexing(self):
        """Test basic indexing of files in folders."""
        # Create some test notes
        self.create_test_note('projects', 'Project1', "# Project 1\nContent here")
        self.create_test_note('projects', 'Project2', "# Project 2\nMore content")
        
        self.indexer.scan_directory(self.test_vault_dir)
        self.indexer.generate_index_files()
        
        # Check if index file was created
        index_path = self.test_vault_dir / 'projects' / 'projects_index.md'
        self.assertTrue(index_path.exists())
        
        # Verify content
        content = index_path.read_text()
        self.assertIn('# 📁 Projects Index', content)
        self.assertIn('[[Project1]]', content)
        self.assertIn('[[Project2]]', content)
        
    def test_linked_notes(self):
        """Test handling of linked notes."""
        # Create notes with links
        self.create_test_note('research', 'Study1', 
                            "# Study 1\nLinks to [[Study2]]",
                            links=['Study2'])
        self.create_test_note('research', 'Study2',
                            "# Study 2\nLinks to [[Study1]]",
                            links=['Study1'])
        
        self.indexer.scan_directory(self.test_vault_dir)
        self.indexer.generate_index_files()
        
        # Check if links are properly indexed
        index_path = self.test_vault_dir / 'research' / 'research_index.md'
        content = index_path.read_text()
        
        self.assertIn('[[Study1]]', content)
        self.assertIn('[[Study2]]', content)
        self.assertIn('Related:', content)
        
    def test_emoji_folder_names(self):
        """Test handling of emoji in folder names and index files."""
        for folder_name, (emoji, desc) in self.folders.items():
            self.create_test_note(folder_name, 'TestNote',
                                f"# Test Note in {folder_name}")
            
        self.indexer.scan_directory(self.test_vault_dir)
        self.indexer.generate_index_files()
        
        for folder_name, (emoji, desc) in self.folders.items():
            index_path = self.test_vault_dir / folder_name / f'{folder_name}_index.md'
            content = index_path.read_text()
            self.assertIn(f'# {emoji} {folder_name.title()} Index', content)
            self.assertIn(desc, content)
            
    def test_index_updates(self):
        """Test that index files are properly updated when content changes."""
        # Create initial note
        self.create_test_note('notes', 'Note1', "# Note 1\nInitial content")
        
        self.indexer.scan_directory(self.test_vault_dir)
        self.indexer.generate_index_files()
        
        # Add another note
        self.create_test_note('notes', 'Note2', "# Note 2\nNew content")
        
        self.indexer.scan_directory(self.test_vault_dir)
        self.indexer.generate_index_files()
        
        # Verify both notes are in index
        index_path = self.test_vault_dir / 'notes' / 'notes_index.md'
        content = index_path.read_text()
        self.assertIn('[[Note1]]', content)
        self.assertIn('[[Note2]]', content)
        
    def test_empty_folder(self):
        """Test handling of empty folders."""
        empty_folder = self.test_vault_dir / 'empty'
        empty_folder.mkdir(exist_ok=True)
        
        self.indexer.scan_directory(self.test_vault_dir)
        self.indexer.generate_index_files()
        
        # Check if index file was created with appropriate message
        index_path = empty_folder / 'empty_index.md'
        self.assertTrue(index_path.exists())
        content = index_path.read_text()
        self.assertIn('No files', content)
        
    def tearDown(self):
        """Clean up test files."""
        shutil.rmtree(self.test_vault_dir)
        
if __name__ == '__main__':
    unittest.main() 