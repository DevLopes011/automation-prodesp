from models.GetLinkDriver import GetLinkDriver
from models.Search import Search
from models.ResultsPdfs import ResultPdfs
from utils.FileManager import FileManager
from utils.PdfDownload import PdfDownloader

class CommertialController:
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def run(self, name):
        getLink = GetLinkDriver()
        search = Search()
        web_result = ResultPdfs()
        pdfDownloader = PdfDownloader()

        self.driver = getLink.get_link()  
        search_box = search.search_cli(name, self.driver)  
        links_inside_iframe = web_result.web_result(search_box)
        pdf_bytes = pdfDownloader.download_pdf(links_inside_iframe)
        print(type(pdf_bytes))

        
        self.driver.quit()
