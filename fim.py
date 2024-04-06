import os
import hashlib
import time
import logging
import argparse
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_file_hash(filepath, algorithm="sha512"):
    """
    Calculate the hash value of a file using the specified algorithm.
    """
    hash_func = hashlib.new(algorithm)
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
    except Exception as e:
        logging.error(f"Error calculating hash for {filepath}: {e}")
        return None
    return hash_func.hexdigest()

def create_hash_file(directory, hashfile, algorithm="sha512"):
    """
    Create a hash file containing hash values of files in a directory.
    """
    try:
        with open(hashfile, "w") as f:
            for root, _, files in os.walk(directory):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    file_hash = calculate_file_hash(filepath, algorithm)
                    if file_hash:
                        f.write(f"{filepath}|{file_hash}|{os.path.getmtime(filepath)}\n")
    except Exception as e:
        logging.error(f"Error creating hash file: {e}")

def monitor_changes(directory, hashfile, algorithm="sha512", interval=5):
    """
    Monitor changes in files and notify when new files are created.
    """
    known_hashes = {}
    try:
        if os.path.exists(hashfile):
            with open(hashfile, "r") as f:
                for line in f:
                    filepath, file_hash, last_modified = line.strip().split("|")
                    known_hashes[filepath] = (file_hash, float(last_modified))
    except Exception as e:
        logging.error(f"Error reading hash file: {e}")

    while True:
        time.sleep(interval)
        for root, _, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_hash = calculate_file_hash(filepath, algorithm)
                if file_hash and filepath not in known_hashes:
                    logging.info(f"New file created: {filepath}")
                    known_hashes[filepath] = (file_hash, os.path.getmtime(filepath))
                    try:
                        with open(hashfile, "a") as f:
                            f.write(f"{filepath}|{file_hash}|{os.path.getmtime(filepath)}\n")
                    except Exception as e:
                        logging.error(f"Error writing to hash file: {e}")
                elif file_hash and known_hashes[filepath][0] != file_hash:
                    logging.info(f"File modified: {filepath}")
                    known_hashes[filepath] = (file_hash, os.path.getmtime(filepath))
                    try:
                        with open(hashfile, "a") as f:
                            f.write(f"{filepath}|{file_hash}|{os.path.getmtime(filepath)}\n")
                    except Exception as e:
                        logging.error(f"Error writing to hash file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Hashing and Monitoring Utility")
    parser.add_argument("directory", help="Directory to be hashed")
    parser.add_argument("--hashfile", default="./hashfile.txt", help="Path to hash file")
    parser.add_argument("--algorithm", default="sha512", help="Hash algorithm to use")
    parser.add_argument("--interval", type=int, default=5, help="Monitoring interval in seconds")
    parser.add_argument("--mode", choices=["baseline", "monitor"], required=True, help="Operation mode")
    args = parser.parse_args()

    if args.mode == "baseline":
        create_hash_file(args.directory, args.hashfile, args.algorithm)
        logging.info("New file baseline created successfully.")
    elif args.mode == "monitor":
        monitor_changes(args.directory, args.hashfile, args.algorithm, args.interval)