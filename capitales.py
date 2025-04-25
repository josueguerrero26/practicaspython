capitales = {
    'Argentina': 'Buenos Aires',
    'Bolivia': 'La Paz',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Colombia': 'Bogota',
    'Ecuador': 'Quito',
    'Guyana': 'Georgetown',
    'Paraguay': 'Asuncion',
    'Peru': 'Lima',
    'Surinam': 'Paramaribo',
    'Uruguay': 'Montevideo',
    'Venezuela': 'Caracas',
    'Mexico': 'Ciudad de Mexico'
}

def capital():
    
    
    print("Bienvenido al juego de las capitales!")
    score = 0

    while True:

        for pais, capital in capitales.items():
            respuesta = input(f'Cual es la capital de {pais}?  ')
            score = 0 

            if respuesta.lower() == capital.lower():
                print('Correcto!')
                score += 1 
            else:
                print(f'Incorrecto! La capital de {pais} es {capital}') 

        else:
            continuar = input('Quieres continuar? (s/n)')
            if continuar.lower() != 's':
                break
    
            
    print(f'Tu puntaje es {score}/{len(capitales)}')

if __name__ == '__main__':
    capital()