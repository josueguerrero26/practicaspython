entrada = input("Introduce tu edad: ")

edad = 0

if entrada.isnumeric() :
    edad= int(entrada)
else :
    print("Dato incorrecto. Debes introducer un numero")
    exit()

if edad <= 0 :
    print("WoooWWW!! Que joven eres ")
elif edad >115 :
    print("Vaya!!!! Como le haces para vivir tanto")
elif edad <18 :
    print("Eres menor de edad. No puedes comprar cigarrillos ")
else :
    print("Eres mayor de edad. Aqui tienes tu cigarrillo")
    