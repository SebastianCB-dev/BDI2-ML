from pprint import pprint
from gensim.models import Word2Vec
import numpy as np
import json
class ModelWord2Vec:

  def __init__(self):
    """
    Esta función carga el modelo Word2Vec de depresión.
    """
    self.model = Word2Vec.load('./depresion.model')

  def get_beck(self):
    """
    Abre el archivo JSON de los items del BECK vectorizados, lo lee y devuelve los datos del archivo JSON en un diccionario de Python
    :return: Un diccionario de diccionarios.
    """
    beck_data_preprocessing = {}
    try:
        if open('./JSON/items_preprocessing.json', 'r'):
            beck_data_preprocessing = json.loads(
                open('./JSON/items_preprocessing.json', 'r', encoding='utf-8').read())
    except Exception as e:
      print(f'Error: {e}')
    return beck_data_preprocessing

  def get_model(self):
    """
    Retorna el Word Embedding.
    :return: modelo Word2Vec de depresión.
    """
    return self.model
  
  def add_corpus(self, corpus):
    """
    > La función toma un corpus como entrada, lo agrega al modelo existente y guarda el modelo actualizado.
    
    :param corpus: El corpus es una lista de listas. Cada lista es un documento. Cada documento es una lista de palabras
    """
    corpus = [corpus]
    self.model.build_vocab(corpus, update=True)
    self.save_model()

  def save_model(self):
    """
    Toma el modelo, y lo guarda como un archivo llamado 'depresion.model'
    """
    self.model.save('depresion.model')

  def get_cosine_similarity(self, corpus_a, corpus_b):
    """
    > La función toma dos listas de palabras como entrada y devuelve la similitud del coseno entre las dos listas
    
    :param corpus_a: una lista de palabras
    :param corpus_b: El corpus con el que comparar
    :return: La similitud del coseno entre los dos documentos.
    """
    return self.model.wv.n_similarity(corpus_a, corpus_b)

  def get_word_vectors(self, corpus):
    """
    Devuelve los vectores de palabras para las palabras del corpus.
    
    :param corpus: El corpus es la lista de palabras para las que desea obtener los vectores
    :return: Los vectores de palabras para cada palabra en el corpus.
    """
    array_result = []
    for word in corpus:
      try:
        array_result.append(self.model.wv[word])
      except Exception as e:
        return self.getVector250()
    return array_result

  def get_cosine_similarity_BECK(self, corpus):
    """
    Esta función toma un corpus y devuelve una lista de similitudes de coseno entre el corpus y cada uno de los resultador del inventario de depresión de BECK (BDI-II) 90 resultados.
    
    :param corpus: el texto que desea comparar con el corpus BECK
    :return: Una lista de similitudes de coseno entre el corpus y los datos de BECK.
    """
    self.add_corpus(corpus)
    beck = self.get_beck()
    data = []
    for item in beck.keys():
      for result in beck[item].keys():
        similarity = self.get_cosine_similarity(corpus, beck[item][result]["data"])
        data.append(similarity)
    return data    

  def get_result_beck(self, cosine_similarities):
    """
    Toma las similitudes del coseno y devuelve los resultados de la encuesta llenada en una lista plana.
    
    :param cosine_similarities: las similitudes de coseno entre la consulta y los documentos
    :return: Los resultados se devuelven como una lista de listas.
    """
    results = []
    primera_parte = cosine_similarities[:60]  # 4 respuestas
    segunda_parte = cosine_similarities[60:67]  # 7 respuestas
    tercera_parte = cosine_similarities[67:71]  # 4 respuestas
    cuarta_parte = cosine_similarities[71:78]  # 7 respuestas
    quinta_parte = cosine_similarities[78:]  # 4 respuestas
    results.append(self.getMaxBeck4Items(primera_parte))
    results.append(self.getMaxBeck7Items(segunda_parte))
    results.append(self.getMaxBeck4Items(tercera_parte))
    results.append(self.getMaxBeck7Items(cuarta_parte))
    results.append(self.getMaxBeck4Items(quinta_parte))
    results_flat = [x for sublist in results for x in sublist]
    return results_flat

  def getMaxBeck4Items(self, array):
    """
    Toma una matriz de números y devuelve una matriz del índice del número más grande en cada grupo de 4
    
    :param array: la matriz de números a procesar
    :return: El índice del valor máximo en cada grupo de 4 elementos.
    """
    results = []
    for index in range(0, len(array), 4):
      item = array[index: index + 4]
      mayor = 0
      mayor_idx = 0
      for index, result in enumerate(item):
        if result > mayor:
          mayor = result
          mayor_idx = index
      results.append(mayor_idx)
    return results

  def getMaxBeck7Items(self, array):
    """
    Toma una matriz de números y devuelve una matriz de números.
    
    :param array: el conjunto de resultados del inventario de depresión de beck
    :return: el valor máximo de cada grupo de 7 artículos.
    """
    results_beck = [0, 1, 1, 2, 2, 3, 3]
    results = []
    for index in range(0, len(array), 7):
      item = array[index: index + 7]
      mayor = 0
      mayor_idx = 0
      for index, result in enumerate(item):
        if result > mayor:
          mayor = result
          mayor_idx = results_beck[index]
      results.append(mayor_idx)
    return results

  def getVector250(self):
    """
    Devuelve una lista de 250 ceros.
    :return: Una lista de 250 ceros.
    """
    return list(np.zeros(250))
