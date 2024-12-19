import os
import logging
from pypdf import PdfReader, PdfWriter, PageObject

log_file = "pypdf_warnings.log"
logging.basicConfig(filename=log_file, level=logging.WARNING, filemode='w')

pdfs_directory = os.path.dirname(os.path.abspath(__file__))
output_directory = os.path.join(pdfs_directory, "output")

os.makedirs(output_directory, exist_ok=True)

if __name__ == "__main__":
    pdf_files = (f for f in os.listdir(pdfs_directory) if f.endswith(".pdf"))

    for pdf_file in pdf_files:
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

            print(f"Processed file: {pdf_file} -> {output_path}")
        except Exception as e:
            logging.warning(f"Error processing {pdf_file}: {e}")

print("Processing completed for all PDF files in the folder. Split files are saved in the 'output' folder.")
print(f"Any warnings have been saved to '{log_file}'.")