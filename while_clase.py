n = 5
while n > 0 :
    n -= 1 
    if n == 2:
        #cierra el citlo cuando llega a dos con brake
        break
        # continue salta el numero 2 y sigue con el ciclo
    print(n)
else:
    print("Hola! ")
print("Loop terminado ")