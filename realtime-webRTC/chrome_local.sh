#!/bin/bash

# Define the Chrome app path and arguments
CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
URL="http://102.218.215.158:8116"
USER_DATA_DIR="/tmp/chrome_dev"

# Run Google Chrome with the specified flags
"$CHROME_PATH" --unsafely-treat-insecure-origin-as-secure="$URL" --user-data-dir="$USER_DATA_DIR"
