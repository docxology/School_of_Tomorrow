#!/bin/bash

# Create output directory
mkdir -p outputs
timestamp=$(date +%Y%m%d_%H%M%S)

# Repository root directory (absolute path)
repo_root=$(cd "../.." && pwd)

# 1. Generate directory structure tree
echo "Generating directory tree..."
tree_file="outputs/tree_${timestamp}.txt"
tree "$repo_root" -a -I '.git|__pycache__|node_modules|.pytest_cache|venv' --charset=ascii > "$tree_file"
echo "Tree saved to: $tree_file"

# 2. Generate file statistics
echo -e "\nGenerating file statistics..."
stats_file="outputs/stats_${timestamp}.txt"
{
    echo "File System Analysis Report"
    echo "=========================="
    echo "Generated on: $(date)"
    echo
    
    echo "Directory Summary"
    echo "----------------"
    cd "$repo_root"
    echo "Total directories: $(find . -type d -not -path '*/\.*' | wc -l)"
    echo "Total files: $(find . -type f -not -path '*/\.*' | wc -l)"
    echo "Total size: $(du -sh . | cut -f1)"
    echo
    
    echo "File Types"
    echo "----------"
    echo "Extension counts:"
    find . -type f -not -path '*/\.*' -exec basename {} \; | grep -o '\.[^.]*$' | sort | uniq -c | sort -nr
    echo
    
    echo "Recent Changes"
    echo "--------------"
    echo "Most recently modified files:"
    find . -type f -not -path '*/\.*' -printf "%T+ %p\n" | sort -r | head -n 10
    echo
    
    echo "Large Files"
    echo "-----------"
    echo "Largest files:"
    find . -type f -not -path '*/\.*' -exec du -h {} \; | sort -hr | head -n 10
    echo
    
    echo "File Type Details"
    echo "----------------"
    echo "MIME type analysis:"
    find . -type f -not -path '*/\.*' -exec file --mime-type {} \; | sort | uniq -c | sort -nr
} > "$stats_file"
echo "Statistics saved to: $stats_file"

# 3. Generate Markdown report
echo -e "\nGenerating Markdown report..."
markdown_file="outputs/report_${timestamp}.md"
{
    echo "# Repository Analysis Report"
    echo
    echo "Generated on: $(date)"
    echo
    
    echo "## Directory Structure"
    echo
    echo '```'
    tree . -L 3 -a -I '.git|__pycache__|node_modules|.pytest_cache|venv' --charset=ascii
    echo '```'
    echo
    
    echo "## File Statistics"
    echo
    echo "### Overview"
    echo "- Total directories: $(find . -type d -not -path '*/\.*' | wc -l)"
    echo "- Total files: $(find . -type f -not -path '*/\.*' | wc -l)"
    echo "- Repository size: $(du -sh . | cut -f1)"
    echo
    
    echo "### File Types"
    echo
    echo "| Extension | Count |"
    echo "|-----------|-------|"
    find . -type f -not -path '*/\.*' -exec basename {} \; | grep -o '\.[^.]*$' | sort | uniq -c | sort -nr | while read count ext; do
        if [ -n "$ext" ]; then
            echo "| $ext | $count |"
        fi
    done
    echo
    
    echo "### Recent Changes"
    echo
    echo "| Date | File |"
    echo "|------|------|"
    find . -type f -not -path '*/\.*' -printf "%TY-%Tm-%Td %TH:%TM:%TS %p\n" | sort -r | head -n 10 | while read date time file; do
        echo "| $date $time | \`${file#./}\` |"
    done
    echo
    
    echo "### Largest Files"
    echo
    echo "| Size | File |"
    echo "|------|------|"
    find . -type f -not -path '*/\.*' -exec du -h {} \; | sort -hr | head -n 10 | while read size file; do
        echo "| $size | \`${file#./}\` |"
    done
} > "$markdown_file"
echo "Markdown report saved to: $markdown_file"

# 4. Generate visualization data
echo -e "\nGenerating visualization data..."
json_file="outputs/data_${timestamp}.json"
{
    echo "{"
    echo "  \"fileTypes\": {"
    first=true
    find . -type f -not -path '*/\.*' -exec basename {} \; | grep -o '\.[^.]*$' | sort | uniq -c | sort -nr | while read count ext; do
        if [ -n "$ext" ]; then
            if [ "$first" = true ]; then
                first=false
            else
                echo ","
            fi
            echo "    \"$ext\": $count"
        fi
    done
    echo "  },"
    
    echo "  \"directorySizes\": {"
    first=true
    find . -type d -not -path '*/\.*' -exec du -s {} \; | sort -nr | head -n 10 | while read size dir; do
        if [ "$first" = true ]; then
            first=false
        else
            echo ","
        fi
        echo "    \"${dir#./}\": $size"
    done
    echo "  },"
    
    echo "  \"mimeTypes\": {"
    first=true
    find . -type f -not -path '*/\.*' -exec file --mime-type {} \; | sort | uniq -c | sort -nr | while read count mime path; do
        if [ "$first" = true ]; then
            first=false
        else
            echo ","
        fi
        echo "    \"$mime\": $count"
    done
    echo "  }"
    echo "}"
} > "$json_file"
echo "Visualization data saved to: $json_file"

echo -e "\nAnalysis complete! All outputs have been saved to the 'outputs' directory." 