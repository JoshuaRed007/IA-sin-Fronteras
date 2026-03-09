# -*- coding: utf-8 -*-
import google.generativeai as genai
from googletrans import Translator
import os

# 1. CONFIGURACION DE SEGURIDAD
# Tu llave personal de Google AI Studio
API_KEY = "AIzaSyDl43V2yZ5H3MmgVYldInDv5tQthGd-BQY"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
traductor = Translator()

# Funcion para que la IA hable (usando mpv y espeak)
def hablar(texto):
    # Generamos el audio y lo reproducimos con mpv
    os.system(f'espeak -v es "{texto}" --stdout | mpv -')

print("--- IA sin Fronteras: Conectada a Gemini ---")
hablar("Hola. Soy tu inteligencia artificial. En que puedo ayudarte?")

# 2. ENTRADA DEL USUARIO
pregunta = input("Usuario (puedes hablar en cualquier idioma): ")

# 3. TRADUCCION Y PROCESAMIENTO
# Traducimos al ingles para que Gemini sea mas preciso en el analisis
try:
    traduccion = traductor.translate(pregunta, dest='en')
    prompt = f"Actua como una IA positiva y humana. Responde de forma breve a: {traduccion.text}"
    
    # Llamada a la API de Google
    response = model.generate_content(prompt)
    
    # Traducimos la respuesta de vuelta al español
    respuesta_es = traductor.translate(response.text, dest='es').text
    
    # 4. RESULTADO
    print(f"🌍 Idioma original detectado: {traduccion.src.upper()}")
    print(f"🤖 IA: {respuesta_es}")
    hablar(respuesta_es)

except Exception as e:
    print(f"Error en la conexion: {e}")
    print("🤖 IA: Disculpa, he tenido un problema tecnico.")
