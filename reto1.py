actual = input("Introduce el año actual: ")
if actual.isnumeric():
    actual = int(actual)
else:
    print("Introduce un año valido")
    exit()
a2 = int(input("Introduce el año para calcular:"))

t = actual - a2 
pos = abs(t)

if  a2 < actual:
    print(f"Han pasado {t} años desde el año que has introducido")
elif a2 > actual :
    print(f"Faltan {pos} años para llegar al año introducido")
elif t == 1 :
    print(f"Desde el {actual} ha pasado {t} año")
elif t == -1 :
    print(f"Para llegar al {a2} Falta {pos} año")
else :
    print("Has introducido el mismo el mismo año actual")
