import pandas as pd

from helpers import preprocesamiento

df_prueba = pd.read_csv('../dataset_validacion.csv')
# dato_1 = df_prueba.iloc[27]
dato_1 = df_prueba.iloc[0]
text = dato_1.loc['text']
print(f"Antes:            {text}")
# Preprocesamiento de texto
text = preprocesamiento(text)
print(f"Despues:          {text}")
