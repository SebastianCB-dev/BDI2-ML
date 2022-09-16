import logging
from helpers import getText
from pprint import pprint  # pretty-printer
from collections import defaultdict
from gensim import corpora

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Get Documents
documents = getText()

# NLP
stoplist = set('for a of the and to in'.split())
texts = [
    [word for word in document.lower().split() if word not in stoplist]
    for document in documents
]

# remove words that appear only once
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [
    [token for token in text if frequency[token] > 1]
    for text in texts
]

# Create dictionary
dictionary = corpora.Dictionary(texts)
# store the dictionary, for future reference
dictionary.save('/tmp/deerwester.dict')


# Update dictionary
# TODO: dictionary.add_documents()

pprint(dictionary.token2id) # Devuelve el diccionario con el id de cada palabra


# Convert tokenized documents to vectors
new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
# the word "interaction" does not appear in the dictionary and is ignored
# print(new_vec) # [(0, 1), (1, 1)]


corpus = [dictionary.doc2bow(text) for text in texts]
# store to disk, for later use
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus)
print(corpus)
