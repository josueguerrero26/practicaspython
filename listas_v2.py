vocales = ['a', 'e', 'i', 'o', 'u']
#modificar los elementos de la lista 
vocales[1:4] = ['E', 'I', 'O']

print(vocales, len(vocales))
# eliminar elementos de la lista
del vocales[1:4]
print(vocales, len(vocales))
# agregar elementos a la lista
vocales.extend(['i', 'i'])

print(vocales, len(vocales))
# insertar elementos en la lista
print(vocales.index('i'))
# contar elementos en la lista
print(vocales.count('i'))
# invertir los elementos de la lista
vocales.reverse()
print(vocales)
# ordenar los elementos de la lista
vocales.sort()
print(vocales, len(vocales))
