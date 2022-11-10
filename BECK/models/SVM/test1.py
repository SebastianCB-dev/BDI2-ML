from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, f1_score, accuracy_score, precision_score, recall_score
def train_val_test_split(df, rstate=42, shuffle=True, stratify=None):
    strat = df[stratify] if stratify else None
    train_set, test_set = train_test_split(
        df, test_size=0.25, random_state=rstate, shuffle=shuffle, stratify=strat)
    strat = test_set[stratify] if stratify else None
    val_set, test_set = train_test_split(
        test_set, test_size=0.5, random_state=rstate, shuffle=shuffle, stratify=strat)
    return (train_set, val_set, test_set)


df = pd.read_csv('../../dataset_entrenamiento.csv')
train_set, val_set, test_set = train_val_test_split(
    df, stratify='Clase')
x_train = train_set.drop(labels='Clase', axis=1)
y_train = train_set['Clase']
x_test = test_set.drop(labels='Clase', axis=1)
y_test = test_set['Clase']
x_val = val_set.drop(labels='Clase', axis=1)
y_val = val_set['Clase']


train_set, val_set, test_set = train_val_test_split(
    df, stratify='Clase')

svm_clf = SVC(kernel="linear", degree=3, coef0=10, C=20, probability=True)
svm_clf.fit(x_train, y_train)

#Test
print(' TEST '.center(50, '#'))
y_pred = svm_clf.predict(x_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print('F1_Score: ', f1_score(y_test, y_pred))
print('Precision: ', precision_score(y_test, y_pred))
print('Accuracy: ', accuracy_score(y_test, y_pred))
print('Recall: ', recall_score(y_test, y_pred))

#Validation
print(' VALIDATION '.center(50, '#'))
y_pred2 = svm_clf.predict(x_val)
print(classification_report(y_val, y_pred2))
print(confusion_matrix(y_val, y_pred2))
print('F1_Score: ', f1_score(y_val, y_pred2))
print('Precision: ', precision_score(y_val, y_pred2))
print('Accuracy: ', accuracy_score(y_val, y_pred2))
print('Recall: ', recall_score(y_val, y_pred2))