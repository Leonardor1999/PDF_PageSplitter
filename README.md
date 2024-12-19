
# PDF Page Splitter Script

This Python script uses the `pypdf` library to split each page of a PDF document into two. This is particularly useful for working with scanned or double-sided PDFs that you want to separate into individual pages.

## Prerequisites

Before running the script, ensure you have Python 3.6+ installed on your system. Additionally, you will need to install `pypdf`.

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/Leonardor1999/PDF_PageSplitter.git
cd PDF_PageSplitter
```

### 2. Create a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate # venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install pypdf
```

## Usage

### 1. Prepare your PDF file

Place the PDF files you want to split in the same directory as the script.

### 2. Run the script

Once the setup is complete, you can run the script using the following command:

```bash
python3 split_pdf_pages_in_half.py
```

### 3. Output

The script will create a new directory called `output/` where the split pages will be saved. Each page will be divided into two, and the resulting files will have the same name as the originals.

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details.
