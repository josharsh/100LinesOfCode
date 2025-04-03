# Hash Generator

## Introduction

Hello, guys! Today, we'll be building a hash generator tool in Python. This tool will help you verify the integrity of files by generating hash values using different algorithms.

## Why Do We Need Hashing?

Hashing allows us to create a unique fingerprint (hash) for a file. This fingerprint is like a digital signature, and any change in the file content results in a completely different hash. We use this property to verify the integrity of files, especially when downloading important files like operating systems.

## Supported Hash Algorithms: md5, sha1, sha256, sha512.

## How It Works

1. **Usage**: Run the script from the command line with the file path and hash algorithm as arguments.

   ```bash
   python hash_generator.py <file_path> <hash_algorithm>


Code Explanation
calculate_hash Function
This function takes a file path and a hash algorithm as parameters and returns the hash value of the file using the specified algorithm.

print_usage Function
Prints the correct usage instructions when the script is run with an incorrect number of arguments.

Command-Line Arguments
input_file_path: Path to the file to be hashed.
hash_algorithm: Chosen hash algorithm (md5, sha1, sha256, sha512).
Error Handling
The script checks for errors such as the file not found, an incorrect number of command-line arguments, and an invalid hash algorithm.