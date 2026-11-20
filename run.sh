#!/bin/bash

# LearnMate Startup Script

echo "========================================="
echo "  LearnMate - Skill Exchange Platform   "
echo "========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt --quiet

echo ""
echo "Starting LearnMate application..."
echo "Access the application at: http://127.0.0.1:5000"
echo ""
echo "Default Admin Credentials:"
echo "Username: admin"
echo "Password: admin123"
echo ""
echo "Press Ctrl+C to stop the server"
echo "========================================="
echo ""

# Run the application
python app.py
