import json
import pandas as pd
from preprocessing_service import preprocesamiento, preprocesamiento_items_beck
from file_service import read_json, read_txt
import pprint
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
  beck_data_preprocessing = preprocesamiento_items_beck(beck_data, types)
  f = open("./JSON/items_preprocessing.json", "a")
  f.write(str(json.dumps(beck_data_preprocessing, indent=2)))
  f.close()

pprint.pprint(beck_data_preprocessing)    
    
    
    