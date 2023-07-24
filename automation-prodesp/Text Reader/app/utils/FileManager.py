import fitz, os
import pathlib

path = pathlib.Path(__file__).parent.parent.resolve()

class FileManager():
     
    def extract_file_dot_pdf(self):
        with open(f'{path}/texto.txt', 'r', encoding="utf8") as file:
            str_file  = file.read()
            return str_file
        
    def open_pdf_files(self, pdf_bytes):
        text = ''
        # folder_path = f'{path.parent}\\PDFs'
        for filename in pdf_bytes:
            if filename.endswith('.pdf'):
                # file_path = os.pth.join(pdf_bytes, filename)
                doc = fitz.open(pdf_bytes)
                for page in range(doc.page_count)[:1]:
                    page = doc[page]
                    page_text = page.get_text()
                    text += page_text
        return text
    
# fileManager = FileManager()
# text = fileManager.open_pdf_files()
# print(text)a