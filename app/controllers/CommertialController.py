from models.Search import Search
from models.ResultsPdfs import ResultPdfs
from models.GetLinkDriver import GetLinkDriver

class CommertialController:
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def run(self, name):
        search = Search()
        web_result = ResultPdfs()
        getLink = GetLinkDriver()

        driver = getLink.get_link()  
        search.search_cli(name, driver)  
        web_result.web_result(driver) 
