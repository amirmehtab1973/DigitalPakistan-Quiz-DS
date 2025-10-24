#!/bin/bash

# Setup script for Streamlit deployment

echo "Setting up Digital Pakistan Quiz App..."

# Create necessary directories
mkdir -p .streamlit

# Create config file if it doesn't exist
if [ ! -f .streamlit/config.toml ]; then
    cat > .streamlit/config.toml << EOF
[server]
headless = true
enableCORS = false
enableXsrfProtection = false

[browser]
serverAddress = "0.0.0.0"
serverPort = 8501
EOF
fi

echo "Setup completed!"
