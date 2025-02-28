#!/bin/bash

# Repository Analysis Script
# -------------------------
# Analyzes repository structure and generates various reports

# Set up variables
OUTPUT_DIR="file_system_analysis"
REPO_ROOT="$(pwd)"
IGNORED_PATTERNS=".git|__pycache__|.pytest_cache"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Function to generate tree structure
generate_tree() {
    echo "Generating tree structure..."
    {
        echo "Repository Structure"
        echo "==================="
        echo
        tree -a -I "$IGNORED_PATTERNS" --dirsfirst
    } > "$OUTPUT_DIR/tree_structure.txt"
}

# Function to generate file statistics
generate_stats() {
    echo "Generating file statistics..."
    {
        echo "File Statistics"
        echo "=============="
        echo
        echo "Total files:"
        find . -type f -not -path "*/\.*" | wc -l
        
        echo
        echo "Files by extension:"
        find . -type f -not -path "*/\.*" -printf "%f\n" | grep -o "\.[^\.]*$" | sort | uniq -c | sort -rn
        
        echo
        echo "Largest files:"
        find . -type f -not -path "*/\.*" -printf "%s %p\n" | sort -rn | head -n 10 | \
            awk '{printf "%10.2f MB  %s\n", $1/1024/1024, $2}'
            
        echo
        echo "Recently modified files:"
        find . -type f -not -path "*/\.*" -mtime -7 -printf "%TY-%Tm-%Td %TH:%TM  %p\n" | sort -r
    } > "$OUTPUT_DIR/file_statistics.txt"
}

# Function to generate Obsidian links
generate_obsidian_links() {
    echo "Generating Obsidian links..."
    {
        echo "# Repository Files"
        echo
        find . -type f -not -path "*/\.*" -printf "[[%P]]\n" | sort
    } > "$OUTPUT_DIR/obsidian_links.md"
}

# Function to generate file type analysis
generate_file_type_analysis() {
    echo "Generating file type analysis..."
    {
        echo "File Type Analysis"
        echo "=================="
        echo
        echo "MIME Types:"
        find . -type f -not -path "*/\.*" -exec file --mime-type {} \; | \
            sort | awk -F: '{print $2}' | sort | uniq -c | sort -rn
    } > "$OUTPUT_DIR/file_types.txt"
}

# Function to generate summary report
generate_summary() {
    echo "Generating summary report..."
    {
        echo "# Repository Analysis Summary"
        echo
        echo "Generated on: $(date)"
        echo
        echo "## Repository Size"
        echo
        echo "Total size: $(du -sh . | cut -f1)"
        echo
        echo "## Directory Structure"
        echo
        echo "\`\`\`"
        tree -d -L 2 -I "$IGNORED_PATTERNS"
        echo "\`\`\`"
        echo
        echo "## File Types"
        echo
        echo "Most common file extensions:"
        echo "\`\`\`"
        find . -type f -not -path "*/\.*" -printf "%f\n" | grep -o "\.[^\.]*$" | sort | uniq -c | sort -rn | head -n 10
        echo "\`\`\`"
    } > "$OUTPUT_DIR/summary_report.md"
}

# Main execution
echo "Starting repository analysis..."
echo "Output will be saved to: $OUTPUT_DIR"

generate_tree
generate_stats
generate_obsidian_links
generate_file_type_analysis
generate_summary

echo
echo "Analysis complete! The following files have been generated:"
echo "  - tree_structure.txt: Complete repository tree"
echo "  - file_statistics.txt: Detailed file statistics"
echo "  - obsidian_links.md: Obsidian-compatible wiki links"
echo "  - file_types.txt: File type analysis"
echo "  - summary_report.md: Overview and statistics" 