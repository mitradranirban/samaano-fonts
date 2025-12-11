#!/usr/bin/env python3
"""
UFO Duplicate Anchor Remover
Checks all glyphs in a UFO font for duplicate anchors and removes duplicates,
keeping only the first occurrence of each anchor name.
"""

import sys
from pathlib import Path
from defcon import Font


def remove_duplicate_anchors(ufo_path):
    """
    Remove duplicate anchors from all glyphs in a UFO font.

    Args:
        ufo_path: Path to the UFO font folder
    """
    ufo_path = Path(ufo_path)

    if not ufo_path.exists():
        print(f"Error: UFO path does not exist: {ufo_path}")
        return False

    if not ufo_path.is_dir():
        print(f"Error: Path is not a directory: {ufo_path}")
        return False

    # Load the UFO font
    print(f"Loading UFO font: {ufo_path}")
    try:
        font = Font(ufo_path)
    except Exception as e:
        print(f"Error loading UFO: {e}")
        return False

    total_duplicates = 0
    glyphs_with_duplicates = []

    # Iterate through all glyphs
    for glyph in font:
        if not glyph.anchors:
            continue

        # Track anchor names and their first occurrence
        seen_anchors = {}
        anchors_to_remove = []

        for anchor in glyph.anchors:
            anchor_name = anchor.name

            if anchor_name in seen_anchors:
                # Duplicate found - mark for removal
                anchors_to_remove.append(anchor)
                total_duplicates += 1
            else:
                # First occurrence - remember it
                seen_anchors[anchor_name] = anchor

        # Remove duplicate anchors
        if anchors_to_remove:
            glyphs_with_duplicates.append(glyph.name)
            for anchor in anchors_to_remove:
                print(f"  Removing duplicate anchor '{anchor.name}' from glyph '{glyph.name}' at ({anchor.x}, {anchor.y})")
                glyph.removeAnchor(anchor)

    # Report results
    print(f"\nProcessed {len(font)} glyphs")
    print(f"Found and removed {total_duplicates} duplicate anchors in {len(glyphs_with_duplicates)} glyphs")

    if glyphs_with_duplicates:
        print(f"\nGlyphs with duplicates removed: {', '.join(glyphs_with_duplicates)}")

    # Save the modified font
    if total_duplicates > 0:
        print(f"\nSaving changes to: {ufo_path}")
        font.save()
        print("Done!")
        return True
    else:
        print("No duplicates found. No changes made.")
        return True


def main():
    if len(sys.argv) != 2:
        print("Usage: python remove_duplicate_anchors.py <path_to_ufo>")
        print("\nExample:")
        print("  python remove_duplicate_anchors.py MyFont.ufo")
        sys.exit(1)

    ufo_path = sys.argv[1]
    success = remove_duplicate_anchors(ufo_path)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
