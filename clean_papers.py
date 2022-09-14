import os

#for file in os.listdir("."):
 #   if file.endswith(".pdf"):
  #      os.system("pdftk {} cat 1 output {}_first_page.pdf".format(file, os.path.splitext(file)[0]))
        

import pyPdf

def remove_first_page(input_pdf, output_pdf):
    pdf = pyPdf.PdfFileReader(input_pdf)
    pdf_writer = pyPdf.PdfFileWriter()
    for page in range(1, pdf.getNumPages()):
        pdf_writer.addPage(pdf.getPage(page))
    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)

if __name__ == '__main__':
    remove_first_page('input.pdf', 'output.pdf')