from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from pathvalidate import sanitize_filename
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import os
import time
# tenha 1 classe q cria o driver e o wait
# tenha outra classe q faça o processo de acessar o site e coletar as informações

class WebDriver:
    def __init__(self):
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
        "download.default_directory": "C:\\KOR\\automation-prodesp\\PDFs", #Change default directory for downloads
        "download.prompt_for_download": False, #To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
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
        
        elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="content_dtgResultado_lblData_0"]')))
        elements.click()
                
        counter = 1
        for element in elements:
            link = element.get_attribute("href")
            links.append(link)
            print(links)


            response = requests.get(link)

            if response.status_code == 200:
                ext = link.split('.')[-1]
                
                cleaned_filename = sanitize_filename(f'{counter}.{ext}')
                
                filename = os.path.join(folder_name, cleaned_filename)
                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        f.write(chunk)
                    
                print('PDF baixado com sucesso:', cleaned_filename)
                
                counter += 1
            else:
                print('Falha ao baixar o PDF:', link)



        
drive = Drive()
drive.search_company_name('"Azul Linhas Aéreas"')





            #CÓDIGO PARA TENTAR PEGAR PDFS
        # for url in links:
        # # Abrir uma nova janela
        #     driver.execute_script(f"window.open('{url}');")

        #     # Trocar para a nova janela
        #     driver.switch_to.window(driver.window_handles[-1])

        #     # Acessar a URL
        #     driver.get(url)

        #     # Baixar o arquivo em formato binário
        #     arquivo = driver.find_element_by_xpath("//a[@href='{}']".format(url))
        #     arquivo.click()