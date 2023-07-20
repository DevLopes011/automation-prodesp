from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

class WebDriver:
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
    driver = webdriver.Chrome(service=servico, options=options)
    wait = WebDriverWait(driver, 10)