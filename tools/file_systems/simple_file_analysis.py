#!/usr/bin/env python3
"""
Simple File System Analysis
--------------------------
Basic file system analysis using only the Python standard library.
"""

import os
import json
from pathlib import Path
from datetime import datetime
import sys

class SimpleFileAnalyzer:
    def __init__(self, root_path: str):
        self.root_path = Path(root_path)
        self.ignored_patterns = ['.git', '__pycache__', '.pytest_cache']
        
    def get_file_stats(self, path: Path) -> dict:
        """Get basic statistics for a file."""
        stats = path.stat()
        return {
            'size': stats.st_size,
            'created': datetime.fromtimestamp(stats.st_ctime).isoformat(),
            'modified': datetime.fromtimestamp(stats.st_mtime).isoformat(),
            'is_dir': path.is_dir(),
            'extension': path.suffix[1:] if path.suffix else None
        }
        
    def generate_tree(self, max_depth: int = None) -> str:
        """Generate a text tree representation."""
        def _build_tree(path: Path, prefix: str = '', depth: int = 0) -> str:
            if max_depth is not None and depth > max_depth:
                return prefix + "...\n"
                
            if any(ignored in str(path) for ignored in self.ignored_patterns):
                return ""
                
            result = []
            try:
                if path.is_file():
                    stats = self.get_file_stats(path)
                    size_str = f" ({stats['size']} bytes)"
                    result.append(f"{prefix}📄 {path.name}{size_str}\n")
                else:
                    result.append(f"{prefix}📁 {path.name}\n")
                    for item in sorted(path.iterdir()):
                        result.append(_build_tree(item, prefix + "  ", depth + 1))
            except PermissionError:
                result.append(f"{prefix}🚫 {path.name} (Permission denied)\n")
                
            return "".join(result)
            
        return _build_tree(self.root_path)
        
    def generate_obsidian_links(self) -> str:
        """Generate Obsidian-compatible wiki links."""
        def _build_links(path: Path) -> str:
            if any(ignored in str(path) for ignored in self.ignored_patterns):
                return ""
                
            result = []
            try:
                if path.is_file():
                    rel_path = path.relative_to(self.root_path)
                    result.append(f"[[{rel_path}]]\n")
                else:
                    for item in sorted(path.iterdir()):
                        result.append(_build_links(item))
            except PermissionError:
                pass
                
            return "".join(result)
            
        return _build_links(self.root_path)
        
    def analyze_extensions(self) -> dict:
        """Analyze file extensions in the repository."""
        extensions = {}
        
        for path in self.root_path.rglob('*'):
            if path.is_file() and not any(ignored in str(path) for ignored in self.ignored_patterns):
                ext = path.suffix[1:] if path.suffix else 'no_extension'
                if ext not in extensions:
                    extensions[ext] = {'count': 0, 'total_size': 0, 'files': []}
                    
                stats = self.get_file_stats(path)
                extensions[ext]['count'] += 1
                extensions[ext]['total_size'] += stats['size']
                extensions[ext]['files'].append(str(path.relative_to(self.root_path)))
                
        return extensions
        
    def export_analysis(self, output_dir: str = 'file_system_analysis'):
        """Export all analysis results to files."""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # Generate tree structure
        with open(output_path / 'tree_structure.txt', 'w') as f:
            f.write(self.generate_tree())
            
        # Generate Obsidian links
        with open(output_path / 'obsidian_links.md', 'w') as f:
            f.write(self.generate_obsidian_links())
            
        # Generate extension analysis
        extensions = self.analyze_extensions()
        with open(output_path / 'extension_analysis.json', 'w') as f:
            json.dump(extensions, f, indent=2)
            
        # Generate summary report
        with open(output_path / 'summary_report.md', 'w') as f:
            f.write("# Repository Structure Analysis\n\n")
            f.write(f"Analysis generated on: {datetime.now().isoformat()}\n\n")
            
            f.write("## File Extensions\n")
            for ext, stats in extensions.items():
                f.write(f"\n### {ext}\n")
                f.write(f"- Count: {stats['count']}\n")
                f.write(f"- Total size: {stats['total_size']} bytes\n")
                f.write("- Files:\n")
                for file in stats['files']:
                    f.write(f"  - {file}\n")

def main():
    if len(sys.argv) > 1:
        root_path = sys.argv[1]
    else:
        root_path = '.'
        
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    else:
        output_dir = 'file_system_analysis'
        
    print(f"Analyzing repository at: {root_path}")
    print(f"Output will be saved to: {output_dir}")
    
    analyzer = SimpleFileAnalyzer(root_path)
    analyzer.export_analysis(output_dir)
    
    print("\nAnalysis complete! The following files have been generated:")
    print("  - tree_structure.txt: ASCII tree representation")
    print("  - obsidian_links.md: Obsidian-compatible wiki links")
    print("  - extension_analysis.json: Detailed file extension analysis")
    print("  - summary_report.md: Overview and statistics")

if __name__ == "__main__":
    main() 