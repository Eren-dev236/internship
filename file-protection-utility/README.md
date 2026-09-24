# File Protection Utility

A Python-based utility that converts file content into a protected encoded format and allows the original content to be restored when required.

## Features

* Protects file content using Base64 encoding
* Restores protected files to their original content
* Checks whether the specified file exists
* Creates a `.protected` version of the original file
* Handles invalid protected content gracefully
* Simple command-line interface

## Technologies Used

* Python
* Base64
* OS module

## How It Works

The program provides two options:

### 1. Protect a File

The selected file is read in binary mode and its contents are converted using Base64 encoding.

A new file with the `.protected` extension is created.

Example:

```text
sample.txt
↓
sample.txt.protected
```

### 2. Restore a File

The `.protected` file is decoded using Base64 and the original file content is restored.

Example:

```text
sample.txt.protected
↓
sample.txt
```

## How to Run

Open the terminal inside the project folder and run:

```bash
python file_protection.py
```

Choose:

```text
1. Protect a file
2. Restore a file
```

Then enter the file name when prompted.

## Example

### Protecting a File

```text
=== File Protection Utility ===
1. Protect a file
2. Restore a file
Enter your choice (1/2): 1
Enter the file name: sample.txt
File protected successfully: sample.txt.protected
```

### Restoring a File

```text
=== File Protection Utility ===
1. Protect a file
2. Restore a file
Enter your choice (1/2): 2
Enter the file name: sample.txt.protected
File restored successfully: sample.txt
```

## Project Structure

```text
file-protection-utility/
│
├── file_protection.py
└── README.md
```

## Note

This project uses Base64 encoding to demonstrate data transformation and restoration. Base64 is **not encryption** and should not be considered a secure method for protecting sensitive information in real-world applications.
