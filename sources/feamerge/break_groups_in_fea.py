import re
import os
import sys

def parse_groups(fea_text):
    """
    Parse group definitions in the feature file which look like:
    @GroupName = [glyph1 glyph2 glyph3];
    Returns a dict: {groupname: [glyphnames]}
    """
    group_pattern = re.compile(r'@(\w+)\s*=\s*\[([^\]]+)\];')
    groups = {}
    for match in group_pattern.finditer(fea_text):
        group_name = match.group(1)
        glyphs_str = match.group(2)
        glyphs = glyphs_str.strip().split()
        groups[group_name] = glyphs
    return groups

def expand_kerning_pairs(fea_text, groups):
    """
    Find kerning pairs using groups and expand them to individual pairs.
    Kerning lines usually look like: pos [@LeftGroup] [@RightGroup] -50;
    or pos [@Group] glyph -50; etc.

    We'll replace all group references (@GroupName) with the actual glyph names.

    Returns rewritten feature text with expanded kerning pairs.
    """
    result_lines = []
    kerning_pattern = re.compile(r'pos\s+(\S+)\s+(\S+)\s+(-?\d+);')

    def expand_side(side):
        # Remove brackets if any
        side = side.strip()
        if side.startswith('[') and side.endswith(']'):
            side = side[1:-1].strip()
            elements = side.split()
            expanded = []
            for el in elements:
                if el.startswith('@'):  # group
                    group_name = el[1:]
                    if group_name in groups:
                        expanded.extend(groups[group_name])
                    else:
                        expanded.append(el)
                else:  # single glyph
                    expanded.append(el)
            return expanded
        else:
            # Could be single group name or glyph name
            if side.startswith('@'):
                group_name = side[1:]
                if group_name in groups:
                    return groups[group_name][:]
                else:
                    return [side]
            else:
                return [side]

    lines = fea_text.splitlines()
    for line in lines:
        line_strip = line.strip()
        if line_strip.startswith('pos '):
            m = kerning_pattern.match(line_strip)
            if m:
                left, right, value = m.groups()
                left_glyphs = expand_side(left)
                right_glyphs = expand_side(right)
                # For all combinations, write separate pos lines
                for lg in left_glyphs:
                    for rg in right_glyphs:
                        result_lines.append(f'pos {lg} {rg} {value};')
            else:
                result_lines.append(line)
        else:
            # Copy group definitions as is to keep them (optional: can skip)
            # Also copy all other lines unchanged
            result_lines.append(line)

    return '\n'.join(result_lines)

def break_groups_in_fea(ufo_path, input_fea='features.fea', output_fea='features_expanded.fea'):
    """
    Read feature file inside UFO, expand groups in kerning pairs,
    and write expanded feature file back.
    """
    fea_path = os.path.join(ufo_path, 'features', input_fea) if os.path.isdir(os.path.join(ufo_path, 'features')) else os.path.join(ufo_path, input_fea)
    if not os.path.exists(fea_path):
        print(f"Feature file {fea_path} not found.")
        return

    with open(fea_path, encoding='utf-8') as f:
        fea_text = f.read()

    groups = parse_groups(fea_text)
    expanded_fea = expand_kerning_pairs(fea_text, groups)

    output_path = os.path.join(ufo_path, 'features', output_fea) if os.path.isdir(os.path.join(ufo_path, 'features')) else os.path.join(ufo_path, output_fea)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(expanded_fea)

    print(f"Expanded features file written to {output_path}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python break_groups_in_fea.py path/to/font.ufo [input_fea_file] [output_fea_file]")
        sys.exit(1)
    ufo_dir = sys.argv[1]
    input_fea_file = sys.argv[2] if len(sys.argv) > 2 else 'features.fea'
    output_fea_file = sys.argv[3] if len(sys.argv) > 3 else 'features_expanded.fea'

    break_groups_in_fea(ufo_dir, input_fea_file, output_fea_file)
