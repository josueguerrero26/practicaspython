import re

def verificar_contraseña(contraseña):
    # Verificar si la contraseña comienza con un número
    return re.match(r'^\d', contraseña)

def solicitar_contraseña():
    return input("Ingrese una contraseña: ")

def main():
    intentos = 0
    while intentos < 3:
        contraseña1 = solicitar_contraseña()
        if not verificar_contraseña(contraseña1):
            print("La contraseña debe comenzar con un número.")
            intentos += 1
            continue
        
        contraseña2 = input("Ingrese la contraseña nuevamente: ")
        if contraseña1 == contraseña2:
            print("Contraseña válida.")
            break
        else:
            print("Las contraseñas no coinciden.")
            intentos += 1
    
    if intentos == 3:
        print("Se han cometido tres errores. El programa se cerrará.")

if __name__ == "__main__":
    main()
