#!/bin/bash
# Usage: run this in a directory to process all *-renamed.* files

for f in *-renamed.*; do
  # Only act if such files exist
  [ -e "$f" ] || continue
  base="${f%-renamed.*}"
  ext="${f##*.}"
  target="${base}.${ext}"
  mv -f -- "$f" "$target"
done

