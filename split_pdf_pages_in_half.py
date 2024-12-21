#!/usr/bin/env python3

import os
import logging
from pypdf import PdfReader, PdfWriter, PageObject
import argparse
from tqdm import tqdm

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Splits each page of PDF files into two separate pages: one for the upper half and one for the lower half. "
                    "Processes all PDF files in the specified directory (or the current directory by default). "
                    "Other file types are ignored. The resulting files are saved in the output directory.",
        usage="split_pdf_pages_in_half.py [-h] [-q | -v] [-i INPUT] [-o OUTPUT] [-l LOG]",
        add_help=False,
        epilog="(C) 2024 - Leonardo Russo"
    )


    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument("-q", "--quiet", action="store_true",
                                 help="Suppress all output messages during execution.")
    verbosity_group.add_argument("-v", "--verbosity", action="count", default=0,
                                 help="Increase output verbosity. Use multiple '-v' for greater detail.")
    
    parser.add_argument("-i", "--input", type=str, help="Directory containing the PDF files to be processed. Defaults to the current directory.")
    parser.add_argument("-o", "--output", type=str, help="Directory where the split PDF files will be saved. Defaults to a folder named 'output' in the current directory.")
    parser.add_argument("-l", "--log", type=str, help="Path to the file where warnings and errors will be logged. If not provided, no logging will occur.")
    parser.add_argument("-h", "--help", action="help", help="Show this help message and exit.")

    args = parser.parse_args()

    current_directory = os.getcwd()
    pdfs_directory = args.input if args.input else current_directory
    output_directory = args.output if args.output else os.path.join(current_directory, "output")

    os.makedirs(output_directory, exist_ok=True)
    
    pdf_files = [f for f in os.listdir(pdfs_directory) if f.endswith(".pdf")]

    if args.log:
        log_file = args.log
        logging.basicConfig(filename=log_file, level=logging.WARNING, filemode='w')
    else:
        logging.basicConfig(handlers=[logging.NullHandler()])

    for pdf_file in tqdm(pdf_files, desc="Processing PDF files", unit="file", dynamic_ncols=True, disable=args.quiet):
        input_path = os.path.join(pdfs_directory, pdf_file)
        output_path = os.path.join(output_directory, pdf_file)

        try:
            reader = PdfReader(input_path)
            writer = PdfWriter()

            for page in reader.pages:
                media_box = page.mediabox

                upper_half = PageObject.create_blank_page(width=media_box.width, height=(media_box.height / 2))
                upper_half.merge_page(page)
                upper_half.mediabox.upper_right = (media_box.right, media_box.top)
                upper_half.mediabox.lower_left = (media_box.left, media_box.top - (media_box.height / 2))

                lower_half = PageObject.create_blank_page(width=media_box.width, height=(media_box.height / 2))
                lower_half.merge_page(page)
                lower_half.mediabox.upper_right = (media_box.right, media_box.top - (media_box.height / 2))
                lower_half.mediabox.lower_left = (media_box.left, media_box.bottom)


                writer.add_page(upper_half)
                writer.add_page(lower_half)

            with open(output_path, "wb") as output_file:
                writer.write(output_file)

            if args.verbosity > 0:
                print(f"\nProcessed file: {pdf_file} -> {output_path}")
        except Exception as e:
            if args.log:
                logging.warning(f"Error processing {pdf_file}: {e}")

    if not args.quiet:
        print("Processing completed for all PDF files in the folder. Split files are saved in the 'output' directory.")
    
    if args.log:
        print(f"Any warnings have been saved to '{log_file}'.")