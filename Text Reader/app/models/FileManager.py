import fitz, os, re
#import pathlib
import boto3
from dotenv import load_dotenv
from utils.RegexPattern import PATTERN
class FileManager():
     
    def __init__(self):
        load_dotenv()
        
        self.aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
        self.s3_region_name = os.environ.get("S3_REGION_NAME")
        self.bucket_name_input = os.environ.get("BUCKET_NAME_INPUT")
          
     
     #ENCONTRAR E CONSEGUIR LER
     
     
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
    
    def extract_text_from_pdf(self, pdf_path):
        doc = fitz.open(pdf_path)
        text = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text += page.get_text()
        doc.close()
        return text

    
    def s3_bucket(self):
        s3_resource = boto3.resource('s3', aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key, region_name=self.s3_region_name)
        bucket = s3_resource.Bucket(self.bucket_name_input)
        
        for obj in bucket.objects.all():
            if obj.key.endswith('.pdf'):
                # Fazer o download do PDF para um arquivo local temporário
                local_temp_file = f"/tmp/{os.path.basename(obj.key)}"
                bucket.download_file(obj.key, local_temp_file)

                # Extrair texto do PDF
                extracted_text = self.extract_text_from_pdf(local_temp_file)

                # Aplicar regex para obter texto relevante
                relevant_text = re.findall(PATTERN, extracted_text)

                # Concatenar texto relevante para salvar no S3
                relevant_text = "\n".join(relevant_text)

                # Salvar o texto relevante no S3 com o mesmo nome do arquivo PDF
                output_key = obj.key.replace('.pdf', '.txt')
                save_text_to_s3(relevant_text, output_key)

                # Remover o arquivo temporário local
                os.remove(local_temp_file)

# fileManager = FileManager()
# text = fileManager.open_pdf_files()
# print(text)a