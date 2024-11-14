import mysql.connector

config = {
    'host': '35.230.95.98',
    'user': 'antplanner-db',
    'password': 'salosamuseba',
    'database': 'antplanner'
}

table_name = 'user_task' 

try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        cursor = connection.cursor()
        
        cursor.execute(f"DESCRIBE {table_name}")
        columns_description = cursor.fetchall()
        print("Descripción de las columnas:")
        for column in columns_description:
            print(column)

        print("\nDatos de la tabla:")
        cursor.execute(f"SELECT * FROM {table_name}")
        users = cursor.fetchall()

        for user in users:
            print(user)

        cursor.close()
        connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
