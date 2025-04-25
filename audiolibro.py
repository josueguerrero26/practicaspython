from gtts import gTTS
import os


try:
    # Abrir y leer el archivo de texto
    with open("libro.txt", "r", encoding="utf-8") as file:
        texto = file.read()

    # Convertir el texto a audio
    audio = gTTS(text=texto, lang="es")
    audio.save("audio.mp3")
    print("El archivo de audio se ha generado correctamente como 'audio.mp3'.")

except FileNotFoundError:
    print("Error: El archivo 'libro.txt' no se encontró. Asegúrate de que esté en el mismo directorio que este script.")
except Exception as e:
    print(f"Se produjo un error: {e}")