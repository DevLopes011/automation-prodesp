from models.FileManager import FileManager
from uuid import uuid4
from models.AwsManager import AwsManager
import re

my_uuid = uuid4()

class CommertialController:
    def __init__(self):
        pass


    def run(self, pdfs_directory):
        awsManager = AwsManager()
        fileManager = FileManager()
        pdf_documents = fileManager.open_pdf_files(pdfs_directory)

        PATTERN_BLOCKS = r"NIRE(.*?)(?=(?:NIRE|$))"

        nires_especificos = ['35300359534']  # Substitua pelos NIREs que você deseja procurar

        for pdf_document in pdf_documents:
            texto_completo = ''
            num_pages = pdf_document.page_count
            page_num = 0

            while page_num < num_pages:  
                page = pdf_document[page_num]
                texto_pagina = page.get_text()
                texto_completo += texto_pagina
                page_num += 1

            pdf_document.close()
 
            pdf_document_single_line = texto_completo.replace("\n", "")
            print("Texto extraído do PDF:")
            # print(pdf_document_single_line)  # Verifique se o texto extraído está correto

            matchs = re.findall(PATTERN_BLOCKS, pdf_document_single_line, re.DOTALL)
            # print(matchs)
            data_list = fileManager.parse_text(matchs)

            for nire_cli in data_list:
                if nire_cli["NIRE"] in nires_especificos:
                    result = nire_cli
                    print("Resultado para o NIRE específico:", result)
                
            
            
            

    



            # for idx, match in enumerate(matches):
            #     nire = nires[idx] if idx < len(nires) else "N/A"
            #     alteracao = match[0]
            #     informacao = match[1]
                
                # if nire in nires_especificos:
                #     print("NIRE:", nire)
                #     print("Número da Alteração:", alteracao)
                #     print("Informação:", informacao)
                #     print("-----")

        # Restante do código continua igual

            
            
            # blocks = fileManager.pattern_blocks(pdf_document_single_line)
            # # print(blocks)
            # for block in blocks:
            #     print(block)
                # client_result = fileManager.extrair_nires(block)
                # print(client_result)
                # print(len(client_result))
            # response_upload = awsManager.upload_dynamo(uuid = my_uuid,
            #                                            nires_encontrados = nires_encontrados,
            #                                            numeros_alteracao = numeros_alteracao,
            #                                            motivos = motivos)
            
            # print(response_upload)

        # Salvar as informações no arquivo de texto
        # with open(output_file, 'w') as f:
        #     f.write("NIREs, Números de Alteração e Motivos encontrados:\n")
        #     for nire, numero_alteracao, motivo in info_total:
        #         f.write(f"NIRE: {nire}, Número de Alteração: {numero_alteracao}, Motivo: {motivo}\n")

        # print("Informações (NIREs, Números de Alteração e Motivos) encontradas e salvas no arquivo:", output_file)
        
