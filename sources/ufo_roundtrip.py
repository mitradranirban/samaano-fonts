#!/usr/bin/env fontforge
import sys
import os
import fontforge

def ufo_to_sfd(ufo_path, sfd_path):
    font = fontforge.open(ufo_path)
    font.save(sfd_path)
    font.close()

def sfd_to_ufo(sfd_path, ufo_out_dir):
    font = fontforge.open(sfd_path)
    font.generate(ufo_out_dir, flags=["round"])
    font.close()

def main():
    if len(sys.argv) < 2:
        print("Usage: fontforge -script ufo_roundtrip.py input.ufo [output_dir]")
        sys.exit(1)
    ufo_src = sys.argv[1]
    sfd_tmp = os.path.splitext(ufo_src)[0] + ".sfd"
    ufo_regen = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(ufo_src)[0] + "_regen.ufo"
    ufo_to_sfd(ufo_src, sfd_tmp)
    sfd_to_ufo(sfd_tmp, ufo_regen)
    print(f"Round-trip complete: {ufo_src} -> {sfd_tmp} -> {ufo_regen}")

if __name__ == "__main__":
    main()

