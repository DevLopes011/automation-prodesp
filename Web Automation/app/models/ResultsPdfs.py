# ResultsPdfs.py
from utils.WebDriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time


class ResultPdfs:
    def __init__(self):
        self.wait = WebDriver.wait
        self.driver = WebDriver.driver
    
    def web_result(self, links):
        links = []
        links_inside_iframe = []
        search_box = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/a[1]")))
        search_box.send_keys(Keys.ENTER)
        search_box = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/a[1]")))
        search_box.send_keys(Keys.ENTER)
        
        sort_date = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content_lnkOrderByData"]')))
        sort_date.send_keys(Keys.ENTER)
        
        elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="aCertificador"]')))
                
        for element in elements:
            link = element.get_attribute("href")
            links.append(link)
        
        for link in links:
            self.driver.get(link)
            
            iframe = self.wait.until(EC.presence_of_element_located((By.NAME, 'GatewayCertificaPDF')))
            self.driver.switch_to.frame(iframe)
            
            main_content = self.driver.find_element(By.XPATH, '//*[@id="main-content"]/a')
            links_inside_iframe.append(main_content.get_attribute("href"))
                
                        
        return links_inside_iframe
