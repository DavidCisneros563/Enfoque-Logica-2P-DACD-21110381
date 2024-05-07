#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import shap
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Cargar conjunto de datos de ejemplo (Boston Housing)
data = load_boston()
X, y = data.data, data.target
feature_names = data.feature_names

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo de regresión aleatoria (Random Forest)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Calcular SHAP values para explicar las predicciones en el conjunto de prueba
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

# Imprimir las explicaciones para una instancia de prueba específica
instance_idx = 0
print("Explicación para la instancia de prueba", instance_idx)
shap.summary_plot(shap_values[instance_idx], features=X_test[instance_idx], feature_names=feature_names)