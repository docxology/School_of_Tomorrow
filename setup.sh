#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Setting up Buckminster Fuller Knowledge Graph Explorer...${NC}"

# Clear any existing Python environment variables
unset PYTHONPATH PYTHONHOME

# Ensure we're using the system Python for setup
PYTHON_CMD=$(which python3)

# Create virtual environment
echo -e "${GREEN}Creating Python virtual environment...${NC}"
$PYTHON_CMD -m venv .venv

# Create wrapper script
echo -e "${GREEN}Creating wrapper script...${NC}"
cat > run <<EOL
#!/bin/bash
# Unset potentially problematic Python environment variables
unset PYTHONPATH PYTHONHOME

# Activate virtual environment
source "\$(dirname "\$0")/.venv/bin/activate"

# Run the explorer
python "\$(dirname "\$0")/explore.py" "\$@"
EOL

# Make wrapper script executable
chmod +x run

# Activate virtual environment and install dependencies
echo -e "${GREEN}Installing dependencies...${NC}"
source .venv/bin/activate
pip install --upgrade pip
pip install -q rich pyfiglet

echo -e "${BLUE}✨ Setup complete! To run the explorer, simply type:${NC}"
echo -e "${GREEN}./run${NC}" 