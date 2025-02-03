fruits = ['Apple', 'Peach', 'Pear']

for fruit in fruits:
    print(fruit)


# Ejemplo 2
scores = [31, 27, 86, 2, 5, 6]

max_score = 0

for scores in scores:
    if scores > max_score:
        max_score = scores
print(f"El puntaje mas alto en la lista es: {max_score}")