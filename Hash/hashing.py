import hashlib
import sys
import os

def calculate_hash(file_path, hash_algorithm):
    hash_obj = hashlib.new(hash_algorithm)
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                hash_obj.update(chunk)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return hash_obj.hexdigest()

def print_usage():
    print("Usage: python hash_calculator.py <file_path> <hash_algorithm>")
    print("Supported hash algorithms: md5, sha1, sha256, sha512")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print_usage()

    input_file_path = sys.argv[1]
    hash_algorithm = sys.argv[2].lower()

    if not os.path.isfile(input_file_path):
        print(f"Error: '{input_file_path}' is not a valid file path.")
        sys.exit(1)

    if hash_algorithm not in ['md5', 'sha1', 'sha256', 'sha512']:
        print("Error: Invalid hash algorithm. Supported algorithms: md5, sha1, sha256, sha512")
        sys.exit(1)

    hash_value = calculate_hash(input_file_path, hash_algorithm)

    print(f"{hash_algorithm.upper()} Hash of '{input_file_path}': {hash_value}")
