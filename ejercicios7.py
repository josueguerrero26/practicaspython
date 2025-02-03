lista = []
alumnos = 0
while alumnos <= 5:
    opccion = input("Agregar alumno (1) o terminar (2) ")
    if opccion == '1':
        nombre = input("Nombre del alumno: ").capitalize()
        calificacion = int (input(f"Ingresa la primera calificacion de {nombre}: "))
        calificacion2 = int (input(f"Ingresa la segunda calificacion de {nombre}: "))
        alumno = [nombre, calificacion, calificacion2]
        lista.append(alumno)
        alumnos += 1
    elif opccion == '2':
        print(f"El programa a terminado con {alumnos} alumnos registrados")
        break
    else:
        print("Opcion no valida")
        continue

print("Lista de alumnos")
print(lista)

