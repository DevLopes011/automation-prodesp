from models.GetLinkDriver import GetLinkDriver
from models.Search import Search
from models.ResultsPdfs import ResultPdfs
from utils.PdfDownload import PdfDownloader
from utils.S3Uploader import S3Uploader

class CommertialController:
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def run(self, name):
        getLink = GetLinkDriver()
        search = Search()
        web_result = ResultPdfs()
        pdfDownloader = PdfDownloader()
        s3_uploader = S3Uploader()
        
        self.driver = getLink.get_link()  
        search_box = search.search_cli(name, self.driver)  
        links_inside_iframe = web_result.web_result(search_box)
        pdf_bytes = pdfDownloader.download_pdf(links_inside_iframe)
        print(pdf_bytes)

        # Configurações para o upload no Amazon S3
        nome_bucket_s3 = "my-tf-prodesp-bucket"
        chave_no_s3 = "s3://my-tf-prodesp-bucket/teste/"  # Coloque o caminho e nome desejado no S3

        # Cria uma instância do S3Uploader (ou 'boto3', se preferir)
        

        # Faz o upload dos PDFs para o Amazon S3
        upload_sucesso = s3_uploader.upload_to_s3(pdf_bytes, nome_bucket_s3, chave_no_s3)
        if upload_sucesso:
            print("Upload para o S3 realizado com sucesso!")

        self.driver.quit()
