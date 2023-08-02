from models.FileManager import FileManager
from uuid import uuid4

my_uuid = uuid4()

class CommertialController:
    def run(self, pdfs_directory, output_file):
        fileManager = FileManager()
        pdf_documents = fileManager.open_pdf_files(pdfs_directory)

        info_total = []  # Inicializar uma lista para armazenar todas as informações encontradas

        for pdf_document in pdf_documents:
            texto_completo = ''
            num_pages = pdf_document.page_count
            page_num = 0

            while page_num < num_pages:  
                page = pdf_document[page_num]
                texto_pagina = page.get_text()
                texto_completo += texto_pagina            
                nires_encontrados = fileManager.extrair_nires(texto_completo)
                numeros_alteracao = fileManager.extrair_numeros_alteracao(texto_completo)
                motivos = fileManager.extrair_motivos(texto_completo)

                if nires_encontrados and numeros_alteracao and motivos:
                    break

                page_num += 1

            pdf_document.close()

            # Combinar as informações em uma única lista de tuplas
            info_pagina = list(zip(nires_encontrados, numeros_alteracao, motivos))
            info_total.extend(info_pagina)

        # Salvar as informações no arquivo de texto
        with open(output_file, 'w') as f:
            f.write("NIREs, Números de Alteração e Motivos encontrados:\n")
            for nire, numero_alteracao, motivo in info_total:
                f.write(f"NIRE: {nire}, Número de Alteração: {numero_alteracao}, Motivo: {motivo}\n")

        print("Informações (NIREs, Números de Alteração e Motivos) encontradas e salvas no arquivo:", output_file)
