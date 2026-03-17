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

def expand_groups_in_line(line, groups):
    """
    Expand group references (e.g., @GroupName or [@GroupName glyphs]) in one mark positioning line
    into multiple lines of individual glyph references.

    Example line:
    pos mark @MarkClass @BaseClass anchor 0 400;

    Could expand to:
    pos mark glyph1 glyph1 anchor 0 400;
    pos mark glyph2 glyph1 anchor 0 400;
    ...
    """
    # Patterns for mark and mark attachment positioning lines to match:
    # 'pos mark leftGlyph rightGlyph anchor X Y;'
    # leftGlyph or rightGlyph can be groups (with @), or bracketed lists

    # Regular expressions for 'pos mark' lines with two glyph or group specs
    pos_mark_pattern = re.compile(r'pos\s+mark\s+(\S+)\s+(\S+)\s+(.*);')

    m = pos_mark_pattern.match(line.strip())
    if not m:
        return [line]  # not a pos mark line

    left, right, rest = m.groups()

    def expand_side(side):
        side = side.strip()
        expanded = []
        if side.startswith('[') and side.endswith(']'):
            # e.g. [@Group glyph1 glyph2]
            inner = side[1:-1].strip().split()
            for el in inner:
                if el.startswith('@'):
                    group_name = el[1:]
                    expanded.extend(groups.get(group_name, [el]))
                else:
                    expanded.append(el)
        else:
            if side.startswith('@'):
                group_name = side[1:]
                expanded.extend(groups.get(group_name, [side]))
            else:
                expanded.append(side)
        return expanded

    left_expanded = expand_side(left)
    right_expanded = expand_side(right)

    expanded_lines = []
    for l in left_expanded:
        for r in right_expanded:
            expanded_lines.append(f'pos mark {l} {r} {rest};')

    return expanded_lines

def break_groups_in_mark_positions(ufo_path, input_fea='features.fea', output_fea='features_expanded_mark.fea'):
    fea_path = os.path.join(ufo_path, 'features', input_fea) if os.path.isdir(os.path.join(ufo_path, 'features')) else os.path.join(ufo_path, input_fea)
    if not os.path.exists(fea_path):
        print(f"Feature file {fea_path} not found.")
        return

    with open(fea_path, encoding='utf-8') as f:
        fea_text = f.read()

    groups = parse_groups(fea_text)
    output_lines = []

    for line in fea_text.splitlines():
        line_strip = line.strip()
        # Handle 'pos mark' lines; expand group references
        if line_strip.startswith('pos mark'):
            expanded = expand_groups_in_line(line_strip, groups)
            output_lines.extend(expanded)
        else:
            # Copy other lines unchanged (including group definitions, etc)
            output_lines.append(line)

    expanded_fea = '\n'.join(output_lines)

    output_path = os.path.join(ufo_path, 'features', output_fea) if os.path.isdir(os.path.join(ufo_path, 'features')) else os.path.join(ufo_path, output_fea)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(expanded_fea)

    print(f"Expanded mark positioning features file written to {output_path}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python break_groups_in_mark_pos.py path/to/font.ufo [input_fea_file] [output_fea_file]")
        sys.exit(1)
    ufo_dir = sys.argv[1]
    input_fea_file = sys.argv[2] if len(sys.argv) > 2 else 'features.fea'
    output_fea_file = sys.argv[3] if len(sys.argv) > 3 else 'features_expanded_mark.fea'

    break_groups_in_mark_positions(ufo_dir, input_fea_file, output_fea_file)
