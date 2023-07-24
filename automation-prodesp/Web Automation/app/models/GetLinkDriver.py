from utils.WebDriver import WebDriver

class GetLinkDriver:
    def __init__(self):
        self.webdrivers = WebDriver()  # Instanciar o WebDriver para uso interno

    def get_link(self):
        driver = self.webdrivers.driver
        driver.get("http://www.imprensaoficial.com.br/")
        return driver
