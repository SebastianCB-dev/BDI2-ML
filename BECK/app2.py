import json
import pandas as pd
from gensim.models import Word2Vec
import numpy as np
import operator
#from preprocessing_service import Preprocesamiento
#txt call with open tool
comentarios= list(open('comentarios_test.txt', 'r', encoding='utf-8').readlines())
beck_data_preprocessing = {}
#json with preprocessing items
try:
  if open('./JSON/items_preprocessing.json', 'r'):
    beck_data_preprocessing = json.loads(open('./JSON/items_preprocessing.json', 'r', encoding='utf-8').read())
except Exception as e:
  print(f'Error: {e}')

modelo = Word2Vec.load('word2vec.model')
#preprocesamiento = Preprocesamiento()
print(modelo)
#comment_test = preprocesamiento.preprocesamiento_con_ortografia(comentarios[0])
comment_test = np.array(comentarios[0].split())
print(comment_test)
hola =np.array([1,2,5,3,3,3,3])

perro=np.array([3,4,3,3,2,3,3])
distancia = np.linalg.norm(hola - perro)
print("sss",distancia)
for key in beck_data_preprocessing.keys():
    #Tristeza values
    for items in beck_data_preprocessing["Tristeza"].values():
        coment_compar= np.array(items["data"])
        #print(coment_compar)
        valor = items["value"]
        #distancia = modelo.wv(np.linalg.norm(hola - perro))
        #distancia= modelo.wv(np.linalg.norm(  comment_test -coment_compar ))
        print(distancia)

import numpy as np

# initializing points in
# numpy arrays
point1 = np.array((1, 2, 3))
point2 = np.array((1, 1, 1))

# calculating Euclidean distance
# using linalg.norm()
dist = np.linalg.norm(point1 - point2)

# printing Euclidean distance
#print(dist)



#first comment call is necesary a coma
"""
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


        print(insta_coment.size)
        print(beck_coment.size)



        print("Comentario insta",insta_coment[0])
        print("Comentario Beck ",beck_coment[0])


        #print(vectorizer.vocabulary_)
        for beck in  insta_coment:
            print(euclidean_distances(beck, beck_coment[0]))
"""
