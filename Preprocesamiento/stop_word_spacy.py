from nltk.tokenize import word_tokenize
import spacy
from nltk.corpus import stopwords

sp = spacy.load('es_core_news_md')

all_stopwords = sp.Defaults.stop_words

text = "....El suicidio es definitivo mientras que el problema que atraviesas es temporal” 🙏🏽"
text_tokens = word_tokenize(text)
tokens_without_sw= [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)
