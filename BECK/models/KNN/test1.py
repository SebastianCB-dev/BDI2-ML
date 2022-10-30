import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, f1_score
def train_val_test_split(df, rstate=42, shuffle=True, stratify=None):
    strat = df[stratify] if stratify else None
    train_set, test_set = train_test_split(
        df, test_size=0.25, random_state=rstate, shuffle=shuffle, stratify=strat)
    strat = test_set[stratify] if stratify else None
    val_set, test_set = train_test_split(
        test_set, test_size=0.5, random_state=rstate, shuffle=shuffle, stratify=strat)
    return (train_set, val_set, test_set)
df = pd.read_csv('../datasets/dataset_entrenamiento_coseno.csv')

train_set, val_set, test_set = train_val_test_split(
    df, stratify='Clase')

x_train = train_set.drop(labels='Clase', axis=1)
y_train = train_set['Clase']
x_test = test_set.drop(labels='Clase', axis=1)
y_test = test_set['Clase']
x_val = val_set.drop(labels='Clase', axis=1)
y_val = val_set['Clase']
print(train_set['Clase'].value_counts())
print('################################')
print(val_set['Clase'].value_counts())
print('################################')
print(test_set['Clase'].value_counts())
print("Longitud del Training Set:", len(train_set))
print("Longitud del Validation Set:", len(val_set))
print("Longitud del Test Set:", len(test_set))

#? KNN
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)

#Test
print(' TEST '.center(50, '#'))
y_pred = classifier.predict(x_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(f1_score(y_test, y_pred))

print(' VALIDATION '.center(50, '#'))
y_pred2 = classifier.predict(x_val)
print(classification_report(y_val, y_pred2))
print(confusion_matrix(y_val, y_pred2))
print(f1_score(y_val, y_pred2))
