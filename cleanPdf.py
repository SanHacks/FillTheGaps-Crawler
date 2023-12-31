import os
import PyPDF2

def contains_text(page, text):
    # Check if the given text is present in the page content
    return text in page.extract_text()

def remove_first_page(input_pdf):
    # Create a temporary file to write the modified content
    temp_pdf = input_pdf + '_temp'

    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        # Add pages from the original PDF (excluding the first page if it contains the specified text)
        first_page = pdf_reader.pages[0]
        if not contains_text(first_page, "You have Downloaded"):
            pdf_writer.add_page(first_page)

        for page_num in range(1, len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        # Write the modified PDF content to the temporary file
        with open(temp_pdf, 'wb') as temp_file:
            pdf_writer.write(temp_file)

    # Replace the original file with the temporary file
    os.replace(temp_pdf, input_pdf)
    print("Removed first page from", input_pdf)

def remove_first_page_all_pdfs(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            input_pdf = os.path.join(folder_path, filename)
            remove_first_page(input_pdf)

if __name__ == "__main__":
    folder_path = "papers"  # Replace with your actual folder path
    remove_first_page_all_pdfs(folder_path)
