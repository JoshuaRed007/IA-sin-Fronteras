# -*- coding: utf-8 -*-
from textblob import TextBlob
from googletrans import Translator
import os

# Inicializamos el traductor
traductor = Translator()

# Funcion para que la IA hable
def hablar(texto):
    # Usamos os.system para llamar a espeak desde Termux
    os.system(f'espeak -v es "{texto}"')

print("--- IA sin Fronteras: Analizador de voz ---")
hablar("Hola. Como te sientes hoy?")
frase_original = input("¿Cómo te sientes hoy? (Cualquier idioma): ")

# 1. Traduccion interna
traduccion = traductor.translate(frase_original, dest='en')
frase_en_ingles = traduccion.text

# 2. Analisis de la IA
analisis = TextBlob(frase_en_ingles)
sentimiento = analisis.sentiment.polarity

# 3. Resultados y Voz
print(f"Idioma detectado: {traduccion.src.upper()}")
print(f"IA (Traduccion): {frase_en_ingles}")

if sentimiento > 0.1:
    respuesta = "Detecto una energia muy positiva."
elif sentimiento < -0.1:
    respuesta = "Parece que no es un buen momento. Animo!"
else:
    respuesta = "Te noto en un estado neutral."

print(f"IA: {respuesta}")
hablar(respuesta)
print(f"Puntuacion: {sentimiento}")
