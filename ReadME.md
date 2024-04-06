# File Hashing and Monitoring Utility

This utility provides functionalities to hash files in a directory and monitor changes within that directory.

## Functionality

### 1. Calculate File Hash
- `calculate_file_hash(filepath, algorithm="sha512")`: Calculates the hash value of a file using the specified algorithm.

### 2. Create Hash File
- `create_hash_file(directory, hashfile, algorithm="sha512")`: Creates a hash file containing hash values of files in a directory.

### 3. Monitor Changes
- `monitor_changes(directory, hashfile, algorithm="sha512", interval=5)`: Monitors changes in files and notifies when new files are created or existing ones are modified.

## How to Use

### Command-line Arguments

- `directory`: Directory to be hashed.
- `--hashfile`: Path to the hash file. (Default: "./hashfile.txt")
- `--algorithm`: Hash algorithm to use. (Default: "sha512")
- `--interval`: Monitoring interval in seconds. (Default: 5)
- `--mode`: Operation mode. Choices: "baseline" or "monitor". (Required)

### Operation Modes

1. **Baseline Mode**: Creates a baseline hash file.
   ```bash
   python fim.py <directory> --mode baseline [--hashfile <hashfile>] [--algorithm <algorithm>]

2. **Monitor Mode**: Monitors changes in the directory.
    python fim.py <directory> --mode monitor [--hashfile <hashfile>] [--algorithm <algorithm>] [--interval <interval>]

## Examples

1. **Create Baseline hashfile**
    python fim.py /path/to/directory --mode baseline

2. **Monitor changes in a directory**
    python fim.py /path/to/directory --mode monitor

## Error Handling
    Errors encountered during file hashing, file writing, or reading hash files are logged with details.

## Dependencies
    The utility requires the os, hashlib, time, logging, argparse, and datetime modules, which are part of Python's standard library.

## Notes
    For monitoring mode, it continuously runs in the background until manually terminated.
    The utility supports various hash algorithms, with SHA-512 being the default.
    This utility provides a convenient way to maintain the integrity of files within a directory by monitoring any changes made to them.

