from gensim.models import Word2Vec
import numpy as np

class ModelWord2Vec:

  def __init__(self):
    self.model = Word2Vec.load('word2vec.model')

  def get_model(self):
    return self.model
  
  def add_corpus(self, corpus: list[str]):
    corpus = [corpus]
    self.model.build_vocab(corpus, update=True)
    self.save_model()

  def save_model(self):
    self.model.save('word2vec.model')

  def get_euclidian_distance(self, corpus_a, corpus_b):
    return np.linalg.norm(self.model.wv[corpus_a] - self.model.wv[corpus_b])

  def get_cosine_distance(self, corpus_a, corpus_b):
    return self.model.wv.wmdistance(corpus_a, corpus_b)

  def get_word_vector(self, word):
    return self.model.wv[word]