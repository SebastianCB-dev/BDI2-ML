from preprocessing_service import Preprocesamiento
from model_word2vec_service import ModelWord2Vec
import joblib

pp = Preprocesamiento()
w2v = ModelWord2Vec()
clf = joblib.load('./models/logistic_regression.pkl')

comentario = "Estoy muy triste y no se que hacer"
# Escribe un comentario triste y largo
comentario = "Estoy muy triste y no se que hacer es un día nublado y esta lloviendo"
# Preprocesado del comentario
comentario_procesado = pp.preprocesamiento_con_ortografia(comentario)
# Obtener la similitud de coseno entre el comentario y 
# Cada una de las respuestas del inventario de depresión de BECK (BDI-II)
cosine_similarity_beck = w2v.get_cosine_similarity_BECK(comentario_procesado)
# Obtener la respuesta por item basandose en la similitud de coseno
results_beck = w2v.get_result_beck(cosine_similarity_beck)
print("El comentario lleno el inventario BECK de esta manera:", results_beck)

print('Predicción:', clf.predict([results_beck]))
