import pandas as pd
import nltk
nltk.download('punkt')
from preprocessing_service import Preprocesamiento
from gensim.models import Word2Vec

df_positivo = pd.read_csv('./comentarios_español_depresivos.csv', encoding='utf-8')
df_negativo = pd.read_csv('./comentarios_español_no_depresivos.csv', encoding='utf-8')
pp = Preprocesamiento()
tokens = []

comentarios_depresivos = list(df_positivo['text'])
clases_depresivos = list(df_positivo['class'])



# Entrenamiento
# vector size = 200 dimensiones
# window = Ventana referente a las palabras siguientes 
# For example "stackoverflow great website for programmers" with 5 words(suppose we save the stop words great and for here) if the window size is 2 then the vector of word "stackoverflow" is directly affected by the word "great" and "website", if the window size is 5 "stackoverflow" can be directly affected by two more words "for" and "programmers". The 'affected' here means it will pull the vector of two words closer.


model = Word2Vec(sentences=tokens, vector_size=200,
                 window=7, workers=4, sg=1, epochs=20)
