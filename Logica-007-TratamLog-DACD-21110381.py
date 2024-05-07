#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Descargar recursos de NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Definir una oración de ejemplo
texto = "El análisis de sentimientos es una técnica para determinar la actitud positiva, negativa o neutral hacia un tema."

# Tokenización
tokens = word_tokenize(texto)

# Eliminar stopwords
stop_words = set(stopwords.words("spanish"))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Lematización
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word, wordnet.VERB) for word in filtered_tokens]

print("Texto original:", texto)
print("Tokens:", tokens)
print("Tokens filtrados:", filtered_tokens)
print("Tokens lematizados:", lemmatized_tokens)
