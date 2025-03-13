#!/usr/bin/env python3
import os
import sys
import argparse
from fontTools.ttLib import TTFont
from fontTools.varLib.mutator import instantiateVariableFont
from itertools import product

def get_all_named_instances(font_path):
    """Extract all named instances from the STAT table of a variable font."""
    font = TTFont(font_path)
    
    # Verify it's a variable font
    if 'fvar' not in font:
        raise ValueError(f"{os.path.basename(font_path)} is not a variable font (no 'fvar' table found).")
    
    # Get axis information from fvar table
    axes = {}
    for axis in font['fvar'].axes:
        axes[axis.axisTag] = {
            'min': axis.minValue,
            'max': axis.maxValue,
            'default': axis.defaultValue
        }
    
    # Check if STAT table exists
    if 'STAT' not in font:
        raise ValueError(f"{os.path.basename(font_path)} does not have a STAT table.")
    
    # Extract named instances from STAT table
    named_values = {}
    
    # Process STAT format 1 (individual axes)
    if hasattr(font['STAT'], 'table') and hasattr(font['STAT'].table, 'AxisValueArray'):
        for value_record in font['STAT'].table.AxisValueArray.AxisValue:
            # Only process format 1 and 3 records (individual axis values with names)
            if hasattr(value_record, 'Format') and value_record.Format in (1, 3):
                axis_tag = font['STAT'].table.DesignAxisRecord.Axis[value_record.AxisIndex].AxisTag
                
                if axis_tag not in named_values:
                    named_values[axis_tag] = []
                
                if value_record.Format == 1:
                    value = value_record.Value
                elif value_record.Format == 3:
                    value = value_record.NominalValue
                
                name_id = value_record.ValueNameID
                name = font['name'].getNameFromID(name_id)
                
                if name:
                    named_values[axis_tag].append({
                        'value': value,
                        'name': name.toUnicode()
                    })
    
    # Process named instances from fvar table as a fallback
    if not named_values and 'fvar' in font and font['fvar'].instances:
        for instance in font['fvar'].instances:
            name = font['name'].getNameFromID(instance.subfamilyNameID)
            if name:
                instance_name = name.toUnicode()
                for axis_tag, value in instance.coordinates.items():
                    if axis_tag not in named_values:
                        named_values[axis_tag] = []
                    
                    # Check if we already have this value
                    if not any(v['value'] == value for v in named_values[axis_tag]):
                        named_values[axis_tag].append({
                            'value': value,
                            'name': f"{axis_tag}={value}"  # Simple naming as fallback
                        })
    
    font.close()
    return named_values, axes

def generate_all_combinations(named_values):
    """Generate all possible combinations of named axis values."""
    axis_tags = named_values.keys()
    values_per_axis = [[(tag, val['value'], val['name']) for val in named_values[tag]] for tag in axis_tags]
    
    if not values_per_axis:
        return []
    
    # Get all possible combinations
    combinations = list(product(*values_per_axis))
    
    # Convert to a list of dictionaries with coordinates and instance name
    result = []
    for combo in combinations:
        coords = {}
        name_parts = []
        
        for axis_tag, value, name in combo:
            coords[axis_tag] = value
            name_parts.append(name)
        
        result.append({
            'coordinates': coords,
            'name': ' '.join(name_parts)
        })
    
    return result

def instantiate_font(font_path, instance, output_dir):
    """Generate a static instance from the variable font."""
    output_filename = instance['name'].replace(' ', '_').replace('=', '_')
    output_filename = ''.join(c for c in output_filename if c.isalnum() or c in '_-').strip('_-')
    output_filename += ".ttf"
    output_path = os.path.join(output_dir, output_filename)
    
    # Load the font
    varfont = TTFont(font_path)
    
    # Instantiate the font with the specified coordinates
    instantiateVariableFont(varfont, instance['coordinates'])
    
    # Set the instance name
    for name_record in varfont['name'].names:
        if name_record.nameID == 1:  # Font Family name
            base_family = name_record.toUnicode()
            if "(" in base_family:  # Remove any existing instance indication
                base_family = base_family.split("(")[0].strip()
            
            # Set a new family name with the instance name
            name_string = f"{base_family} {instance['name']}"
            varfont['name'].setName(name_string, name_record.nameID, 
                                   name_record.platformID, name_record.platEncID,
                                   name_record.langID)
    
    # Save the instantiated font
    varfont.save(output_path)
    return output_path

def main():
    parser = argparse.ArgumentParser(description='Generate all named instances from a variable font\'s STAT table.')
    parser.add_argument('font_path', help='Path to the variable font file')
    parser.add_argument('output_dir', help='Directory to save generated instances')
    
    args = parser.parse_args()
    
    # Check if the font file exists
    if not os.path.isfile(args.font_path):
        print(f"Error: Font file {args.font_path} not found.")
        sys.exit(1)
    
    # Check if the output directory exists, create if it doesn't
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    try:
        # Get named instances from STAT table
        named_values, axes = get_all_named_instances(args.font_path)
        
        if not named_values:
            print("No named instances found in the STAT table.")
            sys.exit(1)
        
        # Generate all combinations
        instances = generate_all_combinations(named_values)
        
        print(f"Found {len(instances)} possible instance combinations.")
        
        # Generate instances
        for i, instance in enumerate(instances):
            print(f"Generating instance {i+1}/{len(instances)}: {instance['name']}")
            output_path = instantiate_font(args.font_path, instance, args.output_dir)
            print(f"  Saved to: {output_path}")
        
        print("\nDone! All instances have been generated.")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
