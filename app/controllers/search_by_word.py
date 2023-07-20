from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from pathvalidate import sanitize_filename
from selenium.webdriver.common.by import By
from selenium import webdriver
import urllib.request
import requests
import os
import time

class WebDriver:
    def __init__(self):
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": "C:\\KOR\\automation-prodesp\\PDFs",
            "download.directory_upgrade": True,
            "plugins.plugins_disabled": ["Chrome PDF Viewer"],
            "plugins.always_open_pdf_externally": True,
            "pdfjs.disabled": True,
            "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
            "profile.default_content_settings.popups": 0,
            "profile.default_content_setting_values.automatic_downloads": 1,
            "download.extensions_to_open": "applications/pdf",
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True,
            
        })        
        servico = Service(ChromeDriverManager().install())
    
        self.driver = webdriver.Chrome(service=servico, options=options)
        self.wait = WebDriverWait(self.driver, 10)     
        
class Drive:
    def __init__(self):
        self.driver = None
        self.wait = None
    
    
    def search_company_name(self, name):
        webdrivers = WebDriver()
        driver = webdrivers.driver
        wait = webdrivers.wait
        links = []
        driver.get("http://www.imprensaoficial.com.br/")
        
        folder_name = 'PDFs'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        search_box = driver.find_element(By.XPATH, '//*[@id="content_txtPalavrasChave"]')
        search_box.send_keys(name)
        search_box.send_keys(Keys.ENTER)
        
        popups = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/a[1]")))
        popups.send_keys(Keys.ENTER)   
        popups = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/a[1]")))
        popups.send_keys(Keys.ENTER)
        
        sort_date = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content_lnkOrderByData"]')))
        sort_date.send_keys(Keys.ENTER)
        
        elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="aCertificador"]')))
                
        for element in elements:
            link = element.get_attribute("href")
            links.append(link)
 
        
        for link in links:
            driver.get(link)
            
            iframe = wait.until(EC.presence_of_element_located((By.NAME, 'GatewayCertificaPDF')))
            driver.switch_to.frame(iframe)
            
            main_content = driver.find_element(By.XPATH, '//*[@id="main-content"]/a')
            
            links_inside_main_content = main_content.find_elements(By.TAG_NAME, 'a')   
                     
            main_content.send_keys(Keys.ENTER)

            for inner_link in links_inside_main_content:
                print(inner_link.get_attribute("href"))
            
            driver.switch_to.default_content()
            
        driver.quit()
        
drive = Drive()
drive.search_company_name('"Azul Linhas Aéreas"')