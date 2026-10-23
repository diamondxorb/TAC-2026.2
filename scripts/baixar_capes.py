import os
import re
from catalogos_capes import datasets

# Cria a pasta data/brutos automaticamente se ela não existir
diretorio_destino = "./data/brutos"
os.makedirs(diretorio_destino, exist_ok=True)

print("Consultando o portal da CAPES...")
df = datasets.get_all_datasets_with_resources() 
df_teses = datasets.get_dataset_by_name(df, 'Catálogo de Teses e Dissertações', 'CSV')

print("Iniciando a triagem de arquivos por ano...")

for url in df_teses['url']:
    nome_arquivo = url.split('/')[-1]
    
    # Procura por um padrão de ano (19XX ou 20XX) no nome do arquivo
    match = re.search(r'(19|20)\d{2}', nome_arquivo)
    
    if match:
        ano = int(match.group())
        
        # Verifica se o ano está dentro do recorte da pesquisa
        if 2010 <= ano <= 2024:
            caminho_arquivo = os.path.join(diretorio_destino, nome_arquivo)
            
            # Checa se o arquivo já foi baixado anteriormente
            if os.path.exists(caminho_arquivo):
                print(f"Pulando (já baixado): {nome_arquivo}")
            else:
                print(f"Baixando ano {ano}: {url}")
                datasets.download_file(url, diretorio_destino)
        else:
            print(f"Pulando ano {ano} (fora do recorte 2010-2024): {nome_arquivo}")
            
    else:
        # Caso algum arquivo não tenha o ano no nome, baixa por precaução
        print(f"Atenção: Não foi possível identificar o ano no arquivo {nome_arquivo}. Baixando...")
        datasets.download_file(url, diretorio_destino)

print("Processo finalizado!")