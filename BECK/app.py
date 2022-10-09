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

# Get Vector Beck
result = w2v.getVectorBeck(comment_test, beck_data_preprocessing)
print(result)
