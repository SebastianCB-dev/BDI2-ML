import pandas as pd
import nltk
nltk.download('punkt')
from preprocessing_service import Preprocesamiento

df = pd.read_csv('./comentarios_español_depresivos.csv', encoding='utf-8')
pp = Preprocesamiento()

comentarios = list(df['text'])
clases = list(df['class'])

print('-- Comentario antes --')
print(comentarios[0])
print('-- Comentario despúes --')
comentario_preprocesado = pp.preprocesamiento_sin_ortografia(comentarios[0])
print(comentario_preprocesado)