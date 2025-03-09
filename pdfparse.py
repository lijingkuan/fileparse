# -*- coding: utf-8 -*-
import PyPDF2


def extract_text_from_pdf(pdf_path):
    # open pdf file
    with open(pdf_path, 'rb') as file:
        # create a pdfreader object
        reader = PyPDF2.PdfReader(file)
        # obtain the total page of the PDF file
        num_pages = len(reader.pages)
        text = ""

        # extract text from every page
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()

    return text


def write_text_to_file(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)


# variables
pdf_path = 'CV-JingkuanLi.pdf'  # pdf path to read
output_txt_path = 'output.txt'  # text file to write

# extract text content from pdf
extracted_text = extract_text_from_pdf(pdf_path)

# write text content to file
write_text_to_file(extracted_text, output_txt_path)

print(f"Text extracted from {pdf_path} and written to {output_txt_path}")
