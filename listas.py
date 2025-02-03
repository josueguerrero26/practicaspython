
# las listas siempre se empizan a contar desde el 0 
mix   = [0, 1.0, 'dos', 3+4j]
# imprimir la lista
for i in mix:
    print(f"{i:6} - tipo{type(i)}")
# agregar un elemento a la lista
sin_dos = mix[0:2] + mix[3:]
print(mix, sin_dos)
# duplicar la lista
duplicado = mix * 2
print(duplicado)
# nueva lista 2
cuadrados = [0,1,4,9,16,25]
for i in range(len(cuadrados)):
    
    cuadrados[i] =cuadrados[i]*i
    print(f"Ahora estan al cubo {cuadrados[i]}")




# lista 3
# agregar elementos a la lista
cuadrados.append(7**3)
print (cuadrados)
# insertar elementos en la lista
cuadrados.insert(6, 6**3)
print (cuadrados)
# extender la lista
cuadrados.extend([27, 100, -1])
print (cuadrados)
# extender la lista con un rango
cuadrados.extend(range(-1, -4, -1))
print (cuadrados)
# eliminar elementos de la lista
del cuadrados[9:]
print (cuadrados)
# eliminar elementos de la lista
cuadrados.remove(27)
print (cuadrados)
# extraer los elememntos de la lista 
valor_removido = cuadrados.pop(2)
print(valor_removido)
print(cuadrados)
# eliminar todos los elementos de la lista
cuadrados.clear()
print(cuadrados)



