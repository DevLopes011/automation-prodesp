from utils.WebDriver import WebDriver

class GetLinkDriver:
    def __init__(self):
        self.driver = WebDriver.driver  # Instanciar o WebDriver para uso interno

    def get_link(self):
        self.driver.get("http://www.imprensaoficial.com.br/")
