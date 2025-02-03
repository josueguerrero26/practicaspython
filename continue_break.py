#uso de la sentecia de un continue en un ciclo for 

# for numero in range(1, 11):
#    if numero % 2 == 1:
#        continue
#    print(f"El numero {numero} es par")


# numero = 0
# while numero < 11:
#     numero += 1
#     if numero % 2 == 1:
#         continue
#     print(f"El numero {numero} es par")
#########################################################
#uso de la sentencia de un break 
 
# numero = int(input("Ingrese un digito: "))
# limite_inferior = 0
# limite_superior = 10
# buscado = 5
# intentos = 0

# while True:
#     intentos += 1
#     if numero ==buscado:
#         print (f"El numero {numero} ha sido encontrado en {intentos} intentos")
#         break
#     elif numero < buscado:
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) // 2
#     else:
#         limite_inferior = buscado
#         buscado = (buscado + limite_superior) // 2

# print ("Fin del ciclo")

#########################################################
#uso de la funcion exit

numero = int(input("Ingrese un digito: "))
limite_inferior = 0
limite_superior = 10
buscado = 5
intentos = 0

while True:
    intentos += 1
    if numero ==buscado:
        print (f"El numero {numero} ha sido encontrado en {intentos} intentos")
        break
    elif numero < buscado:
        limite_superior = buscado
        buscado = (buscado + limite_inferior) // 2
    else:
        limite_inferior = buscado
        buscado = (buscado + limite_superior) // 2

print ("Fin del ciclo")