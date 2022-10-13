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

Para distancia de coseno entre dos textos convertidos a arreglos.
```
coseno = model.wv.wmdistance(first_array, second_array)
```

## Citations
Ofir Pele and Michael Werman "A linear time histogram metric for improved SIFT matching" &lt;http://www.cs.huji.ac.il/\~werman/Papers/ECCV2008.pdf&gt;_

Ofir Pele and Michael Werman "Fast and robust earth mover's distances" &lt;https://ieeexplore.ieee.org/document/5459199/&gt;_

Matt Kusner et al. "From Word Embeddings To Document Distances" &lt;http://proceedings.mlr.press/v37/kusnerb15.pdf&gt;