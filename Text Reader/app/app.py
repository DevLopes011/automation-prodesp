from controllers.CommertialController import CommertialController
import os
from dotenv import load_dotenv

load_dotenv()

pdfs_directory = 'C:\\OtherFiles\\repos-temp\\automation-prodesp\\Text Reader\\app\\PDFS'
output_file = 'output_nires.txt'  # Caminho do arquivo de saída

commertialController = CommertialController()
commertialController.run(pdfs_directory)
 