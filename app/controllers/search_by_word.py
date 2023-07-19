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
# tenha 1 classe q cria o driver e o wait
# tenha outra classe q faça o processo de acessar o site e coletar as informações

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
        self.driver.implicitly_wait(30)
        

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
 
        
           #PESQUISAR SOBRE IFRAME
        for link in links:
            driver.get(link)
            
            
                            # Switch frame by id
            driver.switch_to.frame('buttonframe')

                # Now, Click on the button
            driver.find_element(By.TAG_NAME, 'button').click()
            time.sleep(5000)
            
                # switching to second iframe based on index
            iframe = driver.find_elements(By.XPATH,'//*[@id="main-content"]/a')[1]
            
            
            #driver.find_element(By.XPATH, '//*[@id="main-content"]/a')
        print(iframe)    
        
        
        
        
            # x_coord = 400
            # y_coord = 200
            # actions = ActionChains(driver)
            # actions.move_by_offset(x_coord, y_coord).perform()
            
            # actions.click()
            # time.sleep(3)
            # #actions.click(element).send_keys(Keys.TAB).perform()
            # actions.send_keys(Keys.ENTER)
    
            # actions.perform()
        
            
        #print(driver)
            
        #     time.sleep(5)
        #     time.sleep(5000)
        #     drive.find_element(By.XPATH, '/html/body')
        #     drive.send_keys(Keys.ENTER)
        #     link_inside_xpath = drive.get_attribute("href")
            
        # print(link_inside_xpath)
            
            
            
            # link_down = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content"]/a')))

            # download_link = link_down.get_attribute("href")
            # print(download_link)
                        
            # link_down = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content"]/a')))
            # link_down.get_attribute("href")
            # links.append(link_down)
            
            
            
            
            
        
        # for link in links:
                                    
        #     pdf_path = "C:\\KOR\\automation-prodesp\\PDFs\\nome_do_arquivo.pdf"
        #     urllib.request.urlretrieve(link_down, pdf_path)

        #     print("PDF baixado com sucesso!")
                    
            
        # print(link_down)
            
              
                
                
                
                
                
           #time.sleep(500)
            # response = requests.get(link)
        # print(driver)
        


        
drive = Drive()
drive.search_company_name('"Azul Linhas Aéreas"')

