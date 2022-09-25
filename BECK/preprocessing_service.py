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
    self.stanza.download('es', package='ancora',
                             processors='tokenize,mwt,pos,lemma', verbose=True)
    self.stNLP = stanza.Pipeline(
      processors='tokenize,mwt,pos,lemma', lang='es', use_gpu=True)
    # Variables globales
    self.dic = hunspell.HunSpell(
            "./Diccionario/es_ANY.dic", "./Diccionario/es_ANY.aff")
    self.sp = spacy.load('es_core_news_md')
    self.all_stopwords = self.sp.Defaults.stop_words

  def preprocesamiento_con_ortografia(self, texto: str) -> list[str]:
    """
    Preprocesamiento
    Función que hace el llamado a otras funciones con el fin de limpiar el texto de entrada.
    :param texto: texto sin procesar
    :return: Texto procesado y limpiado
    """
    # Eliminar etiquetas y hashtags
    texto = self.eliminar_etiquetados(texto)
    texto = self.eliminar_emojis(texto)
    texto = self.eliminacion_data_inutil(texto)
    texto = self.correccion_ortografica(texto)
    texto = self.stop_words(texto)
    texto = self.lematizacion(texto)
    return texto


  def preprocesamiento_sin_ortografia(self, texto: str) -> list[str]:
    """
    Preprocesamiento
    Función que hace el llamado a otras funciones con el fin de limpiar el texto de entrada.
    :param texto: texto sin procesar
    :return: Texto procesado y limpiado
    """
    # Eliminar etiquetas y hashtags
    texto = self.eliminar_etiquetados(texto)
    texto = self.eliminar_emojis(texto)
    texto = self.eliminacion_data_inutil(texto)
    texto = self.stop_words(texto)
    texto = self.lematizacion(texto)
    return texto
  
  def eliminar_etiquetados(self, texto: str) -> str:
    """_summary_

    Args:
      texto (str): Texto con etiquetas "@" y hashtags "#"

    Returns:
      str: Texto sin etiquetas ni hashtags
      """
    texto = texto.split(" ")
    texto_no_etiquetas = []
    for word in texto:
      if not (word.startswith("@") or word.startswith("#")):
        texto_no_etiquetas.append(word)
    texto = " ".join(texto_no_etiquetas)
    return texto

  def eliminar_emojis(self, texto: str) -> str:
    return emoji.replace_emoji(texto, "")

  def eliminacion_data_inutil(self, texto: str) -> str:
    '''
      Esta función limpia y tokeniza el texto en palabras individuales.
      El orden en el que se va limpiando el texto no es arbitrario.
      El listado de signos de puntuación se ha obtenido de: print(string.punctuation)
      y re.escape(string.punctuation)
    '''

    # Se convierte todo el texto a minúsculas
    nuevo_texto = texto.lower()
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


  def stop_words(self, text: str) -> list[str]:
    text_tokens = word_tokenize(text)
    tokens_without_sw = [
      word for word in text_tokens if not word in self.all_stopwords]
    return tokens_without_sw

  def lematizacion(self, words: list[str]) -> list[str]:
    new_words = []
    for word in words:
      result = self.stNLP(word)
      new_words.append(
          [word.lemma for sent in result.sentences for word in sent.words][0])
    return new_words

  def correccion_ortografica(self, texto: str) -> str:
    # Correccion Ortografica
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
