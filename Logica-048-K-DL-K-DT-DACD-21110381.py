#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# Datos de ejemplo
X_train = ["I love this movie", "This movie is terrible", "This movie is great", "I hate this movie"]
y_train = [1, 0, 1, 0]  # 1 para positivo, 0 para negativo

# Crear un modelo K-DL usando Logistic Regression
model_k_dl = make_pipeline(CountVectorizer(), LogisticRegression())

# Entrenar el modelo
model_k_dl.fit(X_train, y_train)

# Ejemplo de predicción
X_test = ["This movie is fantastic"]
predictions_k_dl = model_k_dl.predict(X_test)
print("Predicciones K-DL:", predictions_k_dl)

