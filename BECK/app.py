import json
import pandas as pd
from preprocessing_service import preprocesamiento
from embeddings import word_space
from preprocessing_service import preprocesamiento_no_ortografia
from file_service import read_json, read_txt
import gensim as gensim
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

# pprint.pprint(beck_data_preprocessing)    

# !Vector Space Embedding

df_entrenamiento = pd.read_csv('./datasets/dataset_entrenamiento.csv')
comments_array = list(df_entrenamiento['text'])
i = 1
comments_array_preprocessing = []
print(comments_array[6209])
for comment in comments_array:
  print(f'Preprocessing comment: {i}/7096')
  comment = ''
  try:
    comment = preprocesamiento_no_ortografia(comment)
    comments_array_preprocessing.append(comment)
  except Exception as e:
    pass
  i += 1

dictionary = word_space(comments_array_preprocessing)
gensim.corpora.dictionary.Dictionary.save(dictionary, './myModel.sav')
comment = 'a'
while (comment != '0'):
  comment = input('Ingrese el texto: ')
  result = dictionary.doc2bow(preprocesamiento(comment))
  print('El vector es:', result)
