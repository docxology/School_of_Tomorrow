#!/usr/bin/env python3
"""
Repository Analysis Generator
---------------------------
Generate comprehensive analysis of the repository structure.
"""

from pathlib import Path
from file_system_tools import FileSystemAnalyzer
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate repository structure analysis')
    parser.add_argument('--output-dir', '-o', 
                       default='file_system_analysis',
                       help='Output directory for analysis files')
    parser.add_argument('--root-path', '-r',
                       default='.',
                       help='Root path of the repository to analyze')
    args = parser.parse_args()
    
    print(f"Analyzing repository at: {args.root_path}")
    print(f"Output will be saved to: {args.output_dir}")
    
    analyzer = FileSystemAnalyzer(args.root_path)
    
    # Create output directory
    output_path = Path(args.output_dir)
    output_path.mkdir(exist_ok=True)
    
    print("\nGenerating analysis...")
    analyzer.export_all_visualizations(args.output_dir)
    
    print("\nAnalysis complete! The following files have been generated:")
    print("\nText Representations:")
    print("  - tree_structure.txt: ASCII tree representation")
    print("  - obsidian_links.md: Obsidian-compatible wiki links")
    print("  - structure.json: JSON structure representation")
    print("\nStatistics and Reports:")
    print("  - file_statistics.csv: Detailed file statistics")
    print("  - summary_report.md: Overview and statistics")
    print("\nVisualizations:")
    print("  - interactive_structure.html: Interactive network graph")
    print("  - sunburst_chart.html: Interactive sunburst chart")
    print("  - activity_heatmap.png: File modification patterns")
    print("  - size_distribution.png: File size distribution")

if __name__ == "__main__":
    main() 