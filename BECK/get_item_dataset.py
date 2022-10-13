from cmath import inf
import pandas as pd
from pprint import pprint

df = pd.read_csv('./datasets/coseno_vs_euclidian.csv')
values_items_largos = [0, 1, 1, 2, 2, 3, 3]
df_results = pd.read_csv('./results.csv')
classes = list(df['Clase'])
class_idx = 0
columns = list(df_results.columns)[2:]
for i in range(0, 7068):
  column = 0
  comment = list(df.iloc[i])
  result = {}
  result['Comentario'] = comment[0]
  result['Comentario Preprocesado'] = comment[1]
  rest_comment = comment[-29:-1]
  comment = comment[2:-29]
  for i in range(0, len(comment), 8):
    data = comment[i:(i+8)]
    # Euclidian
    menor_euclidian = inf
    menor_euclidian_idx = 0
    #Coseno
    menor_coseno = inf
    menor_coseno_idx = 0
    # Coseno
    for idx, i2 in enumerate(range(0, len(data), 2)):
      if data[i2] < menor_coseno:
        menor_coseno = data[i2]
        menor_coseno_idx = idx
    # Euclidian
    for idx, i3 in enumerate(range(1, len(data), 2)):
      if data[i3] < menor_euclidian:
        menor_euclidian = data[i3]
        menor_euclidian_idx = idx
    result[columns[column]] = menor_coseno_idx
    column += 1
    result[columns[column]] = menor_euclidian_idx
    column += 1
  # Anormal items
  for i in range(0, len(rest_comment), 14):
    data = rest_comment[i:(i+14)]
    # Euclidian
    menor_euclidian = inf
    menor_euclidian_idx = 0
    #Coseno
    menor_coseno = inf
    menor_coseno_idx = 0
    # Coseno
    for idx, i2 in enumerate(range(0, len(data), 2)):
      if data[i2] < menor_coseno:
        menor_coseno = data[i2]
        menor_coseno_idx = idx
    # Euclidian
    for idx, i3 in enumerate(range(1, len(data), 2)):
      if data[i3] < menor_euclidian:
        menor_euclidian = data[i3]
        menor_euclidian_idx = idx
    result[columns[column]] = values_items_largos[menor_coseno_idx]
    column += 1
    result[columns[column]] = values_items_largos[menor_euclidian_idx]
    column += 1

  result['Clase'] = classes[class_idx]
  class_idx += 1
  df_results = df_results.append(result, ignore_index=True)


df_results.to_csv('results_coseno_euclidian.csv', index=False)