import PyPDF2
import re

# Open the PDF file
pdf_file = open('test/file.pdf', 'rb')

# Create a PDF reader object
pdf_writer=PyPDF2.PdfWriter()
text='assalomu'

page=pdf_writer.add_blank_page(width=75,height=75)
page.mergePage(pdf_writer.add_)
pdf_writer.write(pdf_file)
pdf_file.close()

