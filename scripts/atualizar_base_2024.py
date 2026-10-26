import pandas as pd
import os

# 1. Definição dos caminhos
caminho_base_existente = "./data/dados_capes_computacao_2010_2024.csv.gz"
caminho_2024 = "./data/brutos/dados_2024.csv" 

colunas_padrao = [
    "AN_BASE", "NM_PROGRAMA", "SG_ENTIDADE_ENSINO", 
    "NM_REGIAO", "NM_GRAU_ACADEMICO", "NM_PRODUCAO", 
    "DS_PALAVRA_CHAVE", "DS_RESUMO", "NM_AREA_AVALIACAO"
]

print("Carregando a base consolidada (2010-2023)...")
df_existente = pd.read_csv(caminho_base_existente, compression='gzip', low_memory=False)

print("Limpando e filtrando os dados novos de 2024...")
# Tenta ler o arquivo garantindo que o delimitador seja interpretado corretamente
df_2024 = pd.read_csv(caminho_2024, sep=';', usecols=colunas_padrao, encoding='latin1', low_memory=False)

# Padroniza a coluna para maiúsculo e remove espaços extras
df_2024['NM_AREA_AVALIACAO'] = df_2024['NM_AREA_AVALIACAO'].astype(str).str.strip().str.upper()

# Nova filtragem abrangente: captura qualquer área que contenha "COMPUTA" 
# (pega CIÊNCIA DA COMPUTAÇÃO, CIENCIA DA COMPUTACAO, etc.)
df_2024_filtrado = df_2024[df_2024['NM_AREA_AVALIACAO'].str.contains('COMPUTA', na=False)]

print(f"Trabalhos de Computação encontrados em 2024: {len(df_2024_filtrado)}")

print("Mesclando as bases...")
df_atualizado = pd.concat([df_existente, df_2024_filtrado], ignore_index=True)

# Padroniza o Grau Acadêmico para evitar duplicatas (ex: MESTRADO vs Mestrado)
df_atualizado['NM_GRAU_ACADEMICO'] = df_atualizado['NM_GRAU_ACADEMICO'].str.upper().str.strip()

# Limpeza final
df_atualizado = df_atualizado.dropna(subset=['DS_RESUMO'])
df_atualizado = df_atualizado.drop_duplicates(subset=['DS_RESUMO', 'NM_PRODUCAO'])

print("Salvando a base unificada final (2010-2024)...")
df_atualizado.to_csv(caminho_base_existente, index=False, encoding='utf-8', compression='gzip')

print(f"Sucesso! A base completa agora contém {len(df_atualizado)} registros.")