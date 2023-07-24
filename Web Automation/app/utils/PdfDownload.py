import requests

class PdfDownloader:
    def __init__(self):
        pass
    
    def download_pdf(self, urls):
        for url in urls:
            response = requests.get(url)

            if response.status_code == 200:
                pdf_content = response.content

                print(f"PDF '{pdf_content}' salvo com sucesso!")
            else:
                print(f"Erro ao obter o PDF da URL '{url}':", response.status_code)
        
        return pdf_content