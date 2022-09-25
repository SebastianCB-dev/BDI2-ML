import json
import pandas as pd
from preprocessing_service import preprocesamiento
from embeddings import word_space
from preprocessing_service import preprocesamiento_no_ortografia
from file_service import read_json, read_txt
from gensim.models import Word2Vec
from pprint import pprint
# Leer información del archivo items.json y de comentariostest
beck_data = json.loads(read_json('./JSON/items.json'))
comments_array = list(read_txt('./comentarios_test.txt'))

# Arreglo de las 21 categorias del BDI-II
types = list(beck_data.keys())

beck_data_preprocessing = {}
try:
  if open('./JSON/items_preprocessing.json', 'r'):
    beck_data_preprocessing = json.loads(read_json('./JSON/items_preprocessing.json'))
except Exception as e:
  print(f'Error: {e}')  

# pprint(beck_data_preprocessing)
#!Vector Space Embedding
model = Word2Vec.load('word2vec.model')
