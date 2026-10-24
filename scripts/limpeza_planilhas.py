import pandas as pd
import glob
import os

# Padrão Novo (2013 a 2024)
colunas_padrao = [
    "AN_BASE", "NM_PROGRAMA", "SG_ENTIDADE_ENSINO", 
    "NM_REGIAO", "NM_GRAU_ACADEMICO", "NM_PRODUCAO", 
    "DS_PALAVRA_CHAVE", "DS_RESUMO", "NM_AREA_AVALIACAO"
]

# Padrão Antigo (2010 a 2012)
colunas_antigas = [
    "AnoBase", "NomePrograma", "SiglaIes", 
    "Regiao", "Nivel", "TituloTese", 
    "PalavrasChave", "ResumoTese", "AreaAvaliacao"
]

# Dicionário de tradução do padrão antigo para o novo
mapa_renomeacao = {
    "AnoBase": "AN_BASE",
    "NomePrograma": "NM_PROGRAMA",
    "SiglaIes": "SG_ENTIDADE_ENSINO",
    "Regiao": "NM_REGIAO",
    "Nivel": "NM_GRAU_ACADEMICO",
    "TituloTese": "NM_PRODUCAO",
    "PalavrasChave": "DS_PALAVRA_CHAVE",
    "ResumoTese": "DS_RESUMO",
    "AreaAvaliacao": "NM_AREA_AVALIACAO"
}

# Caminho relativo apontando para os dados brutos baixados pelo outro script
caminho_arquivos = "./data/brutos/*.csv"
arquivos = glob.glob(caminho_arquivos)
dataframes = []

for arquivo in arquivos:
    print(f"Processando arquivo: {os.path.basename(arquivo)}...")
    try:
        # Tenta ler com o padrão de colunas novo
        df = pd.read_csv(arquivo, sep=';', usecols=colunas_padrao, encoding='latin1', low_memory=False)
    except ValueError:
        try:
            # Se der erro (ValueError), tenta ler com o padrão antigo
            df = pd.read_csv(arquivo, sep=';', usecols=colunas_antigas, encoding='latin1', low_memory=False)
            
            # Renomeia as colunas antigas para ficarem iguais às novas
            df = df.rename(columns=mapa_renomeacao)
            print(f" -> Formato antigo detectado e convertido com sucesso!")
        except Exception as e:
            print(f" Erro fatal ao ler {arquivo}: {e}")
            continue

    # Padroniza a coluna e filtra (garantindo que seja tratada como texto)
    df['NM_AREA_AVALIACAO'] = df['NM_AREA_AVALIACAO'].astype(str)
    area_padronizada = df['NM_AREA_AVALIACAO'].str.strip().str.upper()
    
    df_filtrado = df[area_padronizada.isin(['CIÊNCIA DA COMPUTAÇÃO', 'CIENCIAS DA COMPUTACAO'])]
    dataframes.append(df_filtrado)

# Consolida tudo
if dataframes:
    df_kdd = pd.concat(dataframes, ignore_index=True)

    df_kdd = df_kdd.dropna(subset=['DS_RESUMO'])
    df_kdd = df_kdd.drop_duplicates(subset=['DS_RESUMO', 'NM_PRODUCAO'])
    
    # Salva o arquivo limpo diretamente na pasta data
    caminho_saida = "./data/dados_capes_computacao_2010_2024.csv.gz"
    df_kdd.to_csv(caminho_saida, index=False, encoding='utf-8', compression='gzip')
    
    print(f"\nProcessamento concluído com sucesso!")
    print(f"Total de trabalhos (Mestrado/Doutorado) retidos para a IA: {len(df_kdd)}")
    print(f"Arquivo salvo em: {caminho_saida}")
else:
    print("Nenhum dado encontrado.")