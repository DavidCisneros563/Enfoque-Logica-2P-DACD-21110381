#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Datos de entrada y salida de ejemplo
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [1], [1], [0]]

# Definición del modelo de red neuronal
model = Sequential([
    Dense(2, input_dim=2, activation='relu'), # Capa oculta con 2 neuronas
    Dense(1, activation='sigmoid')            # Capa de salida con 1 neurona y función de activación sigmoide
])

# Compilación del modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenamiento de la red neuronal
model.fit(X, y, epochs=1000, batch_size=4, verbose=0)

# Evaluación del modelo
loss, accuracy = model.evaluate(X, y)
print(f'Loss: {loss}, Accuracy: {accuracy}')

# Predicciones
predictions = model.predict(X)
print("Predicciones:")
for i in range(len(X)):
    print(f'Entrada: {X[i]}, Predicción: {predictions[i]}')