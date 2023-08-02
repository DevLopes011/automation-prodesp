import fitz
import os
import re
from utils.RegexPattern import PATTERN_NIRES
class FileManager:
    def open_pdf_files(self, directory_path):
        pdf_documents = []
        for filename in os.listdir(directory_path):
            if filename.endswith('.pdf'):
                file_path = os.path.join(directory_path, filename)
                doc = fitz.open(file_path)
                pdf_documents.append(doc)
                
        return pdf_documents

    @staticmethod
    def extrair_nires(texto):
        # Criar o padrão de expressão regular a partir dos PATTERN_NIRES
        padrao_nire = r"\b\d{11}\b"
        nires_encontrados = re.findall(padrao_nire, texto)
        return nires_encontrados
    
    @staticmethod
    def extrair_motivos(texto):
        padrao_motivo = r"N\.\sDA\sALTERACAO:\s(\d{6}/\d{2}-\d)\s-\s(.+?)\s-"
        motivos_encontrados = re.findall(padrao_motivo, texto)
        return motivos_encontrados
    
    @staticmethod
    def extrair_numeros_alteracao(texto):
        padrao_numeros_alteracao = r"N\.\sDA\sALTERACAO:\s(\d{6}/\d{2}-\d)\b"
        numeros_alteracao_encontrados = re.findall(padrao_numeros_alteracao, texto)
        return numeros_alteracao_encontrados