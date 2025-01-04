#con el while se hace un ciclo para en cuanto se detacte un erro se notifique al usuario y vuelva a escribir los datos 
val = True
while val:
    try:
     #if not y el if variable <=0 para detectar y notificar al usuario que tiene error al ingresar los datos 
     nombre = input("Dame tu nombre:  ".strip())
     if not nombre:
        raise ValueError('ingrese datos validos')
     apellidoP = input("Dame tu apellido paterno:  ".strip())
     if not apellidoP:
        raise ValueError('Ingresa datos validos ')
     apellidoM = input("Dame tu apellido materno:  ".strip())
     if not apellidoM:
        raise ValueError('Ingresa datos validos')
     edad = int(input("Dame tu edad: ".strip()))
     if edad <= 0:
        raise ValueError('Ingresa una edad correcta')
     peso = float(input("Dame tu peso:  ".strip()))
     if peso <=0:
        raise ValueError('ingresa un peso correcto')
     estatura = float(input("Dame tu estatura: ".strip()))
     if estatura <= 0:
        raise ValueError('Ingresa una estatura real ')
#el ** el para sacar la potencia y que sea un resultado exacto 
     imc = peso / estatura**2
# se inpriment los datos correctos que nos dio el usuario 
     print("tu resgistro fue exitoso ")
     print("tu nombre es: " + '{}  {}  {}' .format(nombre,apellidoP,apellidoM))
     print(f'Tienes  {edad} años')
     print(f"Tienes un peso de {peso:.2f}")
     print(f"Estatura de {estatura:.2f}")
     print('Tu IMC es: ' +str(imc))
     
     val = False
# aqui se inprime el error y de donde viene 
    except ValueError as e:      
        print(f"ERROR {e}")

# se utiliza el if para determinAr en que rango esta el peso 
if imc <= 18.4:
   print("Tienes un peso Bajo")
elif imc >= 18.5 and imc <= 24.9:
   print("Tienes un peso Normal")
elif imc >= 25.0 and imc <= 29.9:
   print("Tienes Sobrepeso")
elif imc >= 30.0 and imc <= 34.9:
   print("Tienes Obecidad I")
elif imc >= 35.0 and imc <= 39.8:
   print("Tienes Obecidad II")
elif imc >= 39.9:
   print("Tienes Obecidad III")


# se hace un estudio en el codigo para determinar que detecte los datos correctos y todo lo solicitado en el programa 


