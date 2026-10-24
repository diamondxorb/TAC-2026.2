# Evolução Temática da Produção Científica em Computação no Brasil (2010-2024)

Este repositório contém a esteira de dados e as análises para o mapeamento longitudinal da produção científica na pós-graduação brasileira. O projeto aplica o processo de *Knowledge Discovery in Databases* (KDD), modelagem neural de tópicos e algoritmos de classificação nos microdados abertos da CAPES para rastrear a ascensão de áreas como Inteligência Artificial e Aprendizado de Máquina.

## Estrutura do Projeto
* `data/`: Armazena a base de dados consolidada e compactada (formato `.csv.gz`), pronta para análise.
* `scripts/`: Códigos Python para extração automatizada e limpeza dos dados governamentais.
* `notebooks/`: Arquivos Jupyter com as etapas de pré-processamento de NLP, modelagem de tópicos (BERTopic, LDA) e classificação supervisionada (Random Forest, GBM, SVM).

## Pré-requisitos e Configuração do Ambiente
Para garantir a reprodutibilidade, recomenda-se a utilização de um ambiente virtual Python isolado.

1. Clone o repositório:
```bash
git clone https://github.com/diamondxorb/TAC-2026.2.git
cd TAC-2026.2
```

2. Crie e ative o ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências externas para análise (versão CPU otimizada):
```bash
pip install -r requirements.txt
```

4. Baixe o modelo de linguagem em português do spaCy (necessário para a etapa de lematização no notebook 01):
```bash
python -m spacy download pt_core_news_sm
```

## Execução das Análises
Como as bases de dados já estão limpas e compactadas na pasta `data/`, você pode ir direto para as análises metodológicas. Basta iniciar o servidor do Jupyter:

```bash
jupyter notebook
```
Acesse a pasta `notebooks/` no seu navegador e execute os arquivos sequencialmente:
1. `01_pre_processamento_nlp.ipynb`: Limpeza profunda e lematização dos resumos.
2. `02_modelagem_topicos.ipynb`: Aplicação do BERTopic, geração de embeddings e gráficos de evolução temporal.

## Coleta e Limpeza de Dados (Opcional)
Se você deseja auditar ou recriar a base de dados do zero a partir do portal da CAPES, siga os passos abaixo. 

**Nota:** O pacote de extração foi removido do `requirements.txt` padrão para manter o ambiente leve. Instale-o manualmente primeiro:
```bash
pip install git+https://github.com/diamondxorb/catalogos-capes.git
```

Em seguida, execute os scripts sequencialmente:
1. **Download:** Extrai os pacotes CSV anuais diretamente do portal da CAPES.
```bash
python scripts/baixar_capes.py
```
2. **Consolidação:** Filtra os trabalhos da área de Avaliação "Ciência da Computação", padroniza colunas, remove anomalias e gera a versão `.csv.gz`.
```bash
python scripts/limpeza_planilhas.py
```

## Autoria
* **Júlia Paulo Amorim** (Universidade de Brasília)
* **Letícia Gonçalves Bomfim** (Universidade de Brasília)