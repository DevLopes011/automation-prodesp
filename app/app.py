import urllib.request

# URL do PDF
pdf_url = "http://www.imprensaoficial.com.br/Certificacao/GatewayCertificaPDF.aspx?notarizacaoID=88e1ac3e-d267-4edf-8168-7e2af684d2ab"

# Caminho para salvar o PDF
pdf_path = "C:\\KOR\\automation-prodesp\\PDFs\\nome_do_arquivo.pdf"

# Faz o download do PDF
urllib.request.urlretrieve(pdf_url, pdf_path)

print("PDF baixado com sucesso!")
