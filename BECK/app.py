import json
import pandas as pd
from preprocessing_service import preprocesamiento
from file_service import read_json, read_txt

# Leer información del archivo items.json y de comentariostest
beck_data = json.loads(read_json('./items.json'))
comments_array = list(read_txt('./comentarios_test.txt'))

# Arreglo de las 21 categorias del BDI-II
types = list(beck_data.keys())

# Preprocesamiento con el primer comentario y primer item de la prueba BDI
first_comment_preprocessing = preprocesamiento(comments_array[0])

dict_items_preprocessing = {}
for item in list(beck_data[types[0]].keys()):
  dict_items_preprocessing[item] = preprocesamiento(item)

print(dict_items_preprocessing)
