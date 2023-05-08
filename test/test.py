import PyPDF2
import re
# Open the PDF file
pdf_file = open('test/file.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF file
num_pages = len(pdf_reader.pages)
pdf_page=pdf_reader.pages[0].extract_text()
# print(re.findall('\d+',pdf_page)[22])
for i in pdf_page.split('STIR'):
    print(i)



# # # Loop through all the pages and extract text
# for i in range(num_pages):
#     # Get the current page object
#     page = pdf_reader.pages[num_pages-1]

#     # Extract the text from the current page
#     text = page.extract_text()

#     # Print the text
#     print(text[550:600])

# # Close the PDF file
# pdf_file.close()
