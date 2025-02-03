#creamos un ciclo de cierre de programa 
while True:
    opccion = input("Desea ingresar coordenadas (1) o terminar(2): ".strip())
    if opccion == '1':
# ingresar valores 
        x =  int (input("Ingresa el valor de X: "))
        y= int(input("Ingresa el valor  de Y: "))

        if x> 0 and y > 0:
            print(f"Cuadrante I  con las siguientes cordenadas X {x} Y {y}")
        elif x < 0 and y > 0:
            print(f"Cuadrante II  con las siguientes cordenadas X {x} Y {y}")
        elif x < 0 and y < 0:
            print(f"Cuadrante III  con las siguientes cordenadas X {x} Y {y}")
        elif x > 0 and y < 0:
         print(f"Cuadrante IV  con las siguientes cordenadas X {x} Y {y}")

    elif opccion == '2':
        print("Ya no hay cordenadas por ingresar ")
        break
            
    