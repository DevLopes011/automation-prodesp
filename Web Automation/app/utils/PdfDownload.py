import requests

def download_pdf(urls):
    pdf_contents = [] 

    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            pdf_content = response.content
            pdf_contents.append(pdf_content)  # Adiciona o conteúdo do PDF à lista
            print(f"PDF '{url}' baixado com sucesso!")
        else:
            print(f"Erro ao obter o PDF da URL '{url}':", response.status_code)
    
    return pdf_contents  # Retorna a lista de conteúdos dos PDFs
