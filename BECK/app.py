import json
from pprint import pprint
import numpy as np
from sklearn.metrics import euclidean_distances

from preprocessing_service import Preprocesamiento
from model_word2vec_service import ModelWord2Vec
import nltk
nltk.download('punkt')

# Leer información del archivo items.json y de comentarios test
comments_array = list(open('./comentarios_test.txt',
                      'r', encoding='utf-8').readlines())

# Leer información del archivo item_preprocess.json
beck_data_preprocessing = {}
try:
    if open('./JSON/items_preprocessing.json', 'r'):
        beck_data_preprocessing = json.loads(
            open('./JSON/items_preprocessing.json', 'r', encoding='utf-8').read())
except Exception as e:
    print(f'Error: {e}')


preprocesamiento = Preprocesamiento()
# Vector Space Embedding
w2v = ModelWord2Vec()

comment_test = preprocesamiento.preprocesamiento_con_ortografia(
    comments_array[0])
array_item = []
# Get Vector Beck
item_string = 'Pensamiento o deseos suicidas'
for key in beck_data_preprocessing[item_string].keys():
  array_item.append(beck_data_preprocessing[item_string][key]["data"])

print(comment_test)
i = 0
for item in array_item:
  coseno = w2v.get_cosine_distance(item, comment_test) 
  print(f'{item_string} - Item BECK {i} distancia coseno: ${coseno}')
  euclidian = w2v.get_euclidian_distance(["hoy", "me", "quiero", "morir"], ["no", "morir"])
  print(f'{item_string} - Item BECK {i} distancia euclidiana: ${euclidian}')
  i += 1


result = w2v.getVectorBeck(comment_test, beck_data_preprocessing)
print(result)
