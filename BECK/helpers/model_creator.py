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
comentarios_no_depresivos = list(df_negativo['text'])

count = 1
for comentario in comentarios_depresivos:
  print(f'Preprocesando comentario: {count}/{len(comentarios_depresivos) + len(comentarios_no_depresivos)}')
  try:
    comentario_preprocesado = pp.preprocesamiento_sin_ortografia(comentario)
    tokens.append(comentario_preprocesado)
    count += 1
  except Exception as e:
    print(
        f'Error preprocesando el comentario {count}/{len(comentarios_depresivos) + len(comentarios_no_depresivos)}')
    count += 1
    continue
    

for comentario in comentarios_no_depresivos:
  print(
      f'Preprocesando comentario: {count}/{len(comentarios_depresivos) + len(comentarios_no_depresivos)}')
  try:
    comentario_preprocesado = pp.preprocesamiento_sin_ortografia(comentario)
    tokens.append(comentario_preprocesado)
  except Exception as e:
    print(
        f'Error preprocesando el comentario {count}/{len(comentarios_depresivos) + len(comentarios_no_depresivos)}')
    count += 1
    continue

model = Word2Vec(sentences=tokens, vector_size=200,
                 window=7, workers=4, sg=1, epochs=20)

model.save('depresion.model')