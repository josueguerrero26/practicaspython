#pip install slack-sdk
#pip install pyjokes

from slack_sdk import WebClient
import pyjokes

# Token de autenticación del bot
TOKEN = 'xoxb-8707377005968-8695558676689-mFaovue9DyaHUIKvnDRX1Ec2'

# Inicializar cliente de Slack
client = WebClient(token=TOKEN)

# Mensaje a enviar
mensaje = "Hola, soy un bot de Josu. ¿Cómo puedo ayudarte?"

# Enviar mensaje al canal
try:
    response = client.chat_postMessage(
        channel='#proyectos',  # Asegúrate de que el canal existe
        text=mensaje
    )
    print("Mensaje enviado correctamente:", response)
except Exception as e:
    print("Error al enviar el mensaje:", e)