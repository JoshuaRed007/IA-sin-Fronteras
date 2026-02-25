# -*- coding: utf-8 -*-
from textblob import TextBlob
from googletrans import Translator

# Inicializamos el traductor
traductor = Translator()

print("--- IA sin Fronteras: Analizador Multilingue ---")
frase_original = input("Como te sientes hoy? (Cualquier idioma): ")

# 1. Traduccion interna
traduccion = traductor.translate(frase_original, dest='en')
frase_en_ingles = traduccion.text

# 2. Analisis de la IA
analisis = TextBlob(frase_en_ingles)
sentimiento = analisis.sentiment.polarity

# 3. Resultados
print(f"Idioma detectado: {traduccion.src.upper()}")
print(f"IA (Traduccion): {frase_en_ingles}")

if sentimiento > 0.1:
    print("IA: Detecto una energia muy positiva.")
elif sentimiento < -0.1:
    print("IA: Parece que no es un buen momento. Animo!")
else:
    print("IA: Te noto en un estado neutral.")

print(f"Puntuacion: {sentimiento}")
