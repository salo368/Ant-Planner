import mysql.connector
from mysql.connector import Error
from fastapi import HTTPException

class DBModel:
    def __init__(self):
        self.config = {
            'host': '35.230.95.98',
            'user': 'antplanner-db',
            'password': 'salosamuseba',
            'database': 'antplanner'
        }

    def queryFetch(self, query):
        """Método para ejecutar consultas SELECT y devolver los resultados."""
        try:
            connection = mysql.connector.connect(
                host=self.config['host'],
                user=self.config['user'],
                password=self.config['password'],
                database=self.config['database']
            )
            
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                cursor.execute(query)
                
                result = cursor.fetchall()
                
                cursor.close()
                connection.close()
                
                return result
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise HTTPException(status_code=500, detail={"error": "Database connection failed"})

    def queryEdit(self, query, data=None):
        """Método para ejecutar consultas de modificación como INSERT, UPDATE y DELETE."""
        try:
            connection = mysql.connector.connect(
                host=self.config['host'],
                user=self.config['user'],
                password=self.config['password'],
                database=self.config['database']
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
                if data:
                    cursor.execute(query, data)
                else:
                    cursor.execute(query)
                
                connection.commit()
                affected_rows = cursor.rowcount
                
                cursor.close()
                connection.close()
                
                return affected_rows
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise HTTPException(status_code=500, detail={"error": "Database connection failed"})

