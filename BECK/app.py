import json
import pandas as pd

def getTypes(data): 
  types = []
  types.append("text")
  for i in data.keys():
      if not data[i]["tipo"] in types:
        types.append(data[i]["tipo"])
  return types

def getDict(types):
  dictionary = {}
  count = 1
  dictionary["text"] = "....El suicidio es definitivo mientras que el problema que atraviesas es temporal” 🙏🏽"
  for i in types:
    if not i == "text":
      dictionary[i] = count
      count += 1
  return dictionary

data_file = open('./items.json', 'r', encoding='utf8')

beck_data = json.loads(data_file.read())
types = getTypes(beck_data)

print("La cantidad de tipos son:", len(types))
print("La cantidad de items son: ", len(beck_data))

dictionary = getDict(types)
df_comments = pd.DataFrame(data=dictionary, columns=types, index=[1])
print(df_comments)