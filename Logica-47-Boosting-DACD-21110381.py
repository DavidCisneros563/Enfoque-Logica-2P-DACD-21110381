#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generar datos sintéticos
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador de Boosting
clf = AdaBoostClassifier(n_estimators=50, random_state=42)

# Entrenar el clasificador
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del clasificador
precision = accuracy_score(y_test, y_pred)
print("Precisión del clasificador de Boosting:", precision)
