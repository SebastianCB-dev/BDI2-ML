from pprint import pprint
from gensim.models import Word2Vec
import numpy as np
import json
class ModelWord2Vec:

  def __init__(self):
    """
    La función toma una lista de palabras y devuelve una lista de vectores.
    """
    self.model = Word2Vec.load('./depresion.model')

  def get_beck(self):
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
    me devuelve el modelo
    :return: El modelo está siendo devuelto.
    """
    return self.model
  
  def add_corpus(self, corpus):
    """
    > La función toma un corpus (una lista de palabras) y lo agrega al modelo
    
    :param corpus: El corpus es una lista de listas. Cada lista es un documento. Cada documento es una
    lista de palabras
    """
    corpus = [corpus]
    self.model.build_vocab(corpus, update=True)
    self.save_model()

  def save_model(self):
    """
    Esta funcion guarda el modelo
    """
    self.model.save('depresion.model')

  def get_cosine_similarity(self, corpus_a, corpus_b):
    """
    La función toma dos cadenas como entrada y devuelve la distancia del coseno entre las dos cadenas.
    
    :param corpus_a: El primer corpus a comparar
    :param corpus_b: El corpus para comparar con el corpus_a corpus
    :return: La distancia del coseno entre los dos corpus.
    """
    return self.model.wv.n_similarity(corpus_a, corpus_b)

  def get_word_vectors(self, corpus):
    """
    > La función toma una list de palabras como entrada y devuelve el vector de 250D para esa palabra
    
    :param word: La palabra cuya representación vectorial desea obtener
    :return: La palabra vector para la palabra.
    """
    array_result = []
    for word in corpus:
      try:
        array_result.append(self.model.wv[word])
      except Exception as e:
        return self.getVector250()
    return array_result

  def get_cosine_similarity_BECK(self, corpus):
    self.add_corpus(corpus)
    beck = self.get_beck()
    data = []
    for item in beck.keys():
      for result in beck[item].keys():
        similarity = self.get_cosine_similarity(corpus, beck[item][result]["data"])
        data.append(similarity)
    
    return data    

  def get_result_beck(self, cosine_similarities):
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
    return list(np.zeros(250))
