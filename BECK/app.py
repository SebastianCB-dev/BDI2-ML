import json
import pandas as pd
from preprocessing_service import preprocesamiento
from file_service import read_json, read_txt

# Leer información del archivo items.json y de comentariostest
beck_data = json.loads(read_json('./items.json'))
comments_array = list(read_txt('./comentarios_test.txt'))

# Arreglo de las 21 categorias del BDI-II
types = list(beck_data.keys())

# Preprocesamiento
print(' Comentario antes '.center(50, '#'))
print(comments_array[0])
comment1_preprocessing = preprocesamiento(comments_array[0])
print(' Comentario despúes '.center(50, '#'))
print(comment1_preprocessing)
