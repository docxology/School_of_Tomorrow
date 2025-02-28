---
title: File Types
type: guide
tags: [documentation, file-types, standards, organization]
created: 2024-03-21
updated: 2024-03-21
status: active
related: [Style_Guide, Metadata_Schema, Folder_Structure]
aliases: [Document Types, Content Types]
---

# File Types

This document defines the standard file types used in the Fuller Obsidian vault and their specific requirements.

## Content Types

### 1. Person (`type: person`)
Files documenting individuals related to Fuller's work and influence.

**Location:** `/people/`
**Naming:** `Lastname_Firstname.md`
**Required Sections:**
- Biography
- Contributions
- Relationship to Fuller's Work
- Key Works
- References

### 2. Concept (`type: concept`)
Core ideas, principles, and theoretical frameworks.

**Location:** `/concepts/`
**Naming:** `Concept_Name.md`
**Required Sections:**
- Definition
- Origins
- Principles
- Applications
- Examples
- References

### 3. Book (`type: book`)
Documentation of books by or about Fuller and related topics.

**Location:** `/books/`
**Naming:** `Book_Title.md`
**Required Sections:**
- Overview
- Key Concepts
- Summary
- Critical Reception
- Editions
- References

### 4. Mathematics (`type: mathematics`)
Mathematical principles, proofs, and geometric concepts.

**Location:** `/mathematics/`
**Naming:** `Mathematical_Concept.md`
**Required Sections:**
- Definition
- Principles
- Proofs
- Applications
- Visualizations
- References

### 5. Technical (`type: technical`)
Technical specifications, designs, and implementations.

**Location:** `/technical/`
**Naming:** `Technical_Name.md`
**Required Sections:**
- Specifications
- Design
- Implementation
- Materials
- Construction
- References

### 6. Place (`type: place`)
Locations significant to Fuller's work.

**Location:** `/places/`
**Naming:** `Place_Name.md`
**Required Sections:**
- Description
- Significance
- History
- Current Status
- References

### 7. Tool (`type: tool`)
Tools, methods, and processes.

**Location:** `/tools/`
**Naming:** `Tool_Name.md`
**Required Sections:**
- Purpose
- Methodology
- Usage
- Examples
- References

## Documentation Types

### 1. Guide (`type: guide`)
Documentation guidelines and standards.

**Location:** `/documentation/guides/`
**Naming:** `Guide_Name.md`
**Required Sections:**
- Purpose
- Guidelines
- Examples
- Implementation
- References

### 2. Schema (`type: schema`)
Data structure and organization definitions.

**Location:** `/documentation/schemas/`
**Naming:** `Schema_Name.md`
**Required Sections:**
- Structure
- Fields
- Validation
- Examples
- References

### 3. Template (`type: template`)
Standard templates for different file types.

**Location:** `/documentation/templates/`
**Naming:** `Template_Name.md`
**Required Sections:**
- Usage
- Structure
- Fields
- Examples

### 4. Workflow (`type: workflow`)
Process and workflow documentation.

**Location:** `/documentation/workflows/`
**Naming:** `Workflow_Name.md`
**Required Sections:**
- Purpose
- Steps
- Requirements
- Examples
- References

## File Structure

### Common Elements
All files must include:
1. YAML Frontmatter
2. Title (H1)
3. Introduction
4. Main Content
5. References
6. Tags

### Formatting
1. Use Markdown syntax
2. Follow heading hierarchy
3. Include internal links
4. Use consistent spacing
5. Include appropriate metadata

## Content Guidelines

### 1. Quality Standards
- Accurate information
- Clear writing
- Proper citations
- Complete metadata
- Consistent formatting

### 2. Cross-referencing
- Use double brackets [[]]
- Link to relevant files
- Maintain bidirectional links
- Check link validity

### 3. Media
- Use appropriate formats
- Include captions
- Optimize file sizes
- Credit sources

### 4. Maintenance
- Regular updates
- Version control
- Link checking
- Content review

## Implementation

### Creation Process
1. Choose appropriate type
2. Use correct template
3. Follow naming convention
4. Add required metadata
5. Include all sections
6. Add proper references

### Validation
1. Check metadata
2. Verify structure
3. Test links
4. Review content
5. Validate formatting

## References
1. [[documentation/guides/Style_Guide]]
2. [[documentation/schemas/Metadata_Schema]]
3. [[documentation/guides/Folder_Structure]]

## Notes
- Follow type requirements
- Maintain consistency
- Update as needed
- Check references

## Tags
#documentation #file-types #standards #organization 