import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
password = ''
while True:
    length = int(input('Que logintud quieres poner a la contraseña?'))

    for _ in range(length):
        password += random.choice(chars)
    print(password)
    password = ''
    respuesta = input('Quieres generar otra contraseña? (s/n)')
    if respuesta == 'n':
        break
    else:
        continue
    