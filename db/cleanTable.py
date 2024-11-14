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
        
        # Especificar el nombre de la tabla cuyos registros deseas borrar
        table_name = 'state'  # Reemplaza esto con el nombre de la tabla que deseas limpiar
        
        # Confirmar que la tabla existe antes de intentar borrar los registros
        cursor.execute("SHOW TABLES LIKE %s", (table_name,))
        result = cursor.fetchone()
        
        if result:
            # Borrar todos los registros de la tabla
            cursor.execute(f"DELETE FROM {table_name};")
            # Reiniciar el contador de auto-incremento
            cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1;")
            print(f"Todos los registros de la tabla '{table_name}' han sido eliminados correctamente y el contador de IDs ha sido reiniciado.")
            connection.commit()
            
            # Verificar si los registros fueron eliminados
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            if len(rows) == 0:
                print(f"La tabla '{table_name}' está vacía.")
            else:
                print(f"Los registros de la tabla '{table_name}' no han sido eliminados.")
        else:
            print(f"La tabla '{table_name}' no existe en la base de datos.")
        
        cursor.close()
        connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
