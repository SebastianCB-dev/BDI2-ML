import json
import pandas as pd
from gensim.models import Word2Vec
from pprint import pprint
from preprocessing_service import Preprocesamiento
# Leer información del archivo items.json y de comentariostest
comments_array = list(open('./comentarios_test.txt', 'r', encoding='utf-8').readlines())

beck_data_preprocessing = {}
try:
  if open('./JSON/items_preprocessing.json', 'r'):
    beck_data_preprocessing = json.loads(open('./JSON/items_preprocessing.json', 'r', encoding='utf-8').read())
except Exception as e:
  print(f'Error: {e}')  

# pprint(beck_data_preprocessing)
#!Vector Space Embedding
model = Word2Vec.load('word2vec.model')

preprocesamiento = Preprocesamiento()

comment_test = preprocesamiento.preprocesamiento_con_ortografia(comments_array[0])

array_item = []
for key in beck_data_preprocessing["Pensamiento o deseos suicidas"].keys():
  array_item.append(beck_data_preprocessing["Pensamiento o deseos suicidas"][key]["data"])

print(comment_test)
i = 0
for item in array_item:
  coseno = model.wv.wmdistance(comment_test, item)
  print(f'Item BECK {i} distancia coseno: ${coseno}')
  i += 1
