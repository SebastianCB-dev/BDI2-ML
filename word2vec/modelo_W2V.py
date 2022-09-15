#!/usr/bin/env python
# coding: utf-8

# # Crear un modelo de Word2Vec

import nltk
import gensim


# cargar el documento
with open ('data/reglamento_transito.txt',
           'r',encoding='utf-8') as file:
        document = file.read()

document[:1000]

# tokenizar el documento en oraciones
sentences = nltk.sent_tokenize(document)
sentences[1]

#tokenizar cada oracion en palbras
word_tokens = [nltk.tokenize.word_tokenize(sentence.lower()) for sentence in sentences]

#Entrenar el modelo de Word2Vec
modelo_w2v = gensim.models.Word2Vec(sentences = word_tokens,
                                    size = 50,
                                    iter=100,
                                    min_count=1)

#Obtener las 10 palabras mas similares
modelo_w2v.most_similar('auto')

#Vector de cada palabra
modelo_w2v['auto']
