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
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        print("Lista de tablas en la base de datos:")
        for table in tables:
            print(table[0])
        
        cursor.close()
        connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
