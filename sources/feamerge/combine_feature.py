#!/usr/bin/env python3
"""
Enhanced script to combine feature.fea files from UFOs referenced in a designspace
into a single variable features.fea file with proper variable font syntax.
Includes support for variable mark positioning anchors.
"""

import os
import re
from fontTools.designspaceLib import DesignSpaceDocument
from ufoLib2 import Font
from collections import defaultdict, OrderedDict


class VariableFeatureCombiner:
    def __init__(self, designspace_path):
        self.designspace_path = designspace_path
        self.designspace = DesignSpaceDocument.fromfile(designspace_path)
        self.masters_data = {}
        self.combined_classes = {}
        self.kern_pairs = defaultdict(dict)
        self.mark_classes = defaultdict(dict)
        self.mark_bases = defaultdict(dict)
        self.lookups = defaultdict(dict)
        self.axis_mappings = {}
        
        # Extract axis information
        for axis in self.designspace.axes:
            self.axis_mappings[axis.tag] = {
                'name': axis.name,
                'min': axis.minimum,
                'default': axis.default,
                'max': axis.maximum
            }
    
    def load_ufo_features(self):
        """Load feature.fea content from all UFO masters"""
        for source in self.designspace.sources:
            if source.path:
                ufo_path = source.path
            elif source.filename:
                designspace_dir = os.path.dirname(self.designspace_path)
                ufo_path = os.path.normpath(os.path.join(designspace_dir, source.filename))
            else:
                continue
            
            if not os.path.exists(ufo_path):
                print(f"Warning: UFO not found at {ufo_path}")
                continue
            
            try:
                font = Font.open(ufo_path)
                features_content = font.features.text if font.features.text else ""
                
                location = source.location or {}
                master_key = source.filename or os.path.basename(source.path)
                
                self.masters_data[master_key] = {
                    'location': location,
                    'features': features_content,
                    'font': font
                }
                
            except Exception as e:
                print(f"Error loading UFO {ufo_path}: {e}")
    
    def parse_glyph_classes(self, features_text):
        """Extract glyph class definitions from feature text"""
        classes = {}
        class_pattern = r'@([a-zA-Z0-9_.]+)\s*=\s*\[(.*?)\];'
        
        for match in re.finditer(class_pattern, features_text, re.DOTALL):
            class_name = match.group(1)
            glyph_content = match.group(2).strip()
            if '\\' in glyph_content:
                glyph_list = [g.strip() for g in glyph_content.split() if g.strip()]
            else:
                glyph_list = [g.strip() for g in glyph_content.split() if g.strip()]
            classes[class_name] = glyph_list
        
        return classes
    
    def extract_positioning_data(self, features_text, master_key):
        """Extract positioning data from lookups including kern and mark"""
        location = self.masters_data[master_key]['location']
        
        # Extract kern positioning
        kern_pattern = r'pos\s+\\([A-Za-z0-9_]+)\s+\\([A-Za-z0-9_]+)\s+(-?\d+);'
        for match in re.finditer(kern_pattern, features_text):
            left_glyph = match.group(1)
            right_glyph = match.group(2)
            value = int(match.group(3))
            
            pair_key = f"{left_glyph} {right_glyph}"
            self.kern_pairs[pair_key][master_key] = {
                'value': value,
                'location': location
            }
    
    def extract_mark_anchors(self, features_text, master_key):
        """Extract mark anchor data from lookup blocks"""
        location = self.masters_data[master_key]['location']
        
        # Find lookup blocks
        lookup_pattern = r'lookup\s+(\w+)\s*\{(.*?)\}\s*\1;'
        
        for lookup_match in re.finditer(lookup_pattern, features_text, re.DOTALL):
            lookup_name = lookup_match.group(1)
            lookup_content = lookup_match.group(2)
            
            # Extract markClass statements
            markclass_pattern = r'markClass\s+\[(.*?)\]\s+<anchor\s+(-?\d+)\s+(-?\d+)\s*>\s+@(\w+);'
            for mark_match in re.finditer(markclass_pattern, lookup_content):
                glyphs = mark_match.group(1).strip()
                x_coord = int(mark_match.group(2))
                y_coord = int(mark_match.group(3))
                mark_class = mark_match.group(4)
                
                markclass_key = f"{glyphs}@{mark_class}"
                if markclass_key not in self.mark_classes:
                    self.mark_classes[markclass_key] = {}
                
                self.mark_classes[markclass_key][master_key] = {
                    'x': x_coord,
                    'y': y_coord,
                    'location': location,
                    'glyphs': glyphs,
                    'mark_class': mark_class,
                    'lookup_name': lookup_name
                }
            
            # Extract pos base statements
            posbase_pattern = r'pos\s+base\s+\[(.*?)\]\s+<anchor\s+(-?\d+)\s+(-?\d+)\s*>\s+mark\s+@(\w+);'
            for base_match in re.finditer(posbase_pattern, lookup_content):
                glyphs = base_match.group(1).strip()
                x_coord = int(base_match.group(2))
                y_coord = int(base_match.group(3))
                mark_class = base_match.group(4)
                
                base_key = f"{glyphs}@{mark_class}"
                if base_key not in self.mark_bases:
                    self.mark_bases[base_key] = {}
                
                self.mark_bases[base_key][master_key] = {
                    'x': x_coord,
                    'y': y_coord,
                    'location': location,
                    'glyphs': glyphs,
                    'mark_class': mark_class,
                    'lookup_name': lookup_name
                }
    
    def merge_classes(self):
        """Merge glyph classes from all masters"""
        all_classes = defaultdict(set)
        
        for master_name, master_data in self.masters_data.items():
            classes = self.parse_glyph_classes(master_data['features'])
            for class_name, glyphs in classes.items():
                all_classes[class_name].update(glyphs)
        
        self.combined_classes = {
            name: sorted(list(glyphs)) 
            for name, glyphs in all_classes.items()
        }
    
    def format_variable_positioning(self, master_data):
        """Format positioning values with variable font coordinate syntax"""
        if not master_data:
            return "0"
        
        coordinate_values = []
        for master_key, data in master_data.items():
            location = data['location']
            value = data['value']
            
            coords = []
            for axis_tag, axis_value in location.items():
                coords.append(f"{axis_tag}={axis_value}")
            
            if coords:
                coord_str = ",".join(coords)
                coordinate_values.append(f"{coord_str}:{value}")
            else:
                coordinate_values.append(f":{value}")
        
        return " ".join(coordinate_values) if coordinate_values else "0"
    
    def format_variable_anchor(self, master_data):
        """Format anchor coordinates with variable font coordinate syntax"""
        if not master_data:
            return "<anchor 0 0>"
        
        x_coordinates = []
        y_coordinates = []
        
        for master_key, data in master_data.items():
            location = data['location']
            x_coord = data['x']
            y_coord = data['y']
            
            coords = []
            for axis_tag, axis_value in location.items():
                coords.append(f"{axis_tag}={axis_value}")
            
            if coords:
                coord_str = ",".join(coords)
                x_coordinates.append(f"{coord_str}:{x_coord}")
                y_coordinates.append(f"{coord_str}:{y_coord}")
            else:
                x_coordinates.append(f":{x_coord}")
                y_coordinates.append(f":{y_coord}")
        
        x_values = " ".join(x_coordinates) if x_coordinates else "0"
        y_values = " ".join(y_coordinates) if y_coordinates else "0"
        
        return f"<anchor {x_values} {y_values}>"
    
    def generate_variable_features(self):
        """Generate the complete variable features.fea content"""
        output_lines = []
        
        # Add header
        output_lines.extend([
            "languagesystem DFLT dflt;",
            "languagesystem latn dflt;",
            "",
            "# Variable features.fea generated from designspace masters",
            ""
        ])
        
        # Add glyph class definitions
        if self.combined_classes:
            for class_name, glyphs in self.combined_classes.items():
                if glyphs:
                    glyph_list = " ".join([f"\\{g}" if not g.startswith('\\') else g for g in glyphs])
                    output_lines.append(f"@{class_name} = [{glyph_list}];")
            output_lines.append("")
        
        # Generate kern feature with variable syntax
        if self.kern_pairs:
            output_lines.append("feature kern {")
            
            for pair_key, master_data in self.kern_pairs.items():
                variable_value = self.format_variable_positioning(master_data)
                if variable_value != "0":
                    left, right = pair_key.split(' ', 1)
                    output_lines.append(f"    pos \\{left} \\{right} ({variable_value});")
            
            output_lines.extend(["} kern;", ""])
        
        # Generate mark feature with variable anchor syntax
        if self.mark_classes or self.mark_bases:
            # Get lookup name from the first mark class or base
            lookup_name = "markMarkPositioninginLatinlookup2"
            if self.mark_classes:
                first_markclass = next(iter(self.mark_classes.values()))
                if first_markclass:
                    lookup_name = next(iter(first_markclass.values()))['lookup_name']
            elif self.mark_bases:
                first_base = next(iter(self.mark_bases.values()))
                if first_base:
                    lookup_name = next(iter(first_base.values()))['lookup_name']
            
            output_lines.append(f"lookup {lookup_name} {{")
            output_lines.append("  lookupflag 0;")
            
            # Add markClass statements
            for markclass_key, master_data in self.mark_classes.items():
                if master_data:
                    sample_data = next(iter(master_data.values()))
                    glyphs = sample_data['glyphs']
                    mark_class = sample_data['mark_class']
                    variable_anchor = self.format_variable_anchor(master_data)
                    
                    output_lines.append(f"  markClass [\\{glyphs} ] {variable_anchor} @{mark_class};")
            
            # Add pos base statements
            for base_key, master_data in self.mark_bases.items():
                if master_data:
                    sample_data = next(iter(master_data.values()))
                    glyphs = sample_data['glyphs']
                    mark_class = sample_data['mark_class']
                    variable_anchor = self.format_variable_anchor(master_data)
                    
                    output_lines.append(f"  pos base [\\{glyphs} ] {variable_anchor} mark @{mark_class};")
            
            output_lines.extend([f"}} {lookup_name};", ""])
            
            # Add feature mark block
            output_lines.extend([
                "feature mark {",
                "    script DFLT;",
                "    language dflt ;",
                f"    lookup {lookup_name};",
                "    script latn;", 
                "    language dflt ;",
                f"    lookup {lookup_name};",
                "} mark;",
                ""
            ])
        
        # Add GDEF table
        sample_features = next(iter(self.masters_data.values()))['features']
        gdef_pattern = r'(table GDEF \{.*?\} GDEF;)'
        gdef_match = re.search(gdef_pattern, sample_features, re.DOTALL)
        if gdef_match:
            output_lines.extend([gdef_match.group(1), ""])
        
        return "\n".join(output_lines)
    
    def save_combined_features(self, output_path):
        """Save the combined variable features.fea file"""
        self.load_ufo_features()
        self.merge_classes()
        
        # Extract positioning data from all masters
        for master_key, master_data in self.masters_data.items():
            self.extract_positioning_data(master_data['features'], master_key)
            self.extract_mark_anchors(master_data['features'], master_key)
        
        variable_features_content = self.generate_variable_features()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(variable_features_content)
        
        print(f"Variable features.fea saved to: {output_path}")
        print(f"Masters processed: {len(self.masters_data)}")
        print(f"Kern pairs found: {len(self.kern_pairs)}")
        print(f"Mark classes found: {len(self.mark_classes)}")
        print(f"Mark bases found: {len(self.mark_bases)}")
        print(f"Classes combined: {len(self.combined_classes)}")


def main():
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python combine_features.py <designspace_file> <output_features.fea>")
        return
    
    designspace_path = sys.argv[1]
    output_path = sys.argv[2]
    
    if not os.path.exists(designspace_path):
        print(f"Error: Designspace file not found: {designspace_path}")
        return
    
    try:
        combiner = VariableFeatureCombiner(designspace_path)
        combiner.save_combined_features(output_path)
        print("✓ Successfully generated variable features file with mark support")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
