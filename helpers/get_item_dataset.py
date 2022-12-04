import pandas as pd
import numpy as np
df = pd.read_csv('./comentarios_coseno_distancia', encoding='utf-8')
df_coseno = pd.read_csv(
    'drive/MyDrive/word_embedding_spanish/dataset_entrenamiento_coseno.csv', encoding='utf-8', delimiter=';')
array = []
items = list(df_coseno.columns)
classes = list(df['Clase'])
items_raros = [0, 1, 1, 2, 2, 3, 3]
comment_count = 0
for i in range(0, len(df.index)):
  comment = list(df.copy().iloc[i])[2:][:-1]
  normal = list(
      np.array(comment.copy()[:60] + comment.copy()[67:71] + comment.copy()[78:]))
  special = list(np.array(comment.copy()[60:67] + comment.copy()[71:78]))
  comment_data = {}
  item_count = 0
  for index in range(0, len(normal), 4):
    item = normal[index: index + 4]
    mayor = 0
    mayor_idx = 0
    # print(item)
    for index, result in enumerate(item):
      if result > mayor:
        mayor = result
        mayor_idx = index
    comment_data[items[item_count]] = mayor_idx
    item_count += 1
  for index2 in range(0, len(special), 7):
    item2 = special[index2: index2 + 7]
    mayor2 = 0
    mayor_idx2 = 0
    for index2, result2 in enumerate(item2):
      if result2 > mayor2:
        mayor2 = result2
        mayor_idx2 = index2
    comment_data[items[item_count]] = items_raros[mayor_idx2]
    item_count += 1
  comment_data['Clase'] = classes[comment_count]
  comment_count += 1
  df_coseno = df_coseno.append(comment_data, ignore_index=True)
df_coseno.to_csv('dataset_entrenamiento.csv', index=False, encoding="utf-8")
