import emoji
import re
from nltk.tokenize import word_tokenize
import spacy
import stanza
import hunspell

class Preprocesamiento:

    # eliminar_etiquetados(texto)
    # eliminar_emojis(texto)
    # eliminacion_data_inutil(texto)
    # correccion(texto)
    # stop_words(texto)
    # lematizacion(texto)

  def __init__(self):
    """
    1. Descarga el modelo en español para la biblioteca Stanford NLP.
    2. Cargue el modelo de idioma español para la biblioteca Stanford NLP.
    3. Cargue el diccionario Hunspell.
    4. Cargue el modelo en español para la biblioteca SpaCy.
    5. Carga las palabras vacías en español
    """

    stanza.download('es', package='ancora',
                             processors='tokenize,mwt,pos,lemma', verbose=True)
    self.stNLP = stanza.Pipeline(
      processors='tokenize,mwt,pos,lemma', lang='es', use_gpu=True)
    # Variables globales
    self.dic = hunspell.HunSpell(
            "./Diccionario/es_ANY.dic", "./Diccionario/es_ANY.aff")
    self.sp = spacy.load('es_core_news_md')
    self.all_stopwords = self.sp.Defaults.stop_words

  def preprocesamiento_con_ortografia(self, texto):
    """
    Toma una cadena, elimina hashtags, emojis y palabras vacías, y devuelve una cadena
    
    :param texto: El texto a ser preprocesado
    :return: El texto está siendo devuelto.
    """

    # Eliminar etiquetas y hashtags
    texto = self.normalizar(texto)
    texto = self.eliminar_etiquetados(texto)
    texto = self.eliminar_emojis(texto)
    texto = self.eliminacion_data_inutil(texto)
    texto = self.correccion_ortografica(texto)
    texto = self.stop_words(texto)
    texto = self.lematizacion(texto)
    #texto = self.eliminar_duplicados(texto)
    return texto


  def preprocesamiento_sin_ortografia(self, texto):
    """
    Preprocesamiento
    Función que hace el llamado a otras funciones con el fin de limpiar el texto de entrada.
    :param texto: texto sin procesar
    :return: Texto procesado y limpiado
    """
    # Eliminar etiquetas y hashtags
    texto = self.normalizar(texto)
    texto = self.eliminar_etiquetados(texto)
    texto = self.eliminar_emojis(texto)
    texto = self.eliminacion_data_inutil(texto)
    texto = self.stop_words(texto)
    texto = self.lematizacion(texto)
    #texto = self.eliminar_duplicados(texto)
    return texto
  
  def eliminar_etiquetados(self, texto):
    """
    Toma una cadena, la divide en una lista de palabras y luego vuelve a unir la lista en una cadena,
    pero solo si la palabra no comienza con @ o #
    
    :param texto: El texto a limpiar
    :return: el texto sin las etiquetas.
    """
    texto = texto.split(" ")
    texto_no_etiquetas = []
    for word in texto:
      if not (word.startswith("@") or word.startswith("#")):
        texto_no_etiquetas.append(word)
    texto = " ".join(texto_no_etiquetas)
    return texto

  def eliminar_emojis(self, texto):
    """
    > Toma un string y elimina los emojis
    
    :param texto: str
    :type texto: str
    :return: una cadena sin emojis.
    """
    return emoji.replace_emoji(texto, "")

  def eliminacion_data_inutil(self, texto):
    '''
      Esta función limpia y tokeniza el texto en palabras individuales.
      El orden en el que se va limpiando el texto no es arbitrario.
      El listado de signos de puntuación se ha obtenido de: print(string.punctuation)
      y re.escape(string.punctuation)
    '''
    nuevo_texto = texto
    # Eliminación de páginas web (palabras que empiezan por "http")
    nuevo_texto = re.sub('http\S+', ' ', nuevo_texto)
    # Eliminación de signos de puntuación
    regex = '[\\!\\"\\#\\$\\%\\&\\\'\\(\\)\\*\\+\\,\\-\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~\\¿\\¡\\”]'
    nuevo_texto = re.sub(regex, ' ', nuevo_texto)
    # Eliminación de números
    nuevo_texto = re.sub("\d+", ' ', nuevo_texto)
    # Eliminación de espacios en blanco múltiples
    nuevo_texto = re.sub("\\s+", ' ', nuevo_texto)
    # Tokenización por palabras individuales
    nuevo_texto = nuevo_texto.split(sep=' ')
    return " ".join(nuevo_texto)


  def stop_words(self, text):
    """
    Toma una cadena de texto, la tokeniza y luego elimina todas las palabras vacías
    
    :param text: El texto a procesar
    :return: Una lista de palabras que no son palabras vacías.
    """
    text_tokens = word_tokenize(text)
    tokens_without_sw = [
      word for word in text_tokens if not word in self.all_stopwords]
    return tokens_without_sw

  def lematizacion(self, words):
    """
    1. Toma una lista de palabras como entrada.
    2. Luego itera sobre cada palabra en la lista.
    3. Para cada palabra, llama a la función stNLP, que devuelve una lista de lemas.
    4. Luego agrega el primer lema de la lista a una nueva lista.
    5. Devuelve la nueva lista.
    
    :param words: La lista de palabras a lematizar
    :return: Una lista de lemas
    """
    new_words = []
    for word in words:
      result = self.stNLP(word)
      new_words.append(
          [word.lemma for sent in result.sentences for word in sent.words][0])
    return new_words

  def correccion_ortografica(self, texto):    
    # Una función que corrige la ortografía de una palabra.
    arr = texto.split(" ")
    result = ""
    for palabra in arr:
      res = self.dic.spell(palabra)
      if not res:
        try:
          res = self.dic.suggest(palabra)[0]
        except Exception:
          res = palabra
      else:
        res = palabra
      result += res + " "
    result = result.strip()
    return result

  def normalizar(self, texto):
    """
    1. Toma texto como entrada.
    2. Convierte el texto a minusculas.
    3. Reemplaza las letras con tildes por letras normales.

    :param words: Texto a convertir
    :return: Texto transformado
    """
    texto = texto.lower()

    texto = re.sub('á', 'a', texto)
    texto = re.sub('é', 'e', texto)
    texto = re.sub('í', 'i', texto)
    texto = re.sub('ó', 'o', texto)
    texto = re.sub('ú', 'u', texto)
    texto = re.sub('ü', 'u', texto)
    texto = re.sub('ñ', 'n', texto)

    return texto

  def eliminar_duplicados(self, lista):
    return list(set(lista))
