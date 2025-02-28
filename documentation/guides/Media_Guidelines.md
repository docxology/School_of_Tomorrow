---
title: Media Guidelines
type: guide
tags: [media, images, files, guidelines]
created: 2024-02-26
updated: 2024-02-26
status: active
related: [[Style_Guide]], [[Content_Guidelines]]
---

# Media Guidelines

Standards and best practices for handling media files in the Fuller Knowledge Base.

## Media Types

### Supported Formats

#### Images
```yaml
formats:
  - png:  # Preferred for diagrams and screenshots
    max_size: 2MB
    resolution: "1920x1080 max"
  - jpg:  # Preferred for photographs
    max_size: 1MB
    quality: "85%"
  - svg:  # Preferred for vector graphics
    max_size: 500KB
    type: "vector"
  - gif:  # Limited use, only when animation is essential
    max_size: 5MB
    duration: "10s max"
```

#### Documents
```yaml
formats:
  - pdf:  # Preferred for formal documents
    max_size: 10MB
  - markdown:  # Preferred for text content
    max_size: 1MB
  - txt:  # Acceptable for plain text
    max_size: 1MB
```

#### Other Media
```yaml
formats:
  - audio:
    formats: [mp3, wav]
    max_size: 20MB
  - video:
    formats: [mp4]
    max_size: 50MB
    resolution: "1080p max"
```

## File Organization

### Directory Structure
```
media/
├── images/
│   ├── diagrams/
│   ├── photos/
│   └── icons/
├── documents/
│   ├── papers/
│   └── presentations/
└── other/
    ├── audio/
    └── video/
```

### Naming Conventions
```yaml
naming:
  pattern: "{category}-{description}-{date}"
  example: "diagram-tensegrity-20240226"
  rules:
    - lowercase
    - hyphen-separated
    - no spaces
    - descriptive
```

## Usage in Documents

### Image Embedding
```markdown
<!-- Basic image -->
![[image-name.png]]

<!-- With dimensions -->
![[image-name.png|500x300]]

<!-- With caption -->
![[image-name.png|caption]]

<!-- With alignment -->
![[image-name.png|center]]
```

### Document Linking
```markdown
<!-- PDF embedding -->
![[document-name.pdf]]

<!-- Specific page -->
![[document-name.pdf#page=5]]

<!-- Page range -->
![[document-name.pdf#page=5-7]]
```

### Media Galleries
```markdown
<!-- Image gallery -->
![[gallery-1.jpg]]
![[gallery-2.jpg]]
![[gallery-3.jpg]]
```

## Media Processing

### Image Optimization
1. Resize to appropriate dimensions
2. Compress without quality loss
3. Convert to appropriate format
4. Add metadata

### Document Processing
1. OCR when needed
2. Compress PDFs
3. Extract text content
4. Generate previews

### Batch Processing
Using [[Media_Processor]]:
```bash
# Process all images in directory
media-processor optimize ./images/*

# Convert documents to PDF
media-processor convert ./documents/* --to pdf
```

## Metadata Requirements

### Image Metadata
```yaml
---
title: Image Title
description: Brief description
source: Original source
date: YYYY-MM-DD
rights: Copyright status
tags: [relevant, tags]
---
```

### Document Metadata
```yaml
---
title: Document Title
author: Author Name
date: YYYY-MM-DD
version: 1.0
status: [draft|final]
tags: [relevant, tags]
---
```

## Quality Standards

### Image Quality
- Minimum resolution: 72dpi
- Maximum dimensions: 1920x1080
- Clear and legible
- Proper contrast
- Consistent style

### Document Quality
- Searchable text
- Clear formatting
- Proper structure
- Complete metadata

## Accessibility

### Requirements
1. Alt text for images
2. Transcripts for audio
3. Captions for video
4. Screen reader compatibility

### Implementation
```markdown
<!-- Image with alt text -->
![[image.png|alt=Detailed description of image]]

<!-- Audio with transcript -->
![[audio.mp3]]
[[audio-transcript.md]]
```

## Storage and Backup

### Local Storage
- Keep original files
- Maintain version history
- Regular backups
- Organized structure

### Cloud Storage
- Automatic sync
- Version control
- Access control
- Redundancy

## Integration

### With Obsidian
- Use internal links
- Maintain local copies
- Follow naming conventions
- Use supported formats

### With Tools
- [[Media_Processor]] for optimization
- [[Tag_Generator]] for metadata
- [[Link_Discoverer]] for references
- [[Quality_Checker]] for validation

## Best Practices

### General Guidelines
1. Optimize before upload
2. Include complete metadata
3. Follow naming conventions
4. Maintain organization

### Performance
1. Monitor file sizes
2. Use appropriate formats
3. Optimize loading times
4. Cache when possible

## Troubleshooting

### Common Issues
1. File too large
2. Wrong format
3. Missing metadata
4. Broken links

### Solutions
1. Use optimization tools
2. Convert to supported format
3. Add required metadata
4. Fix or update links

## Resources

### Tools
- [[Image_Optimizer]]
- [[PDF_Processor]]
- [[Media_Converter]]
- [[Metadata_Editor]]

### Documentation
- [[File_Format_Guide]]
- [[Optimization_Guide]]
- [[Storage_Guide]]
- [[Backup_Guide]]

## Tags
#media #guidelines #images #documents #accessibility 