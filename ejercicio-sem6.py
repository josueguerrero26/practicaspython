#para que i en el rango de 2,100
for i in range(2, 100) :
    #se asume que el numero es primo
    primo = True

    for j in range(2, i) :

        if i % j == 0 :
            primo = False


    if primo == True :
        print(i, end = " ")