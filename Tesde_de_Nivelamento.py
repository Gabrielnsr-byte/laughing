import requests
import os
import zipfile

def baixar_e_arquivos(url, diretorio_download, nome_zip):
    """Baixa arquivos PDF e compactar em ZIP"""
os.makedirs(diretorio_download, exist_ok=True)
links_pdf = [
    "..."

    "..."
] #Listas com links para arquivos PDF 
for link in links_pdf:
    nome_arquivo = os.path.join(diretorio_download, link.split("/")[-1])

    with requests.get(link, stream=true) as resposta_pdf:
        resposta_pdf.raise_for_status()
        with open(nome_arquivo, "wb") as arquivo_pdf:
            for chunk in resposta_pdf.iter_content(chunk_size=8192):
                arquivo_pdf.write(chunk)

    print(f"Arquivo {nome_arquivo} baixado. ")

   with zipfile.ZipFile(nome_zip, "w") as arquivo_zip:
        for nome_arquivo in os.listdir(diretorio_download):
            caminho_arquivo = os.path.join(diretorio_download, nome_arquivo)
            if os.path.isfile(caminho_arquivo):
                arquivo_zip.write(caminho_arquivo, nome_arquivo)
                
    print(f"Arquivos compactados em {nome_zip}.")

#configurações
url_ans = "..."
diretorio_download = "arquivos_ans"
nome_zip = "anexos_ans.zip"

baixar_e_compactar(url_ans, diretorio_download, nome_zip)