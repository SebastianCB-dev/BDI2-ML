from preprocessing_service import preprocesamiento_no_ortografia
from preprocessing_service import preprocesamiento

comments_array = open('./comentarios_test.txt', 'r').readlines()[0:7]

print(comments_array)

print(" COMENTARIOS ANTES ".center(60, "="))
for comment in comments_array:
  print(comment)

print("COMENTARIOS PREPROCESADOS CON ORTOGRAFÍA ".center(60, "="))
for comment in comments_array:
  print(preprocesamiento(comment))

print("COMENTARIOS PREPROCESADOS SIN ORTOGRAFÍA ".center(60, "="))
for comment in comments_array:
  print(preprocesamiento_no_ortografia(comment))