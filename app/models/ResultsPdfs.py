# ResultsPdfs.py
from utils.WebDriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class ResultPdfs:
    def __init__(self):
        self.wait = WebDriver.wait
        self.driver = WebDriver.driver
    
    def web_result(self, popups):
        links = []
        popups = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/a[1]")))
        popups.send_keys(Keys.ENTER)
        popups = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/a[1]")))
        popups.send_keys(Keys.ENTER)
        
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
            
            links_inside_main_content = main_content.find_elements(By.TAG_NAME, 'a')   
                     
            main_content.send_keys(Keys.ENTER)

            for inner_link in links_inside_main_content:
                print(inner_link.get_attribute("href"))
            
            self.driver.switch_to.default_content()
            
        self.driver.quit()
