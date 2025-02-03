canasta = {'manzana', 'naranja', 'pera', 'naranja', 'platano', 'manzana'}
#no te imprtime los elementos repetidos
print(canasta) # {'naranja', 'manzana', 'pera', 'platano'}
print('naranja' in canasta) # True
print('cereza' in canasta) # False

# operaciones de conjuntos

#vocales = ['a', 'e', 'i', 'o', 'u']
#print(vocales)
#vocales = list(set(vocales))
#print(vocales)

#vocales1 = {'a', 'e', 'i', 'o', 'u', 'a'}
#vocales2 = {'e', 'i', 'o'}
#vocales 2 es un subconjunto de vocales 1
#print(vocales2.issubset(vocales1)) # True

vocales1 = {'a', 'e', 'i', 'o', 'u'}
vocales2 = {'A', 'E', 'I', 'O', 'u'}
#la interseccion de los dos conjuntos
print(vocales1 - vocales2) # {'a', 'u', 'o'}
#la unio de los dos conjuntos
print(vocales1 | vocales2) # {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#que elementos son comunes en los dos conjuntos
print(vocales1 & vocales2) 
#que elementos no son comunes en los dos conjuntos
print(vocales1 ^ vocales2) # {'a', 'A', 'E', 'I', 'O', 'u', 'U', 'o'}