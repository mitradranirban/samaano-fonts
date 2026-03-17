#!/bin/bash

# Find all directories ending in .ufo starting from the current directory
find . -type d -name "*.ufo" | while read -r ufo_dir; do
    
    # Define the source and target paths
    target_file="$ufo_dir/features.fea"
    source_file="$ufo_dir/features_expanded_mark.fea"

    # Check if the specific source file exists within this UFO
    if [ -f "$source_file" ]; then
        echo "Renaming in $ufo_dir..."
        mv "$source_file" "$target_file"
    else
        echo "Skipping $ufo_dir: source file not found."
    fi
done

echo "Done!"
