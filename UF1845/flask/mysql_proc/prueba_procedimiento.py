import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password_que_quieras_para_root',
    database = 'jardineria'
)

cursor = conexion.cursor()
cursor.execute('call contar_gama(%s)',('Frutales',))

resultado = cursor.fetchall()

for fila in resultado:
    print(fila)

cursor.close()
conexion.close()
