#!/bin/bash

# Find all Python files recursively within the current directory
find . -name "*.py" | while IFS= read -r file; do
  # Run each Python file
  echo "Running $file"
  rm "$file"
done