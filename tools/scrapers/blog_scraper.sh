#!/bin/bash

# Blog scraper shell script
# Scrapes Fuller-related blogs and saves content

# Create output directories
mkdir -p output/blogs/{bizmo_diaries,coffee_shops,control_room,world_game}/{posts,metadata,logs}

# Blog URLs (using Atom feeds)
BIZMO_URL="https://mybizmo.blogspot.com/feeds/posts/default"
COFFEE_URL="https://coffeeshopsnet.blogspot.com/feeds/posts/default"
CONTROL_URL="https://controlroom.blogspot.com/feeds/posts/default"
WORLD_URL="https://worldgame.blogspot.com/feeds/posts/default"

# Function to decode HTML entities
decode_html() {
    sed 's/&lt;/</g; s/&gt;/>/g; s/&amp;/\&/g; s/&quot;/"/g; s/&#39;/'"'"'/g'
}

# Function to extract value between XML tags
extract_xml_value() {
    local xml="$1"
    local tag="$2"
    echo "$xml" | xmllint --html --xpath "string(//$tag)" - 2>/dev/null
}

# Function to extract HTML content between XML tags
extract_xml_content() {
    local xml="$1"
    local tag="$2"
    echo "$xml" | xmllint --html --xpath "string(//content)" - 2>/dev/null
}

# Function to clean HTML content
clean_html() {
    local content="$1"
    echo "$content" | decode_html | sed -e 's/<[^>]*>//g' | sed -e 's/^[[:space:]]*//;s/[[:space:]]*$//' | tr -s ' '
}

# Function to scrape a blog
scrape_blog() {
    local url="$1"
    local output_dir="$2"
    local blog_name="$3"
    local feed_file="$output_dir/logs/feed.xml"
    local post_count=0

    echo "Scraping $blog_name from $url"
    
    # Fetch the feed
    curl -s -A "Mozilla/5.0" -H "Accept: application/atom+xml" "$url" > "$feed_file"
    
    # Create a temporary directory for post files
    local tmp_dir=$(mktemp -d)
    
    # Split feed into individual entries
    csplit -f "$tmp_dir/post" "$feed_file" '/<entry>/' '{*}' > /dev/null 2>&1
    
    # Process each entry file
    for entry_file in "$tmp_dir"/post*; do
        if [ -f "$entry_file" ]; then
            local entry=$(cat "$entry_file")
            
            # Extract post details
            local title=$(extract_xml_value "$entry" "title")
            local published=$(extract_xml_value "$entry" "published")
            local updated=$(extract_xml_value "$entry" "updated")
            local content=$(extract_xml_content "$entry" "content")
            
            if [ ! -z "$title" ] && [ ! -z "$content" ]; then
                # Create post ID from title
                local post_id=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/-\+/-/g' | sed 's/^-\|-$//')
                
                # Clean content
                local clean_content=$(clean_html "$content")
                
                # Save post content
                echo "# $title" > "$output_dir/posts/$post_id.md"
                echo -e "\nPublished: $published" >> "$output_dir/posts/$post_id.md"
                [ ! -z "$updated" ] && echo "Updated: $updated" >> "$output_dir/posts/$post_id.md"
                echo -e "\n$clean_content" >> "$output_dir/posts/$post_id.md"
                
                # Save metadata
                cat > "$output_dir/metadata/$post_id.json" << EOF
{
    "title": "$title",
    "published": "$published",
    "updated": "$updated",
    "blog_name": "$blog_name"
}
EOF
                
                ((post_count++))
                echo "Saved post: $title"
            fi
        fi
    done
    
    # Cleanup
    rm -rf "$tmp_dir"
    
    echo "Scraped $post_count posts from $blog_name"
    return $post_count
}

# Main scraping process
total_posts=0

scrape_blog "$BIZMO_URL" "output/blogs/bizmo_diaries" "BizMo Diaries"
total_posts=$((total_posts + $?))

scrape_blog "$COFFEE_URL" "output/blogs/coffee_shops" "Coffee Shops Network" 
total_posts=$((total_posts + $?))

scrape_blog "$CONTROL_URL" "output/blogs/control_room" "Control Room"
total_posts=$((total_posts + $?))

scrape_blog "$WORLD_URL" "output/blogs/world_game" "World Game"
total_posts=$((total_posts + $?))

echo "Total posts scraped: $total_posts"

# Generate simple HTML report
cat > output/blogs/scraping_report.html << EOF
<html>
<head><title>Blog Scraping Report</title></head>
<body>
<h1>Blog Scraping Report</h1>
<p>Total posts scraped: $total_posts</p>
<p>Timestamp: $(date)</p>
</body>
</html>
EOF 