from textblob import TextBlob

print("--- Analizador de Sentimientos IA ---")
frase = input("¿Cómo te sientes hoy? (Escríbelo en inglés para esta prueba): ")

# La IA analiza la frase
analisis = TextBlob(frase)
sentimiento = analisis.sentiment.polarity

# Interpretación de los resultados
if sentimiento > 0:
    print("🤖 IA: ¡Detecto mucha positividad en tus palabras!")
elif sentimiento < 0:
    print("🤖 IA: Parece que algo no va bien. ¡Ánimo!")
else:
    print("🤖 IA: Te noto neutral.")

print(f"Puntuación de la IA: {sentimiento}")
