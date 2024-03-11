import os
import hashlib
import time

def calculate_file_hash(filepath, algorithm="sha512"):
    """
    Calculate the hash value of a file.
    """
    hash_func = hashlib.new(algorithm)
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def create_hash_file(directory, hashfile):
    """
    Create a hash file containing hash values of files in a directory.
    """
    with open(hashfile, "w") as f:
        for root, _, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_hash = calculate_file_hash(filepath)
                f.write(f"{filepath}|{file_hash}\n")

def monitor_changes(directory, hashfile):
    """
    Monitor changes in files and notify when new files are created.
    """
    known_hashes = {}
    if os.path.exists(hashfile):
        with open(hashfile, "r") as f:
            for line in f:
                filepath, file_hash = line.strip().split("|")
                known_hashes[filepath] = file_hash

    while True:
        time.sleep(5)  # Check every 5 seconds
        for root, _, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_hash = calculate_file_hash(filepath)
                if filepath not in known_hashes:
                    print(f"New file created: {filepath}")
                    known_hashes[filepath] = file_hash
                    with open(hashfile, "a") as f:
                        f.write(f"{filepath}|{file_hash}\n")

if __name__ == "__main__":
    file= input("Enter the directory to be hashed:")
    directory = file  # Directory to monitor
    hashfile = "./hashfile.txt"  # Path to hash file

    print("Select an option:")
    print("1) New File Baseline")
    print("2) Begin Monitoring")

    option = input("Enter your choice (1 or 2): ")

    if option == "1":
        create_hash_file(directory, hashfile)
        print("New file baseline created successfully.")

    elif option == "2":
        monitor_changes(directory, hashfile)

    else:
        print("Invalid option. Please choose 1 or 2.")
