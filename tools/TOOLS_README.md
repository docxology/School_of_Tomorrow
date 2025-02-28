# Fuller Blog Scraping Tools

Tools for scraping, analyzing, and visualizing Buckminster Fuller-related blogs.

## Overview

This toolset provides functionality for:
- Scraping content from Blogspot blogs
- Storing blog posts and metadata
- Generating visualizations and insights
- Analyzing content relationships

## Directory Structure

```
tools/
├── scrapers/
│   ├── blogspot_scraper.py    # Core scraping functionality
│   └── fuller_blogs_scraper.py # Main scraping script
├── visualizers/
│   └── blog_visualizer.py     # Visualization generation
├── output/
│   └── blogs/                 # Scraped blog content
│       ├── bizmo_diaries/
│       ├── coffee_shops/
│       ├── control_room/
│       └── world_game/
└── requirements.txt           # Project dependencies
```

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Scraping Blogs

Run the main scraping script:
```bash
python scrapers/fuller_blogs_scraper.py
```

This will:
- Load blog configurations from `fonds/blogs/blogs_index.md`
- Scrape content from each blog
- Store posts and metadata in the output directory
- Generate basic visualizations

### Output Structure

For each blog, the following is generated:
```
output/blogs/[blog_name]/
├── posts/          # Individual post content in Markdown
├── metadata/       # Post metadata in JSON
├── media/         # Downloaded images and media
├── logs/          # Scraping logs
└── visualizations/ # Generated visualizations
```

### Visualizations

The following visualizations are generated:
- Post timeline
- Word cloud of content
- Link network graph
- Topic distribution

To generate visualizations separately:
```bash
python visualizers/blog_visualizer.py [blog_directory]
```

## Configuration

Blog configurations are stored in `fonds/blogs/blogs_index.md` in YAML format:
```yaml
blogs:
  blog_name:
    url: "blog_url"
    profile: "profile_name"
```

## Development

### Adding New Features

1. Scraper modifications:
   - Edit `blogspot_scraper.py` for core functionality
   - Update `fuller_blogs_scraper.py` for execution logic

2. Visualization additions:
   - Add new visualization methods to `blog_visualizer.py`
   - Update visualization generation in main script

### Testing

Run tests:
```bash
python -m pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details 