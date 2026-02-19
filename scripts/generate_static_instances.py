#!/usr/bin/env python3
"""
Generate static font instances from a variable font using fontTools.
This script reads all named instances from the fvar and name tables,
then generates static .ttf files for each instance.
"""

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.varLib.mutator import instantiateVariableFont as mutator_instantiate
from pathlib import Path
import sys

def generate_static_instances(vf_path, output_dir=None):
    """
    Generate static font instances from a variable font.

    Args:
        vf_path: Path to the variable font file (.ttf)
        output_dir: Directory to save static instances (default: same as input)
    """
    vf_path = Path(vf_path)

    if not vf_path.exists():
        print(f"Error: Font file '{vf_path}' not found")
        return

    # Load the variable font
    font = TTFont(vf_path)

    # Check if font has fvar table (variable font)
    if 'fvar' not in font:
        print(f"Error: '{vf_path}' is not a variable font (no fvar table)")
        return

    # Set output directory
    if output_dir is None:
        output_dir = vf_path.parent
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    # Get axis tags
    axes = {axis.axisTag: axis for axis in font['fvar'].axes}
    axis_tags = list(axes.keys())

    print(f"Variable font: {vf_path.name}")
    print(f"Axes: {', '.join(axis_tags)}")
    print(f"Found {len(font['fvar'].instances)} named instances\n")

    # Generate static instance for each named instance
    for idx, instance in enumerate(font['fvar'].instances):
        # Get instance name from name table
        subfamily_name_id = instance.subfamilyNameID
        instance_name = font['name'].getName(subfamily_name_id, 3, 1, 0x409)

        if instance_name is None:
            instance_name = font['name'].getName(subfamily_name_id, 1, 0, 0)

        if instance_name:
            instance_name = instance_name.toUnicode()
        else:
            instance_name = f"Instance_{idx}"

        # Get axis coordinates for this instance
        coordinates = instance.coordinates

        # Create output filename
        safe_name = instance_name.replace(' ', '-').replace('/', '-')
        output_path = output_dir / f"{vf_path.stem}-{safe_name}.ttf"

        print(f"Generating [{idx+1}/{len(font['fvar'].instances)}]: {safe_name}")
        print(f"  Coordinates: {coordinates}")

        # Reload font for each instance (critical to avoid contamination)
        instance_font = TTFont(vf_path)

        # Instantiate the variable font at the specific coordinates
        # This pins the axes and removes variation tables
        instantiateVariableFont(instance_font, coordinates, inplace=True)

        # Update the name table to reflect this is a static instance
        # Remove references to "Variable" in font names
        for nameRecord in instance_font['name'].names:
            if nameRecord.nameID in [1, 4, 6]:  # Family, Full name, PostScript name
                text = nameRecord.toUnicode()
                if 'Variable' in text:
                    text = text.replace('Variable', '').strip()
                    nameRecord.string = text

        # Save the static instance
        instance_font.save(output_path)

        # Verify it's actually static
        verify_font = TTFont(output_path)
        is_static = 'fvar' not in verify_font and 'gvar' not in verify_font
        verify_font.close()

        status = "✓ Static" if is_static else "✗ Still variable!"
        print(f"  Saved: {output_path.name} {status}\n")

    print(f"Successfully generated {len(font['fvar'].instances)} static instances")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_static_instances.py <variable-font.ttf> [output-dir]")
        print("\nExample:")
        print("  python generate_static_instances.py Samaano-VF.ttf")
        print("  python generate_static_instances.py Samaano-VF.ttf ./static")
        sys.exit(1)

    vf_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    generate_static_instances(vf_path, output_dir)
