#!/bin/bash

# Setup script for the Python DBMS project
# This script sets up the virtual environment, installs dependencies, and initializes the MySQL database

# Colors for better readability
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}===================================================${NC}"
echo -e "${GREEN}        Setting up your project environment        ${NC}"
echo -e "${BLUE}===================================================${NC}"

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo -e "${RED}uv is not installed. Installing...${NC}"
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Add uv to the current shell session
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Create and activate virtual environment
echo -e "\n${GREEN}Creating virtual environment...${NC}"
uv venv .venv
source .venv/bin/activate || source .venv/Scripts/activate

# Install dependencies
echo -e "\n${GREEN}Installing dependencies...${NC}"
uv pip install mysql-connector-python

# Check if MySQL is installed
if ! command -v mysql &> /dev/null; then
    echo -e "${RED}MySQL is not installed. Please install MySQL before continuing.${NC}"
    echo -e "On macOS: brew install mysql"
    echo -e "On Ubuntu: sudo apt-get install mysql-server"
    echo -e "On Windows: Download from https://dev.mysql.com/downloads/installer/"
    exit 1
fi

# Create database and user
echo -e "\n${GREEN}Setting up database...${NC}"
echo -e "${BLUE}You'll need to enter your MySQL root password${NC}"

mysql -u root -p <<EOF
CREATE DATABASE IF NOT EXISTS mydb;
CREATE USER IF NOT EXISTS 'test'@'localhost' IDENTIFIED BY 'test';
GRANT ALL PRIVILEGES ON mydb.* TO 'test'@'localhost';
FLUSH PRIVILEGES;
USE mydb;
$(cat schema.sql)
EOF

# Check if database setup was successful
if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}Database setup completed successfully!${NC}"
else
    echo -e "\n${RED}Database setup failed. Please check your MySQL installation and credentials.${NC}"
    exit 1
fi

echo -e "\n${GREEN}Setup completed successfully!${NC}"
echo -e "${BLUE}===================================================${NC}"
echo -e "${GREEN}To run the project:${NC}"
echo -e "1. Activate the virtual environment: ${BLUE}source .venv/bin/activate${NC}"
echo -e "2. Run the application: ${BLUE}python main.py${NC}"
echo -e "${BLUE}===================================================${NC}"
