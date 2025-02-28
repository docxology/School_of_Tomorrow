#!/usr/bin/env python3
"""
Demonstration script for Enhanced File System Analysis
--------------------------------------------------
Runs all visualization and logging features and saves outputs.
"""

import os
from pathlib import Path
from datetime import datetime
from enhanced_file_analysis import EnhancedFileAnalyzer

def main():
    # Setup output directory
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Initialize analyzer with repository root
    repo_root = Path("../..")
    analyzer = EnhancedFileAnalyzer(repo_root)
    
    # 1. Generate main analysis report
    print("Generating main analysis report...")
    report_path = output_dir / f"analysis_report_{timestamp}.md"
    analyzer.generate_markdown_report(report_path)
    print(f"Report saved to: {report_path}")
    
    # 2. Generate tree visualizations in different formats
    print("\nGenerating tree visualizations...")
    
    # Text tree with different depths
    for depth in [2, 3, 5]:
        tree_path = output_dir / f"tree_depth_{depth}_{timestamp}.txt"
        tree = analyzer.generate_tree(format='text', max_depth=depth)
        tree_path.write_text(tree)
        print(f"Text tree (depth {depth}) saved to: {tree_path}")
    
    # Markdown tree
    md_tree_path = output_dir / f"tree_{timestamp}.md"
    md_tree = analyzer.generate_tree(format='markdown')
    md_tree_path.write_text(md_tree)
    print(f"Markdown tree saved to: {md_tree_path}")
    
    # 3. Generate detailed statistics for important directories
    print("\nGenerating directory statistics...")
    important_dirs = ['src', 'docs', 'tools', 'tests']
    stats_path = output_dir / f"directory_stats_{timestamp}.md"
    
    with open(stats_path, 'w') as f:
        f.write("# Directory Statistics Report\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for dirname in important_dirs:
            dir_path = repo_root / dirname
            if dir_path.exists():
                f.write(f"## {dirname}\n\n")
                stats = analyzer._get_directory_stats(dir_path)
                
                f.write(f"- Files: {stats['file_count']}\n")
                f.write(f"- Directories: {stats['dir_count']}\n")
                f.write(f"- Total size: {analyzer._format_size(stats['total_size'])}\n\n")
                
                if stats['extensions']:
                    f.write("### File Types\n")
                    for ext, count in sorted(stats['extensions'].items(), key=lambda x: x[1], reverse=True):
                        f.write(f"- .{ext}: {count}\n")
                f.write("\n")
                
                if stats.get('newest_file'):
                    f.write("### Latest Changes\n")
                    f.write(f"Newest file: {stats['newest_file']['path']}\n")
                    f.write(f"Modified: {stats['newest_file']['modified']}\n\n")
    
    print(f"Directory statistics saved to: {stats_path}")
    
    # 4. Generate file type summary
    print("\nGenerating file type summary...")
    summary_path = output_dir / f"file_type_summary_{timestamp}.md"
    
    all_files = list(repo_root.rglob('*'))
    type_stats = {}
    
    for file_path in all_files:
        if file_path.is_file() and not any(ignored in str(file_path) for ignored in analyzer.ignored_patterns):
            stats = analyzer.get_file_stats(file_path)
            mime_type = stats['mime_type']
            if mime_type not in type_stats:
                type_stats[mime_type] = {
                    'count': 0,
                    'total_size': 0,
                    'examples': []
                }
            type_stats[mime_type]['count'] += 1
            type_stats[mime_type]['total_size'] += stats['size']
            if len(type_stats[mime_type]['examples']) < 3:
                type_stats[mime_type]['examples'].append(str(file_path.relative_to(repo_root)))
    
    with open(summary_path, 'w') as f:
        f.write("# File Type Summary\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for mime_type, stats in sorted(type_stats.items(), key=lambda x: x[1]['count'], reverse=True):
            icon = analyzer._get_file_icon({'mime_type': mime_type, 'is_dir': False, 'is_symlink': False})
            f.write(f"## {icon} {mime_type}\n\n")
            f.write(f"- Count: {stats['count']}\n")
            f.write(f"- Total size: {analyzer._format_size(stats['total_size'])}\n")
            f.write("- Example files:\n")
            for example in stats['examples']:
                f.write(f"  - `{example}`\n")
            f.write("\n")
    
    print(f"File type summary saved to: {summary_path}")
    
    print("\nAnalysis complete! All outputs have been saved to the 'outputs' directory.")

if __name__ == "__main__":
    main() 