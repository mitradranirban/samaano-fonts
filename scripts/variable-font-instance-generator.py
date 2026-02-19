#!/usr/bin/env python3
from fontTools import ttLib
from fontTools.varLib import mutator

# Load your variable font
var_font = ttLib.TTFont("../sources/Samaano-VF.ttf")

# Iterate through all named instances
for instance in var_font["fvar"].instances:
    instance_name = instance.nameID
    # Create a static font for each instance
    static_font = mutator.instantiateVariableFont(var_font, { "wght": instance.coordinates[0] })
    static_font.save(f"Samaano_{instance_name}.ttf")


if __name__ == "__main__":
    main()
