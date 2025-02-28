#!/usr/bin/env python3
"""
File System Analysis Tools
-------------------------
A comprehensive toolkit for analyzing and visualizing repository structure
with support for multiple output formats including Obsidian-compatible links.
"""

import json
from pathlib import Path
from datetime import datetime
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, Union, Optional
import plotly.graph_objects as go
from collections import defaultdict
import seaborn as sns

class FileSystemAnalyzer:
    def __init__(self, root_path: Union[str, Path]):
        """Initialize the analyzer with a root directory path."""
        self.root_path = Path(root_path)
        self.ignored_patterns = ['.git', '__pycache__', '.pytest_cache']
        self._cache = {}
        
    def get_file_stats(self, path: Path) -> Dict:
        """Get detailed statistics for a file."""
        if str(path) in self._cache:
            return self._cache[str(path)]
            
        stats = path.stat()
        result = {
            'size': stats.st_size,
            'created': datetime.fromtimestamp(stats.st_ctime),
            'modified': datetime.fromtimestamp(stats.st_mtime),
            'is_dir': path.is_dir(),
            'extension': path.suffix[1:] if path.suffix else None,
            'depth': len(path.relative_to(self.root_path).parts),
            'name': path.name,
            'parent': str(path.parent.relative_to(self.root_path)) if path != self.root_path else None
        }
        
        self._cache[str(path)] = result
        return result

    def generate_tree(self, 
                     format: str = 'text', 
                     max_depth: Optional[int] = None,
                     include_stats: bool = False) -> str:
        """
        Generate a tree representation of the file system.
        
        Args:
            format: Output format ('text', 'markdown', 'obsidian', 'json')
            max_depth: Maximum depth to traverse
            include_stats: Whether to include file statistics
        """
        def _build_tree(path: Path, depth: int = 0) -> Union[str, Dict]:
            if max_depth is not None and depth > max_depth:
                return "..."
            
            if any(ignored in str(path) for ignored in self.ignored_patterns):
                return None
                
            if path.is_file():
                stats = self.get_file_stats(path) if include_stats else {}
                if format == 'obsidian':
                    return f"[[{path.relative_to(self.root_path)}]]"
                elif format == 'json':
                    return {
                        'type': 'file',
                        'name': path.name,
                        'stats': stats
                    }
                else:
                    stats_str = f" ({stats['size']} bytes)" if include_stats else ""
                    return f"{'  ' * depth}📄 {path.name}{stats_str}"
            
            contents = []
            try:
                for item in sorted(path.iterdir()):
                    result = _build_tree(item, depth + 1)
                    if result:
                        contents.append(result)
            except PermissionError:
                return None
                
            if format == 'json':
                return {
                    'type': 'directory',
                    'name': path.name,
                    'contents': contents
                }
            elif format == 'obsidian':
                return '\n'.join(contents)
            else:
                prefix = '  ' * depth + '📁 ' if depth > 0 else ''
                return f"{prefix}{path.name}\n" + '\n'.join(contents)
                
        result = _build_tree(self.root_path)
        if format == 'json':
            return json.dumps(result, default=str, indent=2)
        return result

    def generate_statistics(self) -> pd.DataFrame:
        """Generate detailed statistics about the repository structure."""
        stats = []
        
        for path in self.root_path.rglob('*'):
            if any(ignored in str(path) for ignored in self.ignored_patterns):
                continue
                
            file_stats = self.get_file_stats(path)
            stats.append({
                'path': str(path.relative_to(self.root_path)),
                'type': 'directory' if file_stats['is_dir'] else 'file',
                'size': file_stats['size'],
                'extension': file_stats['extension'],
                'created': file_stats['created'],
                'modified': file_stats['modified']
            })
            
        return pd.DataFrame(stats)

    def visualize_structure(self, output_path: str = 'repo_structure.html'):
        """Generate an interactive visualization of the repository structure."""
        G = nx.Graph()
        
        def add_nodes(path: Path, parent=None):
            current = str(path.relative_to(self.root_path))
            G.add_node(current)
            
            if parent:
                G.add_edge(parent, current)
            
            if path.is_dir():
                for child in path.iterdir():
                    if any(ignored in str(child) for ignored in self.ignored_patterns):
                        continue
                    add_nodes(child, current)
        
        add_nodes(self.root_path)
        
        # Create Plotly figure
        pos = nx.spring_layout(G)
        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        node_x = [pos[node][0] for node in G.nodes()]
        node_y = [pos[node][1] for node in G.nodes()]
        
        fig = go.Figure(
            data=[
                go.Scatter(x=edge_x, y=edge_y, line=dict(width=0.5, color='#888'), hoverinfo='none', mode='lines'),
                go.Scatter(x=node_x, y=node_y, mode='markers+text', 
                          text=list(G.nodes()),
                          textposition="bottom center",
                          hoverinfo='text',
                          marker=dict(size=10))
            ],
            layout=go.Layout(
                title='Repository Structure Visualization',
                showlegend=False,
                hovermode='closest',
                margin=dict(b=0,l=0,r=0,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
            )
        )
        
        fig.write_html(output_path)

    def analyze_file_types(self) -> Dict[str, Dict]:
        """
        Analyze file types in the repository.
        Returns statistics about different file extensions.
        """
        extension_stats = defaultdict(lambda: {'count': 0, 'total_size': 0, 'files': []})
        
        for path in self.root_path.rglob('*'):
            if path.is_file() and not any(ignored in str(path) for ignored in self.ignored_patterns):
                stats = self.get_file_stats(path)
                ext = stats['extension'] or 'no_extension'
                extension_stats[ext]['count'] += 1
                extension_stats[ext]['total_size'] += stats['size']
                extension_stats[ext]['files'].append(str(path.relative_to(self.root_path)))
                
        return dict(extension_stats)

    def generate_sunburst_chart(self, output_path: str = 'file_structure_sunburst.html'):
        """
        Generate an interactive sunburst chart of the directory structure.
        """
        def process_directory(path: Path) -> dict:
            result = {'name': path.name or str(path), 'children': []}
            
            try:
                for item in sorted(path.iterdir()):
                    if any(ignored in str(item) for ignored in self.ignored_patterns):
                        continue
                        
                    if item.is_dir():
                        result['children'].append(process_directory(item))
                    else:
                        stats = self.get_file_stats(item)
                        result['children'].append({
                            'name': item.name,
                            'value': stats['size'],
                            'type': 'file'
                        })
            except PermissionError:
                pass
                
            return result
            
        data = process_directory(self.root_path)
        
        fig = go.Figure(go.Sunburst(
            ids=[],
            labels=[],
            parents=[],
            values=[],
            branchvalues="total",
        ))
        
        def process_for_sunburst(node, parent=""):
            current_id = f"{parent}/{node['name']}" if parent else node['name']
            fig.data[0].ids = fig.data[0].ids + (current_id,)
            fig.data[0].labels = fig.data[0].labels + (node['name'],)
            fig.data[0].parents = fig.data[0].parents + (parent,)
            fig.data[0].values = fig.data[0].values + (node.get('value', 0),)
            
            for child in node.get('children', []):
                process_for_sunburst(child, current_id)
                
        process_for_sunburst(data)
        
        fig.update_layout(
            title="Repository Structure Sunburst Chart",
            width=1000,
            height=1000
        )
        
        fig.write_html(output_path)

    def generate_heatmap(self, output_path: str = 'file_activity_heatmap.png'):
        """
        Generate a heatmap of file modifications over time.
        """
        stats_df = self.generate_statistics()
        stats_df['date'] = pd.to_datetime(stats_df['modified']).dt.date
        stats_df['hour'] = pd.to_datetime(stats_df['modified']).dt.hour
        
        pivot_table = pd.pivot_table(
            stats_df,
            values='size',
            index='date',
            columns='hour',
            aggfunc='count',
            fill_value=0
        )
        
        plt.figure(figsize=(15, 8))
        sns.heatmap(pivot_table, cmap='YlOrRd', cbar_kws={'label': 'Number of Files Modified'})
        plt.title('File Modification Activity Heatmap')
        plt.xlabel('Hour of Day')
        plt.ylabel('Date')
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()

    def generate_size_distribution(self, output_path: str = 'file_size_distribution.png'):
        """
        Generate a visualization of file size distribution.
        """
        stats_df = self.generate_statistics()
        stats_df['size_kb'] = stats_df['size'] / 1024
        
        plt.figure(figsize=(12, 6))
        sns.histplot(data=stats_df, x='size_kb', bins=50, log_scale=True)
        plt.title('File Size Distribution')
        plt.xlabel('File Size (KB)')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()

    def export_all_visualizations(self, output_dir: str = 'file_system_analysis'):
        """
        Generate and export all available visualizations and reports.
        """
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # Generate basic tree structure
        with open(output_path / 'tree_structure.txt', 'w') as f:
            f.write(self.generate_tree(format='text'))
            
        with open(output_path / 'obsidian_links.md', 'w') as f:
            f.write(self.generate_tree(format='obsidian'))
            
        with open(output_path / 'structure.json', 'w') as f:
            f.write(self.generate_tree(format='json'))
            
        # Generate statistics
        stats_df = self.generate_statistics()
        stats_df.to_csv(output_path / 'file_statistics.csv')
        
        # Generate summary report
        with open(output_path / 'summary_report.md', 'w') as f:
            f.write("# Repository Structure Analysis\n\n")
            f.write(f"Analysis generated on: {datetime.now()}\n\n")
            
            f.write("## General Statistics\n")
            f.write(f"- Total files: {len(stats_df)}\n")
            f.write(f"- Total size: {stats_df['size'].sum() / (1024*1024):.2f} MB\n")
            f.write(f"- Average file size: {stats_df['size'].mean() / 1024:.2f} KB\n")
            f.write(f"- Median file size: {stats_df['size'].median() / 1024:.2f} KB\n")
            
            f.write("\n## File Types\n")
            for ext, stats in self.analyze_file_types().items():
                f.write(f"### {ext}\n")
                f.write(f"- Count: {stats['count']}\n")
                f.write(f"- Total size: {stats['total_size'] / 1024:.2f} KB\n")
                
        # Generate visualizations
        self.visualize_structure(str(output_path / 'interactive_structure.html'))
        self.generate_sunburst_chart(str(output_path / 'sunburst_chart.html'))
        self.generate_heatmap(str(output_path / 'activity_heatmap.png'))
        self.generate_size_distribution(str(output_path / 'size_distribution.png'))

def main():
    """Example usage of the FileSystemAnalyzer."""
    analyzer = FileSystemAnalyzer('.')
    analyzer.export_all_visualizations()

if __name__ == "__main__":
    main()