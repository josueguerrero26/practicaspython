 
val = True

while val:
    c1 = input("Introduce una contraseña: ")
    
    if c1[0].isdigit():  # Verifica si el primer carácter es un número
        c2 = input("Ingresa nuevamente la contraseña: ")
        if c1 == c2:
            print("Contraseña Correcta")
            val = False  # Sale del bucle si las contraseñas coinciden
        else:
            print("La contraseña no coincide")
    else:
        print("La contraseña debe comenzar con un número")

        



        
     
          



