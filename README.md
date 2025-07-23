# PdfSplitter

A simple Python script to split a PDF file into multiple smaller files based on specified page ranges.

## ✨ Features

*   Splits a PDF into multiple files according to given page ranges.
*   Checks the total number of pages in a PDF file.

## ⚙️ Requirements

*   Python 3.7+
*   `pypdf`

## 🚀 Installation

1.  Clone this repository or download the script.
2.  Install the required dependency using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

## 📖 Usage

Run the script from your command line or terminal.

### 1. Check Total Page Count
To check the total number of pages in a PDF, provide the file path as the only argument.
```bash
python split.py [path_to_your_pdf]
```
**Example:**
```bash
python split.py Test.pdf
```

### 2. Split a PDF File
To split a PDF, provide the file path followed by one or more page ranges, separated by spaces. A page range should be in the format `start-end`. You can use the keyword `end` to specify the last page of the document.

**Example:** To split `Test.pdf` into two files (pages 1-5 and pages 6 to the end):
```bash
python split.py Test.pdf 1-5 6-end
```
> This command will create files like `Test.pdf.1-5.pdf` and `Test.pdf.6-end(end).pdf` in the current directory.
