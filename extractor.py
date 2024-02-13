# Importar módulo Aspose.Words for Python
import aspose.words as aw

# Cargar archivo PDF
pdf = aw.Document("90_91.pdf")

# Extrae y guarda texto en un archivo TXT
pdf.save("extracted-text.txt")


'''
import fitz  # PyMuPDF

with fitz.open('90_91.pdf') as pdf_doc:
    text = ''
    for page_num in range(pdf_doc.page_count):
        page = pdf_doc[page_num]
        print(pdf_doc[page_num])
        print(page.get_text())
        text += page.get_text()

    print(text)

'''



'''
import pdfplumber

with pdfplumber.open('90_91.pdf') as pdf:
    text = ''
    for page in pdf.pages:
        aux = page.extract_text()
        text += aux

    print(text)
'''


'''
import PyPDF2

with open('90_91.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ''
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()

    print(text)
'''


'''
import fitz  # Esta es la librería pymupdf que habéis instalado
import re
import pandas
with fitz.open("90_91.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()
text = text.replace('�','')
print(text)
'''


'''
import pdfminer

texto = pdfminer.extract_text("90_91.pdf")

print(texto)
'''