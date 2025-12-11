#!/usr/bin/env python3
"""
FontForge SFD Duplicate Anchor Remover
Checks all glyphs in a FontForge SFD file for duplicate anchors and removes duplicates,
keeping only the first occurrence of each anchor name.
"""

import sys
import fontforge
from pathlib import Path


def remove_duplicate_anchors(sfd_path):
    """
    Remove duplicate anchors from all glyphs in a FontForge SFD file.

    Args:
        sfd_path: Path to the SFD file
    """
    sfd_path = Path(sfd_path)

    if not sfd_path.exists():
        print(f"Error: SFD file does not exist: {sfd_path}")
        return False

    if not sfd_path.is_file():
        print(f"Error: Path is not a file: {sfd_path}")
        return False

    # Load the SFD font
    print(f"Loading SFD font: {sfd_path}")
    try:
        font = fontforge.open(str(sfd_path))
    except Exception as e:
        print(f"Error loading SFD: {e}")
        return False

    total_duplicates = 0
    glyphs_with_duplicates = []
    total_glyphs = 0

    # Iterate through all glyphs
    for glyph in font.glyphs():
        total_glyphs += 1

        # Get all anchor points for this glyph
        anchors = glyph.anchorPoints

        if not anchors:
            continue

        # Track anchor names and their first occurrence
        seen_anchors = {}
        anchors_to_keep = []
        duplicates_found = []

        for anchor in anchors:
            # anchor is a tuple: (anchor_class_name, anchor_type, x, y)
            # anchor_type: "mark", "base", "ligature", "basemark", "entry", "exit", "baselig"
            anchor_name = anchor[0]  # anchor class name
            anchor_type = anchor[1]  # anchor type
            anchor_x = anchor[2]
            anchor_y = anchor[3]

            # Create a unique key combining name and type
            anchor_key = (anchor_name, anchor_type)

            if anchor_key in seen_anchors:
                # Duplicate found
                duplicates_found.append((anchor_name, anchor_type, anchor_x, anchor_y))
                total_duplicates += 1
            else:
                # First occurrence - keep it
                seen_anchors[anchor_key] = anchor
                anchors_to_keep.append(anchor)

        # If duplicates were found, remove all anchors and re-add only the ones to keep
        if duplicates_found:
            glyphs_with_duplicates.append(glyph.glyphname)

            # Remove all anchors
            glyph.anchorPoints = ()

            # Re-add only the first occurrence of each anchor
            for anchor in anchors_to_keep:
                glyph.addAnchorPoint(anchor[0], anchor[1], anchor[2], anchor[3])

            # Report what was removed
            for dup in duplicates_found:
                print(f"  Removing duplicate anchor '{dup[0]}' ({dup[1]}) from glyph '{glyph.glyphname}' at ({dup[2]}, {dup[3]})")

    # Report results
    print(f"\nProcessed {total_glyphs} glyphs")
    print(f"Found and removed {total_duplicates} duplicate anchors in {len(glyphs_with_duplicates)} glyphs")

    if glyphs_with_duplicates:
        print(f"\nGlyphs with duplicates removed: {', '.join(glyphs_with_duplicates)}")

    # Save the modified font
    if total_duplicates > 0:
        print(f"\nSaving changes to: {sfd_path}")
        font.save(str(sfd_path))
        print("Done!")
        font.close()
        return True
    else:
        print("No duplicates found. No changes made.")
        font.close()
        return True


def main():
    if len(sys.argv) != 2:
        print("Usage: python remove_duplicate_anchors_sfd.py <path_to_sfd>")
        print("\nExample:")
        print("  python remove_duplicate_anchors_sfd.py MyFont.sfd")
        sys.exit(1)

    sfd_path = sys.argv[1]
    success = remove_duplicate_anchors(sfd_path)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
