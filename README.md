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

## How the Script Works

1. **Input Reading**: The script reads all files from the specified input directory (or the current directory if none is specified). Only files with the `.pdf` extension are processed; other files are ignored.
2. **Page Splitting**:
   - For each PDF, it iterates through its pages.
   - Each page is split into two separate pages:
     - The **upper half** of the original page.
     - The **lower half** of the original page.
3. **Output Writing**: The split pages are saved into new PDF files in the specified output directory.
4. **Logging**: Any warnings or errors encountered during the process are logged to the specified file if provided.
5. **Progress Tracking**: The script uses `tqdm` to display a progress bar during the processing.

## Additional Configuration

### Global Execution

To make the script executable globally:

1. **Add a Shebang**: Ensure the script starts with the following line:
   ```python
   #!/usr/bin/env python3
   ```

2. **Make the Script Executable**:
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

### Creating an Alias

For easier execution, you can create an alias:

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
   - Execute the script using the alias:
     ```bash
     splitpdfs [options]
     ```

## Notes and Limitations

- **File Types**: Only files with the `.pdf` extension are processed. Other files in the input directory are ignored without causing errors.
- **Page Orientation**: The splitting assumes standard portrait orientation for pages. Results may vary for landscape-oriented pages.

## License

(C) 2024 Leonardo Russo. All rights reserved.

For more information, visit the project repository: [GitHub - pdf-page-splitter](https://github.com/leonardor1999/pdf-page-splitter).
