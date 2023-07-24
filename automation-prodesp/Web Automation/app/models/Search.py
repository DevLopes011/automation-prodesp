from models.GetLinkDriver import GetLinkDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Search:
    def __init__(self):
        self.driver = GetLinkDriver()

    def search_cli(self, name, driver):
        search_box = driver.find_element(By.XPATH, '//*[@id="content_txtPalavrasChave"]')
        search_box.send_keys(name)
        search_box.send_keys(Keys.ENTER)

        return search_box
