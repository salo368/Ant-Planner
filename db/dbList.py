import mysql.connector

config = {
    'host': '35.230.95.98',
    'user': 'antplanner-db',
    'password': 'salosamuseba'
}

try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        
        print("Lista de bases de datos:")
        for db in databases:
            print(db[0])
        
        cursor.close()
        connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
