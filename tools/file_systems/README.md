# Enhanced File System Analysis Tools

A comprehensive toolkit for analyzing file systems, generating reports, and visualizing directory structures.

## Features

- Detailed file and directory statistics
- Tree-style directory visualization (text and markdown formats)
- Git integration for file history
- MIME type detection and file categorization
- Comprehensive Markdown report generation
- Configurable ignored patterns
- Beautiful file type icons
- Error handling for restricted files/directories

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

```bash
python enhanced_file_analysis.py /path/to/analyze -o report.md
```

Options:
- `path`: Directory to analyze (required)
- `-o, --output`: Output report path (optional)
- `--max-depth`: Maximum depth for tree generation (optional)

### Python API

```python
from enhanced_file_analysis import EnhancedFileAnalyzer

# Initialize analyzer
analyzer = EnhancedFileAnalyzer("/path/to/analyze")

# Generate tree representation
tree = analyzer.generate_tree(format='text', max_depth=3)
print(tree)

# Generate and save report
analyzer.generate_markdown_report("report.md")
```

## Report Contents

The generated report includes:
1. Repository overview (file count, total size)
2. File type statistics (by extension and MIME type)
3. Directory structure visualization
4. Recent changes and file history
5. Largest files listing

## Testing

Run the test suite:
```bash
python -m pytest test_enhanced_analysis.py -v
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

MIT License 