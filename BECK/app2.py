import json
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
comentarios= list(open('comentarios_test.txt', 'r', encoding='utf-8').readlines())
beck_data_preprocessing = {}
try:
  if open('./JSON/items_preprocessing.json', 'r'):
    beck_data_preprocessing = json.loads(open('./JSON/items_preprocessing.json', 'r', encoding='utf-8').read())
except Exception as e:
  print(f'Error: {e}')

lista= comentarios[0],
print(lista)

for key in beck_data_preprocessing.keys():
    for llave in beck_data_preprocessing["Tristeza"].values():
        coment_compar= llave["data"]
        print(coment_compar)
        valor = llave["value"]
        vectorizer = CountVectorizer()
        features = vectorizer.fit_transform(lista).todense()
        features2 = vectorizer.fit_transform(coment_compar).todense()
        print(features)
        print(features2)
        print(euclidean_distances(features[0], features2[0]))
        #print(vectorizer.vocabulary_)
        for f in features:
            pass
            #print("fff",f)
            #print("ggg",features[0])
            #print( euclidean_distances(features[0], f) )
        # print(euclidean_distances(comentarios1[0],f))
