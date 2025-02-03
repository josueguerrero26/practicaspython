tiempos = {
    'Hamilton': '1:34:55',
    'Verstappen': '1:35:20',
    'Bottas': '1:35:22',
    'Perez': '1:53:23',
}
# imprimir el diccionario
print(tiempos.items())
# imprimir las llaves del diccionario
print(tiempos.keys())
# imprimir los valores del diccionario
print(tiempos.values())
# imprimir el valor de una llave
print(tiempos.get('Hamilton'))

print(tiempos.get('hamilton', 'No existe'))