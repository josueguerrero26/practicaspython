# condonar errores 
val = True

while val:
    try:

#solicitar datos del ususario
     # .string no deja espacios vacios
     nombre = input('Ingresa tu nombre: '.strip())
     if not nombre:
        raise ValueError('El nombre no puede quear vacio')

     edad = int(input("Ingresa tu edad: ".strip()))
     if not edad:
        raise ValueError('El numero no puede ser menor a 0')
     ingreso = input("Ingresa tu ingreso mensual: ".strip())
     if not  ingreso >=1:
        raise ValueError('Ingrese un numero positivo')

     gasto = int(input('Ingresa tu gasto mensual: '))
     if  gasto <= ingreso:
        raise ValueError('Ingresa datos validos ')
     objetivo = int(input("Ingresa tu objetivo de ahorro: "))
     if not object:
        raise ValueError('Ingresa un objetivo valido ')
     

     Ahorro_mensual = ingreso - gasto
     tiempo_ahorro = objetivo / Ahorro_mensual

     print(Ahorro_mensual)
     print(tiempo_ahorro)

     val = False

    except ValueError as e:
        print(f"ERROR: {e}")




