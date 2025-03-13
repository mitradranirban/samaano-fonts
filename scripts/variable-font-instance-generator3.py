from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
import itertools
import os

def create_named_instances(font_path, output_dir="instances"):
    """
    Creates all named instances from a variable font's STAT table in all axis combinations.

    Args:
        font_path (str): Path to the variable font file.
        output_dir (str): Directory to save the instance fonts.
    """

    try:
        font = TTFont(font_path)
    except Exception as e:
        print(f"Error opening font: {e}")
        return

    if "STAT" not in font:
        print("Font does not contain a STAT table.")
        return

    stat_table = font["STAT"]
    axis_values = {}

    for axis_value in stat_table.table.AxisValue:
        axis_tag = stat_table.table.Axis[axis_value.AxisIndex].AxisTag
        value = axis_value.Value
        if axis_tag not in axis_values:
            axis_values[axis_tag] = []
        axis_values[axis_tag].append((value, axis_value))

    if not axis_values:
        print("No named instances found in the STAT table.")
        return

    # Create all possible combinations of axis values
    all_combinations = list(itertools.product(*axis_values.values()))

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for combination in all_combinations:
        instance_dict = {}
        instance_name_parts = []
        for axis_tag, (value, axis_value) in zip(axis_values.keys(), combination):
            instance_dict[axis_tag] = value
            instance_name_parts.append(axis_value.Name.toUnicode())

        instance_name = "-".join(instance_name_parts)
        output_file = os.path.join(output_dir, f"{instance_name}.ttf")

        try:
            instance_font = instancer.instantiateVariableFont(font, instance_dict)
            instance_font.save(output_file)
            print(f"Created instance: {instance_name}")
        except Exception as e:
            print(f"Error creating instance {instance_name}: {e}")
        finally:
            if 'instance_font' in locals():
                instance_font.close()
    font.close()

if __name__ == "__main__":
    font_path = Samaano-VF.ttf
    create_named_instances(font_path)
