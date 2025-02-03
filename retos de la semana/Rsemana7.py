lista = []

while True:
    opccion = input("Agregasr alumno (1) o terminar(2): ".strip())

    if opccion == '1':
        nombre = input("Nombre del alumno: ").capitalize()

        while True:
            opccion2 = input("Agregar calificacion (1) o terminar (2): ")
            if opccion2 == '1':
                calificacion = int(input(f"Ingresa la calificacion de {nombre}: "))
                calF = calificacion + (1 / calificacion)
                alumno = [nombre, calF]
                lista.append(alumno)

            elif opccion2 == '2':
                print ("Ya no hay calificaciones por agregar") 
                break

    elif opccion == '2':
        print("Ya no hay alumnos por agregar")  
        break   

print("Lista de alumnos")
print(lista)
