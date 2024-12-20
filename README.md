# PDF Page Splitter

This repository contains a Python script for splitting each page of a PDF into two pages: one for the upper half and one for the lower half.

## Features

- **Batch Processing**: Automatically process all PDF files in a specified directory.
- **Customizable Directories**: Specify input and output directories for flexibility.
- **Logging**: Log warnings and errors to a specified file.
- **Verbosity Control**: Adjust the level of output verbosity for better control.
- **Compatibility**: Works with Python 3.6 and later versions.

## Requirements

- Python 3.6 or higher
- `pypdf` package
- `tqdm` package

Install the required packages:
```bash
pip install pypdf tqdm
```

## Usage

Run the script using the command line:
```bash
python split_pdf_pages_in_half.py [options]
```

### Options:
- `-i`, `--input`: Directory containing PDF files to split. Defaults to the current directory.
- `-o`, `--output`: Directory where split PDF files will be saved. Defaults to a folder named `output` in the current directory.
- `-l`, `--log`: File to save warnings and errors. Defaults to no logging if not specified.
- `-q`, `--quiet`: Suppress output messages.
- `-v`, `--verbosity`: Increase output verbosity. Use multiple `-v` for higher verbosity levels.

### Example Command

```bash
python split_pdf_pages_in_half.py -i ./pdfs -o ./output -l ./warnings.log -v
```

This command will process all PDFs in the `./pdfs` directory, save the split PDFs to the `./output` directory, and log warnings to `./warnings.log` with verbosity enabled.

## Making the Script Executable Globally

To make the script executable from any directory, follow these steps:

1. **Add a Shebang**: Ensure the script starts with the following line:
   ```python
   #!/usr/bin/env python3
   ```

2. **Make the Script Executable**: Run the following command:
   ```bash
   chmod +x split_pdf_pages_in_half.py
   ```

3. **Move the Script to a Directory in `PATH`**:
   - Create a directory for your custom scripts if it doesn’t exist:
     ```bash
     mkdir -p ~/scripts
     ```
   - Move the script to this directory:
     ```bash
     mv split_pdf_pages_in_half.py ~/scripts/
     ```

4. **Update the `PATH` Environment Variable**:
   - Open your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`) and add the following line:
     ```bash
     export PATH="$HOME/scripts:$PATH"
     ```
   - Apply the changes:
     ```bash
     source ~/.bashrc
     ```

Now, you can execute the script from any directory by typing:
```bash
split_pdf_pages_in_half.py [options]
```

## Creating an Alias for Easier Execution

To simplify execution, you can create an alias for the script:

1. **Add an Alias**:
   - Open your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`) and add the following line:
     ```bash
     alias splitpdfs="~/scripts/split_pdf_pages_in_half.py"
     ```

2. **Apply the Changes**:
   - Save the file and reload the shell configuration:
     ```bash
     source ~/.bashrc
     ```

3. **Use the Alias**:
   - Now you can execute the script using the alias:
     ```bash
     splitpdfs [options]
     ```

## How It Works

1. Reads PDF files from the input directory.
2. Splits each page into two pages:
   - Upper half
   - Lower half
3. Saves the resulting PDF to the output directory.
4. Logs any warnings or errors encountered during processing.

## License

(C) 2024 Leonardo Russo. All rights reserved.

For more information, visit the project repository: [GitHub - PDF Page Splitter](https://github.com/Leonardor1999/PDF_PageSplitter)
