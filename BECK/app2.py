import json
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
import operator
#txt call with open tool
comentarios= list(open('comentarios_test.txt', 'r', encoding='utf-8').readlines())
beck_data_preprocessing = {}
#json with preprocessing items
try:
  if open('./JSON/items_preprocessing.json', 'r'):
    beck_data_preprocessing = json.loads(open('./JSON/items_preprocessing.json', 'r', encoding='utf-8').read())
except Exception as e:
  print(f'Error: {e}')
#first comment call is necesary a coma
lista= comentarios[0],
print(lista)
#route in beck dict and key(Tristeza call)
for key in beck_data_preprocessing.keys():
    #Tristeza values
    for items in beck_data_preprocessing["Tristeza"].values():
        coment_compar= items["data"]
        print(coment_compar)
        valor = items["value"]
        vectorizer = CountVectorizer()
        #This method performs fit and transform on the input data at a single time and converts the data points.
        insta_coment = vectorizer.fit_transform(lista).todense()
        feature = vectorizer.fit_transform(coment_compar).todense()
        beck_coment = np.concatenate((feature), axis=1)
        diferencia = -(insta_coment.size - beck_coment.size)
        print(diferencia)
        if(insta_coment.size<beck_coment.size):
            [*lista]
        print(type(lista))

        print(insta_coment.size)
        print(beck_coment.size)



        print("Comentario insta",insta_coment[0])
        print("Comentario Beck ",beck_coment[0])


        #print(vectorizer.vocabulary_)
        for beck in  insta_coment:
            print(euclidean_distances(beck, beck_coment[0]))

