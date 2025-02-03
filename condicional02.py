peso = float(input("Dame tu peso: "))
altura = float(input("Dame tu altura: "))

bmi = peso / altura ** 2

if bmi >= 25:
    print("Sobrepeso")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Bajo de peso")