# merge_images_to_pdf.py

import os
import argparse
from glob import glob
from PIL import Image
from PyPDF2 import PdfMerger

def merge_jpg_to_pdf(directory, output_pdf):
    # Verify if the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Find all JPEG files in the specified directory
    jpg_files = glob(os.path.join(directory, '*.jpg'))
    
    if not jpg_files:
        print(f"No JPEG files found in directory: {directory}")
        return
    
    print(f"Found {len(jpg_files)} JPEG files: {jpg_files}")

    # Convert JPG files to PDF format using Pillow
    pdf_files = []
    for jpg_file in jpg_files:
        image = Image.open(jpg_file)
        pdf_file = jpg_file.replace('.jpg', '.pdf')
        image.convert('RGB').save(pdf_file)
        pdf_files.append(pdf_file)
        print(f"Converted {jpg_file} to {pdf_file}")

    # Merge PDFs into a single PDF using PyPDF2
    merger = PdfMerger()
    for pdf_file in pdf_files:
        merger.append(pdf_file)
        print(f"Appended {pdf_file} to merger")

    # Write out the final combined PDF
    merger.write(output_pdf)
    merger.close()
    print(f"Created merged PDF: {output_pdf}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge JPEG files into a single PDF.")
    parser.add_argument("directory", type=str, help="Directory containing JPEG files")
    parser.add_argument("output_pdf", type=str, help="Output PDF file name")

    args = parser.parse_args()
    merge_jpg_to_pdf(args.directory, args.output_pdf)

