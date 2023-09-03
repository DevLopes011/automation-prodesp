from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.WebDriver import WebDriver
class Search:
    def __init__(self):
        self.driver = WebDriver.driver

    def search_client(self, name):
        search_box = self.driver.find_element(By.XPATH, '//*[@id="content_txtPalavrasChave"]')
        search_box.send_keys(name)
        search_box.send_keys(Keys.ENTER)
