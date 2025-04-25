#https://www.mysqltutorial.org/python-mysql/ (suele ser: mysql -u root -p)
# pip install mysql-connector-python
import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'bbdd_prueba'
)

cursor = conexion.cursor()

nuevo_usuario = []
print('Añadir nuevo usuario')
nombre = input('Introduce el nombre del usuario: ')
nuevo_usuario.append(nombre)
edad = input('Introduce la edad del usuario: ')
nuevo_usuario.append(edad)


nuevo_usuario = (nombre, edad)

consulta = 'INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)'
cursor.execute(consulta, nuevo_usuario)
conexion.commit()

print(f'Usuario {nuevo_usuario[0]} añadido a la base de datos.')
conexion.close()
