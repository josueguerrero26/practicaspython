carros = ['audi', 'BMW', 'Ford', 'VW']

carros.sort(key=len)
print(carros)

lista = [[0,1], [2,3,4],[5,6]]
print(lista[0], lista[1:3])

print (lista[2][1])

vocales = ['a', 'e', 'i', 'o', 'u']
#hacer una copia de la lista 
vocales2 = vocales.copy()
print(vocales2, vocales)
print(id(vocales), id(vocales2))


del vocales2[2]
print(vocales2, vocales)
