#!/bin/bash

# Rover MCP Server Wrapper Script
# This script ensures proper environment setup and starts the MCP server

# Set working directory
TARGET_DIR="/Users/ggeorgie/code/projects/sp-hackathon/rover-mcp-local"
cd "${TARGET_DIR}"

# Set environment variables
export MCP_TRANSPORT="stdio"
export CERT_FILE="${TARGET_DIR}/sa-cert.crt"
export KEY_FILE="${TARGET_DIR}/privkey.pem"
export PYTHONIOENCODING="utf-8"
export PYTHONUNBUFFERED="1"

# Use the full Python path
PYTHON_PATH="/Users/ggeorgie/miniconda3/bin/python"

# Start the MCP server
exec "${PYTHON_PATH}" mcp_server.py 