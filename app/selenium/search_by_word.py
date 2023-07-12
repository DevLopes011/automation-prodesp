from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


class Search_by_word:
    def __init__(self):
        pass
    
    def drive(self):
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico)
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        driver.find_element(By.XPATH, "xpath")
        

search_by_word = Search_by_word()
search_by_word.drive()
