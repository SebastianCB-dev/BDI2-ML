import hunspell

dic = hunspell.HunSpell("./Diccionario/es_ANY.dic", "./Diccionario/es_ANY.aff")

text = 'Mi padre prefiere que aubiera muerto envés de aver nacido 😭'

text_array = text.split(' ')

result = ""
for palabra in text_array:
    res = dic.spell(palabra)
    if not res:
      try:
        print("*", palabra)
        print(dic.suggest(palabra))
        res = dic.suggest(palabra)[0]
      except Exception:
        res = palabra
    else:
      res = palabra
    result += res + " "
result = result.strip()

print(result)