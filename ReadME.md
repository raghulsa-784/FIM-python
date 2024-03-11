# File Integrity Management Script

This Python script allows you to manage file integrity by calculating hash values of files in a specified directory and monitoring for changes.

## Features

- **New File Baseline:** Option to create a new baseline of file hash values.
- **Monitoring:** Option to continuously monitor specified files for changes and notify when new files are created.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Wicked2468/FIM-python.git
    cd FIM-python
    ```

2. Install dependencies (if required):

    This script does not require any external dependencies beyond the Python standard library.

3. Run the script:

    ```bash
    python fim.py
    ```

4. Select an option:
   - **Option 1:** Create a new file baseline by calculating hash values of files in the specified directory.
   - **Option 2:** Begin monitoring the specified directory for changes and get notified when new files are created.

## Configuration

- Modify the `directory` variable in the script to specify the directory to monitor.
- Modify the `hashfile` variable to specify the path to the hash file.

## Dependencies

- This script relies only on the Python standard library, so no additional dependencies are needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script was created for educational purposes and can be further enhanced based on specific requirements.
