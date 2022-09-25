## Preprocesamiento de datos
Este es un repositorio dedicado al preprocesamiento de datos en Python usando diferentes librerías.

Lo que se hace:
* stop words removal
* emoji removal
* punctuaction sign removal
* Hashtags and mentions removal

#### Data
Para entrenar mas corpus al modelo
```
model.build_vocab(data)
```

Para cargar el modelo
```
Word2Vec.load('word2vec.model')
```

Para guardar el modelo
```
model.save('word2vec.model')
```