# PDF-Merger

This Python script allows you to merge multiple PDF files into a single PDF file. The script uses the `PyPDF2` library to handle PDF manipulation.

## Requirements

* Python 3.x
* `PyPDF2` library

You can install the required library using pip:

```bash
pip install PyPDF2
```

# PDF Merger Script

This repository contains a Python script designed to merge multiple PDF files into a single document.

## Script Explanation

### `merge_pdfs` Function

This function takes two arguments:

* `input_pdfs`: A list of paths to the input PDF files to be merged.
* `output_pdf`: The path where the merged PDF file will be saved.

The function performs the following steps:

1.  **Creates a `PdfWriter` object.** This object will collect all the pages from the input PDFs.
2.  **Iterates over each input PDF file:**
    * Opens the PDF file.
    * Reads the PDF file using a `PdfReader` object.
    * Adds each page of the PDF to the `PdfWriter` object.
    * Closes the PDF file.
3.  **Writes the combined pages to the output PDF file.**
