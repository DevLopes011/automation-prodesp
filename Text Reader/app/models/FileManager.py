import fitz
import os
import re
from utils.RegexPattern import PATTERN_NIRES, PATTERN_BLOCKS
class FileManager:
    def __init__(self):
        pass
    
    def open_pdf_files(self, directory_path):
        pdf_documents = []
        for filename in os.listdir(directory_path):
            if filename.endswith('.pdf'):
                file_path = os.path.join(directory_path, filename)
                doc = fitz.open(file_path)
                pdf_documents.append(doc)
                
        return pdf_documents
             
    @staticmethod
    def extract_nires(texto):
        padrao_nire = r"\b\d{11}\b"
        nires_encontrados = re.findall(padrao_nire, texto)
        return nires_encontrados

    def parse_text(self, text):
        data_list = []
        
        for line in text:
            if not line.strip():
                continue
            
            regex = r"-\s*(\d+)\s*-\s*N\.\s*DA\s*ALTERACAO:\s*(\d{6}/\d{2})\s*-\s*(.*?)\s*-\s*(.*)\s*-"
            match = re.search(regex, line)
            
            if match:
                nire, num_alteracao, empresa_num, motivo  = match.groups()
                if empresa_num is not None:
                    num_alteracao += f"-{empresa_num}"
                data_dict = {
                    "NIRE": nire.strip(),
                    "N. DA ALTERACAO": num_alteracao.strip(),
                    # "Empresa": empresa.strip(),
                    "Motivo": motivo.strip()
                }
                data_list.append(data_dict)
        
        return data_list