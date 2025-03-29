import requests as req
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json
import os
from io import BytesIO


#Crear  la c arpeta pokemon si no existe 
if not os.path.exists("Pokedex"):
    os.makedirs("Pokedex")

def obtener_datos_pokemon(nombre_pokemon):
    ''''
    Esta funcion obtiene los datos de un pokemon
    utilizando la API de pokeapi.co
    E imprimir los errores que se puedan presentar
    '''
    url=f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}' #URL de la API
    try:
        respuesta = req.get(url, timeout=10) #Obtener respuesta de la API
        if  respuesta.status_code == 404: #Si el status code es 404
            print(f"El pokemon {nombre_pokemon} no existe. Intenta con otro nombre") #Imprimir mensaje
            return None #Si no existe el pokemon retorna None

        elif respuesta.status_code != 200:
            print(f"Error en obtener datos del pokemon. Codigfo de estado: {respuesta.status_code}") #Si el status code no es 200
            return None #Retorna None
        return respuesta.json() #Retorna la respuesta en formato json
    except req.exceptions.RequestException as e: #Si hay un error en la conexion con la API 
        print(f"Error al conectar con la API: {e}")
        return None
    

def guardar_datos_pokemon(nombre_pokemon, datos):
    '''
    Esta funcion guarda los datos de un pokemon en un archivo json
    '''
    archivo = f"Pokedex/{nombre_pokemon.lower()}.json" #Nombre del archivo
    with open(archivo, "w", encoding="utf-8") as f: #Abrir el archivo
        json.dump(datos, f, ensure_ascii=False, indent=4) #Guardar los datos en el archivo
    print(f"Datos del pokemon {nombre_pokemon} guardados en {archivo}.") #Imprimir mensaje

def mostrar_dotos_pokemon(datos):
    '''
    Esta funcion muestra los datos del pokemon
    '''
    print(f"""\n--- Información del Pokémon ---
          Nombre: {datos['name'].capitalize()}
          Peso:  {datos['weight']} Hectogramos
          Tamaño: {datos['height']} Decimetros
          """)
    print("\nTipos:")
    for tipo in datos['types']:
        print(f"- {tipo['type']['name'].capitalize()}") #Imprimir los tipos del pokemon y capitalize lo pone en mayuscula

    print("\nHabilidades:")
    for habilidad in datos['abilities']:
        print(f"- {habilidad['ability']['name'].capitalize()}") #Imprimir las habilidades del pokemon y capitalize lo pone en mayuscula
    print("\nMovimientos:")
    for movimiento in datos['moves'][:10]: #Mostrar solo los primeros 10 movimientos
        print(f"- {movimiento['move']['name'].capitalize()}") #Imprimir los movimientos del pokemon y capitalize lo pone en mayuscula
    
    print("\nImagen del Pokemon:")
    print(datos['sprites']['front_default']) #Imprimir la imagen del pokemon
    
def graficar_datos_pokemon(datos):
    '''
    Esta funcion grafica los datos del pokemon
    '''
    nombre = datos['name'].capitalize() #Nombre del pokemon en mayuscula
    peso = datos['weight'] #Peso del pokemon
    altura = datos['height'] #Altura del pokemon    
    tipos = [tipo['type']['name'].capitalize() for tipo in datos['types']] #Tipos del pokemon en mayuscula
    habilidades = [habilidad['ability']['name'].capitalize() for habilidad in datos['abilities']] #Habilidades del pokemon en mayuscula
    imagen_url = datos['sprites']['front_default'] #Imagen del pokemon

    response = req.get(imagen_url) #Obtener la imagen del pokemon
    imagen = Image.open(BytesIO(response.content)) #Abrir la imagen del pokemon

    # Crear la grafica
    plt.figure(figsize=(8, 6)) #Tamaño de la imagen
    plt.axis('off') #Ocultar los ejes
    plt.title(f"Informaion de {nombre}") #Titulo de la imagen
    plt.imshow(imagen) #Mostrar la imagen
    texto = (
        f"Nombre: {nombre}\n"
        f"Peso: {peso} hectogramos\n"
        f"Altura: {altura} decimetros\n"
        f"Tipos: {', '.join(tipos)}\n"
        f"Habilidades: {', '.join(habilidades)}"
    )
    plt.text(1.05, 0.5, texto, fontsize=12, transform=plt.gca().transAxes, verticalalignment='center') #Texto de la imagen
    plt.show() #Mostrar la imagen

def main():
    '''
    Esta funcion es la principal

    '''
    
    print("Bienvenido a la pokedex de pokemon") #Mensaje de bienvenida
    while True:
        nombre_pokemon = input("Introduce el nombre del pokemon que deseas buscar: ").strip()
        if not nombre_pokemon: #Si no se ingresa un nombre
            print("No ingresaste ningun nombre. Intentalo de nuevo") #Imprimir mensaje
            continue #Continuar
        datos = obtener_datos_pokemon(nombre_pokemon)
        if datos: #Si hay datos
            guardar_datos_pokemon(nombre_pokemon, datos) #Guardar los datos
            mostrar_dotos_pokemon(datos) #Mostrar los datos
            graficar_datos_pokemon(datos) #Graficar los datos

        respuesta = input("Deseas buscar otro pokemon? (s/n): ").strip().lower() #Preguntar si desea buscar otro pokemon
        if respuesta != "s": #Si la respuesta no es s
            break #Salir del ciclo
    print("Gracias por usar la pokedex") #Mensaje de despedida

if __name__ == "__main__":
    main() #Llamar a la funcion principal
