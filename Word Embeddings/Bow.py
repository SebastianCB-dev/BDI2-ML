
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def otrafuncion(vector):
    comentario = ' '.join([vector])
    print(comentario)
    comentario = ''
    for i in vector:
        comentario = ' '.join(i)
        Contador = CountVectorizer(ngram_range=(1, 1), )
        Count_data = Contador.fit_transform([comentario, ])
        print(Count_data)
        cv_dataframe = pd.DataFrame(Count_data.toarray(), columns=Contador.get_feature_names())
        print(cv_dataframe)


def Embeding(lista_comentarios):
    vector = []
    for comentario in lista_comentarios:
            vector.append(comentario.split())


    otrafuncion(vector)



try:
    archivo = open('comentarios.txt', 'r',encoding='utf8')
    Embeding(archivo.readlines())

except Exception as e:
    print(e)
finally :
    pass

