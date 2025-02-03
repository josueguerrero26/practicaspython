pila = [3,6,7]

while len(pila) >= 3 :
    if pila[-1] % 3:
        extraido =pila.pop()
        pila.append(extraido + 1)
        print(pila)
    else :
        print('Todos los elementos de la pila son multiplos de 3 ')
        break