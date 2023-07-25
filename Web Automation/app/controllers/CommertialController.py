from models.GetLinkDriver import GetLinkDriver
from models.Search import Search
from models.ResultsPdfs import ResultPdfs
from utils.PdfDownload import PdfDownloader
from models.S3Uploader import S3Uploader

class CommertialController:
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def run(self, name):
        nome_bucket_s3 = "my-tf-prodesp-bucket"
        chave_no_s3 = f"pasta/{name}{i}.pdf"  
        
        
        getLink = GetLinkDriver()
        search = Search()
        web_result = ResultPdfs()
        pdfDownloader = PdfDownloader()
        s3_uploader = S3Uploader()
        
        self.driver = getLink.get_link()  
        search_box = search.search_cli(name, self.driver)  
        links_inside_iframe = web_result.web_result(search_box)
        pdf_bytes = pdfDownloader.download_pdf(links_inside_iframe)
        self.driver.quit()
        for i, content in enumerate(pdf_bytes, start=1):
            chave_no_s3 = f"{name}{i}.pdf"  
            s3_uploader.upload_to_s3(content, nome_bucket_s3, chave_no_s3)

