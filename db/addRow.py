import mysql.connector

config = {
    'host': '35.230.95.98',
    'user': 'antplanner-db',
    'password': 'salosamuseba'
}

try:
    # Establecer conexión
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Seleccionar la base de datos
        cursor.execute("USE antplanner")
        
        # Insertar los estados solicitados
        # states = [
        #     ('TO DO', 'Estado inicial de la tarea'),
        #     ('IN PROGRESS', 'La tarea está en progreso'),
        #     ('PAUSED', 'La tarea está pausada'),
        #     ('VERIFY', 'La tarea está en proceso de verificación'),
        #     ('DONE', 'La tarea ha sido completada')
        # ]

        states = [
            ('ADMIN', 'Usuario con permisos completos para administrar el sistema, gestionar usuarios, configuraciones y todos los aspectos del proyecto.'),
            ('SCRUM ADMIN', 'Usuario con permisos para editar sprints, tareas, categorías y asignaciones, facilitando la gestión y el seguimiento del proyecto.'),
            ('TEAM MEMBER', 'Usuario con permisos limitados, puede visualizar y actualizar las tareas asignadas, pero no gestionar aspectos globales del proyecto.')
        ]

        # states = [
        #     ('NEW', 'Nueva funcionalidad que se va a desarrollar'),
        #     ('BUG', 'Arreglo de un error o fallo en el sistema'),
        #     ('UPDATE', 'Actualización o adición a una funcionalidad o componente existente'),
        #     ('TEST', 'Proceso de prueba o verificación de una funcionalidad o componente'),
        #     ('IMPROVE', 'Mejora de una funcionalidad existente, enfocándose en eficiencia o calidad'),
        #     ('DOC', 'Trabajo relacionado con la documentación del sistema o proyecto')
        # ]

        insert_query = "INSERT INTO role (name, info) VALUES (%s, %s)"
        
        # Ejecutar la inserción de los estados
        cursor.executemany(insert_query, states)
        connection.commit()
        
        print("Estados insertados exitosamente.")
        
        # Cerrar cursor y conexión
        cursor.close()
        connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
