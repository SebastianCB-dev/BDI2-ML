import pandas as pd

df_completo = pd.read_csv(
    './comentarios_coseno_distancia.csv', encoding='utf-8', low_memory=False)
df_comentarios = pd.read_csv(
    './datasets/comentarios_full.csv', encoding='utf-8', low_memory=False)
for i in range(0, len(df_completo['Comentario'].index)):
    # for i in range(0, 3):
    print(i)
    clase = df_comentarios[df_comentarios['text'] ==
                           df_completo.iloc[i]['Comentario']]['class']
    df_completo.at[i, 'Clase'] = clase.iloc[0]

df_completo.to_csv('./comentarios_coseno_distancia.csv',
                   encoding='utf-8', index=False)
