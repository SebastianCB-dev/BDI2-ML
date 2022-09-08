import json
import pandas as pd
from preprocessing_service import preprocesamiento
from file_service import read_json, read_txt
import pprint
# Leer información del archivo items.json y de comentariostest
beck_data = json.loads(read_json('./items.json'))
comments_array = list(read_txt('./comentarios_test.txt'))

# Arreglo de las 21 categorias del BDI-II
types = list(beck_data.keys())

beck_data_preprocessing = {}
for tipo in types:
  results = list(beck_data[tipo].keys())
  results_id = list(beck_data[tipo].values())
  i = 0
  beck = {}
  for result in results:  
    beck[i] = preprocesamiento(result)
    i += 1
  beck_data_preprocessing[tipo] = beck

pprint.pprint(beck_data_preprocessing)    
    
    
    