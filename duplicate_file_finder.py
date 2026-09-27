import os
import hashlib
from collections import defaultdict

def find_duplicates(directory):
    hashes = defaultdict(list)
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                    hashes[file_hash].append(filepath)
            except (OSError, IOError):
                continue
    
    duplicates = {h: paths for h, paths in hashes.items() if len(paths) > 1}
    return duplicates

if __name__ == "__main__":
    import sys
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    dupes = find_duplicates(target_dir)
    for h, paths in dupes.items():
        print(f"Duplicate files (hash {h}):")
        for path in paths:
            print(f"  {path}")
