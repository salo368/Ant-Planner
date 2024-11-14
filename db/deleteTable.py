import mysql.connector

config = {
    'host': '35.230.95.98',
    'user': 'antplanner-db',
    'password': 'salosamuseba',
    'database': 'antplanner'
}

try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Especificar el nombre de la tabla a borrar
        table_name = 'user_task'  # Reemplaza esto con el nombre de la tabla que deseas eliminar
        
        # Confirmar que la tabla existe antes de intentar borrarla
        cursor.execute("SHOW TABLES LIKE %s", (table_name,))
        result = cursor.fetchone()
        
        if result:
            cursor.execute(f"DROP TABLE {table_name}")
            print(f"La tabla '{table_name}' ha sido eliminada correctamente.")
        else:
            print(f"La tabla '{table_name}' no existe en la base de datos.")
        
        cursor.close()
        connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
