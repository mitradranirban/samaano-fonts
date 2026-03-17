import subprocess
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Merge Adobe feature files sequentially.")
    parser.add_argument("ufo_path", help="Path to the UFO file")
    parser.add_argument("designspace", help="Path to the .designspace file")
    parser.add_argument("output_fea", help="Name of the output .fea file")
    
    args = parser.parse_args()

    # Step 1: break_groups_in_fea.py
    print(f"--- Step 1: Breaking groups in {args.ufo_path} ---")
    subprocess.run([sys.executable, "-m", "feamerge.break_groups_in_fea", args.ufo_path], check=True)

    # Step 2: break_groups_in_mark_pos.py
    print(f"--- Step 2: Breaking mark positioning in {args.ufo_path} ---")
    subprocess.run([sys.executable, "-m", "feamerge.break_groups_in_mark_pos", args.ufo_path], check=True)

    # Step 3: combine_features.py
    print(f"--- Step 3: Combining into {args.output_fea} ---")
    subprocess.run([sys.executable, "-m", "feamerge.combine_features", args.designspace, args.output_fea], check=True)

    print("\nDone! Variable features generated successfully.")
