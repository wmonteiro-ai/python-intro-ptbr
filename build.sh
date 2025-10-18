#!/bin/bash

echo "Building Python Descomplicado with Quarto..."

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies if needed
echo "Installing Python dependencies..."
pip install -r docs/requirements.txt

# Build the book
echo "Building book..."
cd docs
quarto render

# Open the book in browser
echo "Opening book in browser..."
quarto preview

cd ..
echo "Build complete!"