from collections import defaultdict
from gensim import corpora

def word_space(data: list[str]):
  dictionary = corpora.Dictionary(data)
  return dictionary