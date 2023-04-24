# This Code was Provided by ChatGPT

import os
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger, PdfReader

# Create a file dialog for selecting multiple PDF files
root = tk.Tk()
root.withdraw()

file_paths = filedialog.askopenfilenames(
    filetypes=[("PDF files", "*.pdf")],
    title="Select PDF files to concatenate"
)

if not file_paths:
    print("No files selected. Exiting...")
    exit()

# Merge the selected PDF files
merger = PdfMerger()

for file_path in file_paths:
    with open(file_path, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        merger.append(pdf_reader)

# Save the merged PDF to a new file
output_file = "merged_output.pdf"
with open(output_file, "wb") as output_pdf:
    merger.write(output_pdf)

print(f"Merged PDF files saved as '{output_file}'.")
