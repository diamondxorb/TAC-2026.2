# Evolução Temática da Produção Científica em Computação no Brasil (2010-2024)

Este repositório contém a esteira de dados e as análises para o mapeamento longitudinal da produção científica na pós-graduação brasileira. O projeto aplica o processo de *Knowledge Discovery in Databases* (KDD), modelagem neural de tópicos e algoritmos de classificação nos microdados abertos da CAPES para rastrear a ascensão de áreas como Inteligência Artificial e Aprendizado de Máquina.

## Estrutura do Projeto
* `data/`: Armazena a base de dados consolidada e pré-processada.
* `scripts/`: Códigos Python para extração automatizada e limpeza dos dados governamentais.
* `notebooks/`: Arquivos Jupyter com as etapas de pré-processamento de NLP, modelagem de tópicos (BERTopic, LDA) e classificação supervisionada (Random Forest, GBM, SVM).

## Pré-requisitos e Configuração do Ambiente
Para garantir a reprodutibilidade, recomenda-se a utilização de um ambiente virtual Python isolado.

1. Clone o repositório:
```bash
git clone [https://github.com/diamondxorb/TAC-2026.2.git](https://github.com/diamondxorb/TAC-2026.2.git)
cd TAC-2026.2
```

2. Crie e ative o ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências externas:
```bash
pip install -r requirements.txt
```

4. Baixe o modelo de linguagem em português do spaCy (necessário para a etapa de lematização):
```bash
python -m spacy download pt_core_news_sm
```

## Execução da Coleta e Limpeza de Dados
Com o ambiente ativado, execute os scripts sequencialmente a partir da raiz do projeto para recriar a base de dados central:

1. **Download:** Extrai os pacotes CSV anuais diretamente do portal da CAPES.
```bash
python scripts/baixar_capes.py
```

2. **Consolidação:** Filtra os trabalhos da área de Avaliação "Ciência da Computação" no recorte temporal de 2010 a 2024, padroniza colunas e remove anomalias.
```bash
python scripts/limpeza_planilhas.py
```

## Autoria
* **Júlia Paulo Amorim** (Universidade de Brasília)
* **Letícia Gonçalves Bomfim** (Universidade de Brasília)