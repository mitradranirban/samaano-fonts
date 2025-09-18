#! /usr/bin/env python
import fontforge
import sys

def rename_glyphs_to_production(font):
    for glyph in font.glyphs():
        uni = glyph.unicode
        if uni != -1:
            new_name = fontforge.nameFromUnicode(uni)
            if new_name and glyph.glyphname != new_name:
                glyph.glyphname = new_name

def main():
    if len(sys.argv) < 2:
        print("Usage: fontforge -script rename_glyphs.py fontfile.sfd")
        return
    fontfile = sys.argv[1]
    font = fontforge.open(fontfile)
    rename_glyphs_to_production(font)
    new_name = fontfile.rsplit('.', 1)[0] + "-renamed.sfd"
    font.save(new_name)
    font.close()
    print(f"Glyphs renamed and saved to {new_name}")

if __name__ == "__main__":
    main()

