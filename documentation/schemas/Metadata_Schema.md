---
title: Metadata Schema
type: schema
tags: [documentation, metadata, schema, standards]
created: 2024-03-21
updated: 2024-03-21
status: active
related: [Style_Guide, File_Types, Folder_Structure]
aliases: [Frontmatter Schema, YAML Standards]
---

# Metadata Schema

This document defines the standard metadata structure for all documents in the Fuller Obsidian vault.

## Core Schema

### Universal Fields
```yaml
metadata_schema:
  required:
    title: string           # Document title
    type: string           # Document type (see types below)
    tags: array[string]    # Relevant tags
    created: date          # Creation date (YYYY-MM-DD)
    updated: date          # Last update date (YYYY-MM-DD)
    status: string         # active|draft|archived
    related: array[string] # Related documents
    aliases: array[string] # Alternative names
```

### Type-Specific Fields

1. Person Type
```yaml
person_metadata:
  required:
    birth_date: date          # YYYY-MM-DD
    nationality: string       # Primary nationality
    occupation: array[string] # List of occupations
  optional:
    death_date: date         # YYYY-MM-DD
    known_for: array[string] # Notable contributions
    education: array[string] # Educational background
```

2. Concept Type
```yaml
concept_metadata:
  required:
    creator: string          # Original creator/discoverer
    principle: string        # Core principle
  optional:
    period: string          # Development period
    applications: array     # Known applications
    significance: array     # Key importance points
```

3. Book Type
```yaml
book_metadata:
  required:
    author: string          # Primary author
    publication_date: date  # YYYY-MM-DD
    publisher: string       # Original publisher
  optional:
    isbn: string           # ISBN number
    editions: array        # List of editions
    translations: array    # Available translations
```

4. Mathematics Type
```yaml
mathematics_metadata:
  required:
    domain: string         # Mathematical domain
    principles: array      # Core principles
  optional:
    prerequisites: array   # Required knowledge
    applications: array    # Practical applications
    proofs: array         # Related proofs
```

5. Technical Type
```yaml
technical_metadata:
  required:
    category: string       # Technical category
    components: array      # Key components
  optional:
    specifications: object # Technical specs
    materials: array       # Required materials
    tools: array          # Required tools
```

## Valid Values

### Status Options
```yaml
status_values:
  - active    # Current and maintained
  - draft     # In development
  - archived  # Historical/deprecated
```

### Type Options
```yaml
type_values:
  content:
    - person
    - concept
    - book
    - mathematics
    - technical
    - place
    - tool
  documentation:
    - guide
    - schema
    - template
    - workflow
```

### Tag Categories
```yaml
tag_categories:
  - concept
  - person
  - mathematics
  - technical
  - documentation
  - methodology
  - history
  - application
```

## Validation Rules

### Format Requirements
1. Dates
   ```yaml
   date_format: YYYY-MM-DD
   ```

2. Arrays
   ```yaml
   array_format:
     - single line for small arrays
     - multi-line for large arrays
     - consistent indentation
   ```

3. Strings
   ```yaml
   string_format:
     - no special characters except hyphen and underscore
     - consistent capitalization
     - proper escaping when needed
   ```

### Content Rules
1. Title Format
   ```yaml
   title_rules:
     - match file name (with spaces instead of underscores)
     - proper capitalization
     - no abbreviations
   ```

2. Tag Format
   ```yaml
   tag_rules:
     - lowercase
     - hyphenated
     - no spaces
     - from approved list
   ```

3. Related Documents
   ```yaml
   related_rules:
     - full document path
     - exists in vault
     - relevant connection
   ```

## Examples

### Person Document
```yaml
---
title: R. Buckminster Fuller
type: person
tags: [architect, inventor, philosopher, designer]
created: 2024-03-21
updated: 2024-03-21
status: active
birth_date: 1895-07-12
death_date: 1983-07-01
nationality: American
occupation: [architect, inventor, philosopher]
known_for: [Geodesic dome, Dymaxion concepts, Synergetics]
related: [Geodesic_Dome, Dymaxion_House, Synergetics]
aliases: [Bucky Fuller, RBF]
---
```

### Concept Document
```yaml
---
title: Vector Equilibrium
type: concept
tags: [geometry, synergetics, mathematics, structure]
created: 2024-03-21
updated: 2024-03-21
status: active
creator: R. Buckminster Fuller
principle: Nature's zero-reference of energy mathematics
related: [Synergetics, Isotropic_Vector_Matrix]
aliases: [VE, Cuboctahedron]
---
```

## Implementation

### Usage Guidelines
1. Frontmatter Block
   - Place at start of file
   - Use triple-dash delimiters
   - Proper YAML indentation
   - No empty fields

2. Field Order
   - Follow schema order
   - Group related fields
   - Maintain consistency
   - Clear organization

### Validation Process
1. Technical Validation
   - YAML syntax
   - Required fields
   - Valid values
   - Proper formatting

2. Content Validation
   - Logical relationships
   - Accurate information
   - Complete metadata
   - Consistent style

## References
1. [[documentation/guides/Style_Guide]]
2. [[documentation/guides/File_Types]]
3. [[documentation/guides/Folder_Structure]]

## Notes
- Follow schema strictly
- Validate all metadata
- Update as needed
- Maintain consistency

## Tags
#documentation #metadata #schema #standards 