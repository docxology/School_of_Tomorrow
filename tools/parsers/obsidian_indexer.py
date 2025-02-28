#!/usr/bin/env python3

import os
import datetime
from pathlib import Path
from typing import List, Dict, Set, Tuple, Optional, Any
import yaml
import re
import json
import csv
from dataclasses import dataclass, asdict
from collections import defaultdict

@dataclass
class FileMetadata:
    """Metadata for a single file."""
    path: str
    name: str
    folder: str
    created: str
    modified: str
    links_to: List[str]
    linked_from: List[str]
    tags: List[str]
    frontmatter: Dict[str, Any]

@dataclass
class FolderMetadata:
    """Metadata for a folder."""
    path: str
    name: str
    emoji: str
    description: str
    files: List[str]
    subfolders: List[str]
    total_files: int
    total_links: int
    has_index: bool

class DateTimeEncoder(json.JSONEncoder):
    """Custom JSON encoder for handling datetime objects."""
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        return super().default(obj)

class ObsidianIndexer:
    """Enhanced indexer for Obsidian vaults with emoji support and folder descriptions."""
    
    # Default folder emojis and descriptions
    DEFAULT_FOLDER_METADATA = {
        'projects': ('📁', 'Active projects and tasks'),
        'notes': ('📔', 'General notes and thoughts'),
        'research': ('🔬', 'Research materials and findings'),
        'archive': ('🗄️', 'Archived content'),
        'resources': ('📚', 'External resources and references'),
        'templates': ('📋', 'Note templates'),
        'attachments': ('📎', 'File attachments'),
        'daily': ('📅', 'Daily notes'),
        'meetings': ('👥', 'Meeting notes'),
        'ideas': ('💡', 'Ideas and brainstorms'),
        'documentation': ('📖', 'Documentation and guides'),
        'workflows': ('🔄', 'Process workflows'),
        'guides': ('🎯', 'User guides and tutorials'),
        'concepts': ('🧠', 'Core concepts and theories'),
        'systems': ('⚙️', 'System configurations'),
        'tools': ('🛠️', 'Tools and utilities')
    }
    
    # Directories to ignore
    IGNORED_DIRS = {
        '.git', '__pycache__', '.pytest_cache', '.obsidian', '.benchmarks',
        'node_modules', '.vscode', '.idea', '.hypothesis', 'tools'
    }
    
    # Directories to ignore by pattern
    IGNORED_PATTERNS = [
        r'^\.',  # Hidden directories
        r'^_',   # Underscore prefixed
        r'^\d+$' # Pure numeric names
    ]
    
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.index_files: Dict[str, Set[str]] = {}
        self.file_links: Dict[str, List[str]] = {}
        self.folder_metadata: Dict[str, Tuple[str, str]] = self.DEFAULT_FOLDER_METADATA.copy()
        self.empty_folders: Set[str] = set()
        
        # New tracking attributes
        self.file_metadata: Dict[str, FileMetadata] = {}
        self.folder_stats: Dict[str, FolderMetadata] = {}
        self.backlinks: Dict[str, Set[str]] = defaultdict(set)
        self.tags: Dict[str, Set[str]] = defaultdict(set)
        self.broken_links: Dict[str, List[str]] = defaultdict(list)
        self.same_folder_links_only = False
        
        # Create tools output directory
        self.tools_dir = self.root_dir / 'fuller-obsidian/tools/output'
        self.tools_dir.mkdir(parents=True, exist_ok=True)
        
    def should_ignore_dir(self, dir_name: str) -> bool:
        """Check if directory should be ignored."""
        if dir_name in self.IGNORED_DIRS:
            return True
            
        return any(re.match(pattern, dir_name) for pattern in self.IGNORED_PATTERNS)
        
    def set_folder_metadata(self, folder_name: str, emoji: str, description: str) -> None:
        """Set custom emoji and description for a folder."""
        self.folder_metadata[folder_name] = (emoji, description)
        
    def scan_directory(self, dir_path: Path) -> None:
        """Scan directory and collect file information."""
        try:
            if self.should_ignore_dir(dir_path.name):
                return
                
            has_files = False
            for item in dir_path.iterdir():
                if item.is_file() and item.suffix == '.md':
                    # Skip existing index files
                    if item.name.endswith('_index.md'):
                        continue
                        
                    folder_name = item.parent.name
                    if folder_name not in self.index_files:
                        self.index_files[folder_name] = set()
                    
                    # Add file to index without extension
                    self.index_files[folder_name].add(item.stem)
                    has_files = True
                    
                    # Collect links from file content
                    self._collect_file_links(item)
                    
                elif item.is_dir():
                    self.scan_directory(item)
                    
            # If this is a directory with no markdown files, add it to empty_folders
            if not has_files and dir_path != self.root_dir and not self.should_ignore_dir(dir_path.name):
                self.empty_folders.add(dir_path.name)
                
        except Exception as e:
            print(f"Error scanning directory {dir_path}: {e}")

    def _collect_file_links(self, file_path: Path) -> None:
        """Collect Obsidian-style links from file content and frontmatter."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Extract frontmatter and its links
                frontmatter_data, frontmatter_links = self._extract_frontmatter_links(content)
                
                # Extract inline links
                inline_links = self._extract_links(content)
                
                # Extract tags
                tags = self._extract_tags(content, frontmatter_data)
                
                # Combine all unique links
                all_links = list(set(frontmatter_links + inline_links))
                
                if all_links:
                    self.file_links[file_path.stem] = all_links
                    
                # Update backlinks
                for link in all_links:
                    self.backlinks[link].add(file_path.stem)
                    
                # Store file metadata
                rel_path = file_path.relative_to(self.root_dir)
                self.file_metadata[file_path.stem] = FileMetadata(
                    path=str(rel_path),
                    name=file_path.stem,
                    folder=file_path.parent.name,
                    created=datetime.datetime.fromtimestamp(file_path.stat().st_ctime).strftime("%Y-%m-%d"),
                    modified=datetime.datetime.fromtimestamp(file_path.stat().st_mtime).strftime("%Y-%m-%d"),
                    links_to=all_links,
                    linked_from=list(self.backlinks[file_path.stem]),
                    tags=list(tags),
                    frontmatter=frontmatter_data or {}
                )
                
                # Store tags
                self.tags[file_path.stem].update(tags)
                
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")

    def _extract_tags(self, content: str, frontmatter: Optional[Dict] = None) -> Set[str]:
        """Extract tags from content and frontmatter."""
        tags = set()
        
        # Extract inline tags (#tag)
        inline_tags = re.findall(r'#([\w/-]+)', content)
        tags.update(inline_tags)
        
        # Extract frontmatter tags
        if frontmatter and 'tags' in frontmatter:
            if isinstance(frontmatter['tags'], list):
                tags.update(frontmatter['tags'])
            elif isinstance(frontmatter['tags'], str):
                tags.add(frontmatter['tags'])
                
        return tags

    def _extract_frontmatter_links(self, content: str) -> Tuple[Dict[str, Any], List[str]]:
        """Extract frontmatter and its links."""
        links = []
        frontmatter_data = {}
        
        try:
            if content.startswith('---'):
                end_idx = content.find('---', 3)
                if end_idx != -1:
                    frontmatter = content[3:end_idx]
                    
                    # Replace template variables with placeholders
                    frontmatter = re.sub(r'\{\{.*?\}\}', 'placeholder', frontmatter)
                    
                    # Handle comma-separated lists in YAML
                    frontmatter = re.sub(r'\[(.*?)\]', lambda m: '[' + m.group(1).replace(',', '') + ']', frontmatter)
                    
                    # Clean up related fields that use commas
                    frontmatter = re.sub(r'related:\s*\[\[(.*?)\]\],\s*\[\[(.*?)\]\]', 
                                       lambda m: f'related: ["[[{m.group(1)}]]", "[[{m.group(2)}]]"]', 
                                       frontmatter)
                    
                    try:
                        frontmatter_data = yaml.safe_load(frontmatter) or {}
                    except yaml.YAMLError as e:
                        print(f"YAML parsing error in frontmatter: {e}")
                        print(f"Problematic frontmatter:\n{frontmatter}")
                        frontmatter_data = {}
                    
                    # Extract links from frontmatter
                    for field in ['links', 'related']:
                        if field in frontmatter_data:
                            field_value = frontmatter_data[field]
                            if isinstance(field_value, list):
                                for item in field_value:
                                    if isinstance(item, str):
                                        # Extract link from [[link]] format
                                        match = re.search(r'\[\[(.*?)\]\]', item)
                                        if match:
                                            links.append(match.group(1))
                                        else:
                                            links.append(item)
                            elif isinstance(field_value, str):
                                match = re.search(r'\[\[(.*?)\]\]', field_value)
                                if match:
                                    links.append(match.group(1))
                                else:
                                    links.append(field_value)
                    
        except Exception as e:
            print(f"Error parsing frontmatter: {e}")
            print(f"Content preview: {content[:200]}...")
            
        return frontmatter_data, links

    def _extract_links(self, content: str) -> List[str]:
        """Extract Obsidian-style links from content."""
        import re
        # Match [[link]] and [[link|alias]] patterns
        pattern = r'\[\[(.*?)(?:\|.*?)?\]\]'
        matches = re.findall(pattern, content)
        return matches

    def generate_index_files(self) -> None:
        """Generate index files for each directory."""
        # Generate index files for directories with files
        for folder_name, files in self.index_files.items():
            if not self.should_ignore_dir(folder_name):
                self._write_index_file(folder_name, files)
            
        # Generate index files for empty directories
        for folder_name in self.empty_folders:
            if not self.should_ignore_dir(folder_name):
                self._write_index_file(folder_name, set())

    def _write_index_file(self, folder_name: str, files: Set[str]) -> None:
        """Write index file for a specific directory."""
        folder_path = self.root_dir / folder_name
        if not folder_path.exists():
            try:
                folder_path.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                print(f"Error creating directory {folder_path}: {e}")
                return
                
        index_path = folder_path / f'{folder_name}_index.md'
        try:
            emoji, description = self.folder_metadata.get(folder_name, ('📂', 'Folder contents'))
            
            with open(index_path, 'w', encoding='utf-8') as f:
                # Write header
                f.write(f'---\ntitle: {folder_name.title()} Index\n')
                f.write(f'description: {description}\n')
                f.write(f'created: {datetime.datetime.now().strftime("%Y-%m-%d")}\n')
                f.write(f'updated: {datetime.datetime.now().strftime("%Y-%m-%d")}\n')
                f.write(f'emoji: {emoji}\n---\n\n')
                
                # Write main heading with emoji
                f.write(f'# {emoji} {folder_name.title()} Index\n\n')
                
                # Write folder description
                f.write(f'> {description}\n\n')
                
                if not files:
                    f.write('*No files in this folder yet.*\n\n')
                else:
                    # Write file list with links
                    f.write('## Files\n\n')
                    for file in sorted(files):
                        f.write(f'- [[{file}]]\n')
                        
                        # Add related links if they exist
                        if file in self.file_links:
                            f.write('  - Related:\n')
                            for link in sorted(set(self.file_links[file])):
                                f.write(f'    - [[{link}]]\n')
                
                # Write statistics
                f.write(f'\n## Statistics\n\n')
                f.write(f'- Total files: {len(files)}\n')
                f.write(f'- Files with links: {sum(1 for f in files if f in self.file_links)}\n')
                f.write(f'- Total links: {sum(len(links) for links in self.file_links.values())}\n')
                f.write(f'- Last updated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
                
            print(f"Generated index file: {index_path}")
        except Exception as e:
            print(f"Error writing index file for {folder_name}: {e}")

    def generate_machine_readable_logs(self) -> None:
        """Generate machine-readable logs in various formats."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Generate JSON file structure
        structure = {
            'files': {name: asdict(metadata) for name, metadata in self.file_metadata.items()},
            'folders': {name: asdict(metadata) for name, metadata in self.folder_stats.items()},
            'tags': {tag: list(files) for tag, files in self.tags.items()},
            'backlinks': {target: list(sources) for target, sources in self.backlinks.items()},
            'broken_links': dict(self.broken_links),
            'metadata': {
                'generated': datetime.datetime.now().isoformat(),
                'total_files': len(self.file_metadata),
                'total_folders': len(self.folder_stats),
                'total_tags': len(self.tags),
                'total_links': sum(len(links) for links in self.file_links.values())
            }
        }
        
        # Save as JSON
        json_path = self.tools_dir / f'vault_structure_{timestamp}.json'
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(structure, f, indent=2, cls=DateTimeEncoder)
            
        # Save as YAML
        yaml_path = self.tools_dir / f'vault_structure_{timestamp}.yaml'
        with open(yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(structure, f, allow_unicode=True)
            
        # Generate CSV files for easy processing
        self._generate_csv_logs(timestamp)
        
        # Generate link graph
        self._generate_link_graph(timestamp)
        
        print(f"Generated machine-readable logs in {self.tools_dir}")

    def _generate_csv_logs(self, timestamp: str) -> None:
        """Generate CSV logs for various aspects of the vault."""
        # Files CSV
        files_csv = self.tools_dir / f'files_{timestamp}.csv'
        with open(files_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'path', 'folder', 'created', 'modified', 'num_links', 'num_backlinks', 'num_tags'])
            for name, metadata in self.file_metadata.items():
                writer.writerow([
                    name,
                    metadata.path,
                    metadata.folder,
                    metadata.created,
                    metadata.modified,
                    len(metadata.links_to),
                    len(metadata.linked_from),
                    len(metadata.tags)
                ])
                
        # Links CSV
        links_csv = self.tools_dir / f'links_{timestamp}.csv'
        with open(links_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['source', 'target'])
            for source, targets in self.file_links.items():
                for target in targets:
                    writer.writerow([source, target])
                    
        # Tags CSV
        tags_csv = self.tools_dir / f'tags_{timestamp}.csv'
        with open(tags_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['tag', 'file'])
            for tag, files in self.tags.items():
                for file in files:
                    writer.writerow([tag, file])

    def _generate_link_graph(self, timestamp: str) -> None:
        """Generate a Mermaid graph of file relationships."""
        graph_path = self.tools_dir / f'link_graph_{timestamp}.md'
        with open(graph_path, 'w', encoding='utf-8') as f:
            f.write('```mermaid\ngraph TD\n')
            
            # Add nodes
            for file in self.file_metadata:
                f.write(f'    {file}["{file}"]\n')
                
            # Add relationships
            for source, targets in self.file_links.items():
                for target in targets:
                    f.write(f'    {source} --> {target}\n')
                    
            f.write('```\n')

    def validate_links(self) -> None:
        """Validate all links and record broken ones."""
        all_files = set(self.file_metadata.keys())
        
        for source, links in self.file_links.items():
            for target in links:
                if target not in all_files:
                    self.broken_links[source].append(target)
                    
        # Generate broken links report
        if self.broken_links:
            report_path = self.tools_dir / 'broken_links_report.md'
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write('# Broken Links Report\n\n')
                for source, targets in self.broken_links.items():
                    f.write(f'## In file: [[{source}]]\n')
                    for target in targets:
                        f.write(f'- Missing link to: [[{target}]]\n')
                    f.write('\n')

    def update_folder_stats(self) -> None:
        """Update folder statistics."""
        for folder_name in set(self.index_files.keys()) | self.empty_folders:
            if self.should_ignore_dir(folder_name):
                continue
                
            folder_path = self.root_dir / folder_name
            if not folder_path.exists():
                print(f"Skipping non-existent folder: {folder_path}")
                continue
                
            files = self.index_files.get(folder_name, set())
            
            try:
                subfolders = [d.name for d in folder_path.iterdir() 
                            if d.is_dir() and not self.should_ignore_dir(d.name)]
            except Exception as e:
                print(f"Error listing subfolders for {folder_path}: {e}")
                subfolders = []
            
            self.folder_stats[folder_name] = FolderMetadata(
                path=str(folder_path.relative_to(self.root_dir)),
                name=folder_name,
                emoji=self.folder_metadata.get(folder_name, ('📂', ''))[0],
                description=self.folder_metadata.get(folder_name, ('', 'Folder contents'))[1],
                files=list(files),
                subfolders=subfolders,
                total_files=len(files),
                total_links=sum(len(self.file_links.get(f, [])) for f in files),
                has_index=any(f.endswith('_index.md') for f in os.listdir(folder_path) if os.path.isfile(folder_path / f))
            )

    def process_vault(self) -> None:
        """Process the entire vault and generate all outputs."""
        print(f"Scanning directory: {self.root_dir}")
        self.scan_directory(self.root_dir)
        
        print("Updating folder statistics...")
        self.update_folder_stats()
        
        print("Generating index files...")
        self.generate_index_files()
        
        print("Validating links...")
        self.validate_links()
        
        print("Generating machine-readable logs...")
        self.generate_machine_readable_logs()
        
        print("Generating human-readable log...")
        self.generate_log()
        
        print("Processing complete!")

    def generate_log(self) -> None:
        """Generate a log file with indexing statistics."""
        log_path = self.root_dir / 'indexing_log.txt'
        try:
            with open(log_path, 'w', encoding='utf-8') as f:
                f.write(f'Indexing Log - {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
                f.write('=' * 50 + '\n\n')
                
                total_files = 0
                total_links = 0
                
                # Log directories with files
                for folder_name, files in self.index_files.items():
                    if self.should_ignore_dir(folder_name):
                        continue
                        
                    emoji, desc = self.folder_metadata.get(folder_name, ('📂', 'Folder contents'))
                    f.write(f'\nFolder: {emoji} {folder_name}\n')
                    f.write('-' * 20 + '\n')
                    f.write(f'Description: {desc}\n')
                    f.write(f'Files indexed: {len(files)}\n')
                    
                    folder_links = sum(len(self.file_links.get(file, [])) for file in files)
                    total_files += len(files)
                    total_links += folder_links
                    
                    f.write(f'Total links: {folder_links}\n')
                    f.write('Files:\n')
                    for file in sorted(files):
                        f.write(f'- {file}\n')
                        if file in self.file_links:
                            f.write(f'  Links: {len(self.file_links[file])}\n')
                            
                # Log empty directories
                if self.empty_folders:
                    f.write('\nEmpty Folders:\n')
                    f.write('-' * 20 + '\n')
                    for folder_name in sorted(self.empty_folders):
                        if not self.should_ignore_dir(folder_name):
                            emoji, desc = self.folder_metadata.get(folder_name, ('📂', 'Folder contents'))
                            f.write(f'- {emoji} {folder_name}: {desc}\n')
                            
                f.write('\nSummary\n')
                f.write('=' * 20 + '\n')
                f.write(f'Total folders: {sum(1 for f in self.index_files if not self.should_ignore_dir(f)) + len([f for f in self.empty_folders if not self.should_ignore_dir(f)])}\n')
                f.write(f'Total files: {total_files}\n')
                f.write(f'Total links: {total_links}\n')
                f.write(f'Empty folders: {len([f for f in self.empty_folders if not self.should_ignore_dir(f)])}\n')
                
            print(f"Generated log file: {log_path}")
        except Exception as e:
            print(f"Error writing log file: {e}")

    def generate_clean_index_files(self) -> None:
        """Generate clean index files for each folder."""
        # Get all folders that should have an index
        folders_to_index = set(self.index_files.keys()) | set(self.folder_metadata.keys())
        
        for folder_name in folders_to_index:
            folder_path = self.root_dir / folder_name
            if not folder_path.exists():
                print(f"Skipping non-existent folder: {folder_path}")
                continue

            files = self.index_files.get(folder_name, set())
            emoji, description = self.folder_metadata.get(folder_name, ('📁', 'Files and documents'))
            
            # Track valid files and their locations
            valid_files = []
            for file in sorted(files):
                file_path = folder_path / f"{file}.md"
                if file_path.exists():
                    valid_files.append((file, str(file_path)))
                else:
                    print(f"Warning: File not found at {file_path}")
            
            # Create index file content
            content = [
                f"---",
                f"title: {folder_name.title()} Index",
                f"description: {description}",
                f"created: {datetime.datetime.now().strftime('%Y-%m-%d')}",
                f"updated: {datetime.datetime.now().strftime('%Y-%m-%d')}",
                f"emoji: {emoji}",
                f"total_files: {len(valid_files)}",
                f"---",
                f"",
                f"# {emoji} {folder_name.title()} Index",
                f"",
                f"> {description}",
                f"",
                f"## Contents"
            ]
            
            # Add existing files in alphabetical order
            if valid_files:
                content.append("")
                for file, file_path in valid_files:
                    content.append(f"- [[{file}]]")
                    # Log file location for debugging
                    print(f"Added link to {file} from {file_path}")
            
            # Write index file
            index_path = folder_path / f"{folder_name}_index.md"
            try:
                with open(index_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(content))
                print(f"Generated index file: {index_path} with {len(valid_files)} valid links")
            except Exception as e:
                print(f"Error writing index file {index_path}: {e}")
            
            # Update folder statistics
            self.folder_stats[folder_name] = FolderMetadata(
                path=str(folder_path.relative_to(self.root_dir)),
                name=folder_name,
                emoji=emoji,
                description=description,
                files=[f[0] for f in valid_files],
                subfolders=[d.name for d in folder_path.iterdir() if d.is_dir() and not self.should_ignore_dir(d.name)],
                total_files=len(valid_files),
                total_links=sum(len(self.file_links.get(f[0], [])) for f in valid_files),
                has_index=True
            )

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Generate Obsidian index files and analysis')
    parser.add_argument('root_dir', help='Root directory to scan')
    parser.add_argument('--emoji', help='Custom emoji for folder (format: folder:emoji)')
    parser.add_argument('--desc', help='Custom description for folder (format: folder:description)')
    args = parser.parse_args()
    
    indexer = ObsidianIndexer(args.root_dir)
    
    # Handle custom emoji and descriptions
    if args.emoji:
        for folder_emoji in args.emoji.split(','):
            folder, emoji = folder_emoji.split(':')
            if folder in indexer.folder_metadata:
                desc = indexer.folder_metadata[folder][1]
                indexer.set_folder_metadata(folder, emoji, desc)
                
    if args.desc:
        for folder_desc in args.desc.split(','):
            folder, desc = folder_desc.split(':')
            if folder in indexer.folder_metadata:
                emoji = indexer.folder_metadata[folder][0]
                indexer.set_folder_metadata(folder, emoji, desc)
    
    indexer.process_vault()

if __name__ == '__main__':
    main() 