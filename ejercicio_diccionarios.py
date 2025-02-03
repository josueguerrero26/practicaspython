emoji_diccionario = {
    "feliz": "😊",
    "triste": "😢",
    "enojado": "😠",
    "sorprendido": "😲",
    "pensativo": "🤔",
    "llorando": "😭",
    "riendo": "😂",
    "amo": "❤️",
    "estrella": "⭐",
    "fuego": "🔥",
    "pulgar arriba": "👍",
    "pulgar abajo": "👎",
    "aplauso": "👏",
    "cara con gafas de sol": "😎",
    "cara con máscara": "😷",
    "python": "🐍",
    "gato": "🐱",
    "perro": "🐶",
    "sol": "☀️",
    "luna": "🌙",
    "nube": "☁️",
    "lluvia": "🌧️",
    "nieve": "❄️",
    "trueno": "⚡",
    "arco iris": "🌈",
    "flor": "🌸",
    "árbol": "🌳",
    "coche": "🚗",
    "volar": "✈️",
    "bicicleta": "🚲",
    "libro": "📚",
    "computadora": "💻",
    "teléfono": "📱",
    "reloj": "⌚",
    "café": "☕",
    "pizza": "🍕",
    "hamburguesa": "🍔",
    "helado": "🍦",
    "pastel": "🍰"
}


frase = input("Escribe una frase: ").lower()
palabras = frase.split(" ")
respuesta = ""

for palabra in palabras:
    if palabra in emoji_diccionario:
        respuesta += emoji_diccionario[palabra] + " "
    else:
        respuesta += palabra + " "

print(respuesta)