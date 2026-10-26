"""Dicionário de IA aplicado a título + palavras-chave + resumo originais (não lematizados)."""
import re
import unicodedata

def norm(s):
    s = str(s).lower()
    s = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in s if not unicodedata.combining(c))

# Termos (já sem acento). \b nas bordas; plural opcional onde faz sentido.
TERMOS_IA = [
    r'inteligencia artificial', r'artificial intelligence',
    r'aprendizado de maquina', r'aprendizagem de maquina', r'machine learning',
    r'aprendizado profundo', r'aprendizagem profunda', r'deep learning',
    r'redes? neura(?:l|is)', r'neural networks?', r'perceptron',
    r'redes? (?:neurais )?convolucion(?:al|ais)', r'convolutional',
    r'lstm', r'transformers?', r'\bbert\b', r'\bgpt', r'\bllms?\b',
    r'modelos? de linguagem', r'language models?',
    r'processamento de linguagem natural', r'natural language processing', r'\bpln\b', r'\bnlp\b',
    r'visao computacional', r'computer vision',
    r'mineracao de dados', r'data mining', r'mineracao de textos?', r'text mining',
    r'aprendizado (?:supervisionado|nao supervisionado|semi-supervisionado|por reforco)',
    r'reinforcement learning', r'supervised learning',
    r'classificadore?s', r'classifiers?',
    r'support vector', r'maquinas? de vetores? de suporte', r'\bsvm\b',
    r'random forest', r'floresta aleatoria', r'arvores? de decisao', r'decision trees?',
    r'k-means', r'k-nearest', r'\bknn\b', r'naive bayes', r'redes? bayesianas?',
    r'gradient boosting', r'xgboost',
    r'algoritmos? geneticos?', r'genetic algorithms?', r'computacao evolutiva', r'evolutionary',
    r'otimizacao por enxame', r'particle swarm', r'colonia de formigas',
    r'logica fuzzy', r'fuzzy logic', r'sistemas? fuzzy',
    r'sistemas? multiagentes?', r'multi-?agent', r'agentes? inteligentes?',
    r'reconhecimento de padroes', r'pattern recognition',
    r'sistemas? de recomendacao', r'recommender systems?',
    r'ciencia de dados', r'data science',
]
PADRAO_IA = re.compile(r'\b(?:' + '|'.join(TERMOS_IA) + r')', re.IGNORECASE)

def texto_doc(row):
    return norm(' '.join(str(row[c]) for c in ('NM_PRODUCAO', 'DS_PALAVRA_CHAVE', 'DS_RESUMO')))

def eh_ia(texto_normalizado):
    return bool(PADRAO_IA.search(texto_normalizado))

def termos_encontrados(texto_normalizado):
    return sorted(set(m.group(0) for m in PADRAO_IA.finditer(texto_normalizado)))
