import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

text1 = ['esto', 'no', 'me' ,'gustar', 'verde', 'caca.']
text2 = ['esto', 'no', 'me' ,'gustar', 'verde', 'caca.']

vector1 = text_to_vector(' '.join(text1))
vector2 = text_to_vector(' '.join(text2))

cosine = get_cosine(vector1, vector2)

print('Cosine:', cosine)