import json
import pandas as pd
from gensim.models import Word2Vec
from pprint import pprint
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


data_beck = []

items = beck_data_preprocessing.keys()
for item in items:
  keys = beck_data_preprocessing[item].keys()
  for key in keys:
    data_beck.append(beck_data_preprocessing[item][key]["data"])

model.build_vocab(data_beck)
model.save('word2vec.model')











# comment_test = preprocesamiento(comments_array[0])

# array_item = []
# for key in beck_data_preprocessing["Pensamiento o deseos suicidas"].keys():
#   array_item.append(beck_data_preprocessing["Pensamiento o deseos suicidas"][key]["data"])

# print(comment_test)
# i = 0
# # for item in array_item:
# #   coseno = model.wv.distances(comment_test, item)
# #   print(f'Item BECK {i} distancia coseno: ${coseno}')

# model.wv.distances()