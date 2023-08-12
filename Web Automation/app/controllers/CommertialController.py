from models.GetLinkDriver import GetLinkDriver
from models.Search import Search
from models.ResultsPdfs import ResultPdfs
from utils.PdfDownload import download_pdf
from manipulators.S3Manipulators import S3Uploader
from manipulators.SnsManipulator import SNSManipulator

from datetime import datetime
import traceback
class CommertialController:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.getLink = GetLinkDriver()
        self.search = Search()
        self.web_result = ResultPdfs()
        self.s3_uploader = S3Uploader()
        self.sns_manipulator = SNSManipulator()
    
    def run(self, name):
        try:
            mes_atual = datetime.now().strftime("%m-%y")
            nome_bucket_s3 = "my-tf-prodesp-bucket"
            
            self.driver = self.getLink.get_link()  
            self.search.search_client(name)  
            document_download_links = self.web_result.web_result()
            pdf_bytes = download_pdf(document_download_links)

            for i, content in enumerate(pdf_bytes, start=1):
                try:
                    chave_no_s3 = f"coletas/prodesp/{name}/{mes_atual}/{i}.pdf"
                    self.s3_uploader.upload_to_s3(content, nome_bucket_s3, chave_no_s3)
                except:
                    print(e)
                else:
                    self.sns_manipulator.publicar_mensagem(chave_no_s3)
                
        except Exception as e:
            print("erro ao executar o coletor do Prodesp")
            print(e)
            traceback.print_exc()