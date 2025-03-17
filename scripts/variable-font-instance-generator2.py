from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from itertools import product
import os

def generate_static_instances(font_path, output_dir):
    # Load the variable font
    font = TTFont(font_path)
    
    
    # Extract the named instances# Get the axes data (e.g., weight, width, etc.)
    axes = font['fvar'].axes
    axis_names = [axis.axisTag for axis in axes]
    
    named_instances = font['fvar'].instances
    
    # Create a list of the combinations of the named instances for each axis
    instance_combinations = []

    for axis in axis_names:
        # For each axis, find all the instances (min/max, user-defined values)
        instances_for_axis = [instance for instance in named_instances if axis in instance.coords]
        instance_combinations.append(instances_for_axis)
    
    # Generate all possible combinations of the named instances
    all_combinations = product(*instance_combinations)
    
    # Output directory check and creation
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create static fonts for each combination
    for i, combination in enumerate(all_combinations):
        instance_coords = {axis: instance.coords[axis] for axis, instance in zip(axis_names, combination)}
        
        # Instantiate the font for this combination of axis values
        static_font = instancer.instantiateVariableFont(font, instance_coords)
        
        # Save the generated static font
        output_file = os.path.join(output_dir, f"instance_{i+1}.ttf")
        static_font.save(output_file)
        print(f"Saved static instance: {output_file}")

    print(f"Generated {i+1} static instances.")

if __name__ == "_main_":
    font_path = "/home/artim/devel/samaano-fontsSamanoo-VF.ttf"  # Specify the path to your variable font
    output_dir = "output"  # Specify the output directory
    
    generate_static_instances(font_path, output_dir)
