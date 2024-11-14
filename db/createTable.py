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
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS antplanner")
        print("Base de datos `antplanner` creada o ya existe.")
        
        cursor.execute("USE antplanner")
        
        # create_table_query = '''
        # CREATE TABLE IF NOT EXISTS user (
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     name VARCHAR(100) NOT NULL,
        #     last_name VARCHAR(100),
        #     email VARCHAR(100) UNIQUE NOT NULL,
        #     password VARCHAR(255) NOT NULL
        # );
        # '''

        # create_table_query = '''
        # CREATE TABLE IF NOT EXISTS role (
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     name VARCHAR(100) NOT NULL,
        #     info VARCHAR(500)
        # );
        # '''

        # create_table_query = '''
        # CREATE TABLE IF NOT EXISTS project (
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     name VARCHAR(100) NOT NULL,
        #     info VARCHAR(500)
        # );
        # '''

        # create_table_query = '''
        # CREATE TABLE IF NOT EXISTS user_project (
        #     user_id INT NOT NULL,
        #     project_id INT NOT NULL,
        #     role_id INT NOT NULL,
        #     PRIMARY KEY (user_id, project_id), 
        #     FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE, 
        #     FOREIGN KEY (project_id) REFERENCES project(id) ON DELETE CASCADE, 
        #     FOREIGN KEY (role_id) REFERENCES role(id) ON DELETE CASCADE 
        # );
        # '''

        # create_table_query = '''
        # CREATE TABLE IF NOT EXISTS sprint (
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     project_id INT NOT NULL,
        #     FOREIGN KEY (project_id) REFERENCES project(id) ON DELETE CASCADE,
        #     name VARCHAR(100) NOT NULL,
        #     info VARCHAR(500),
        #     start_date TIMESTAMP,
        #     end_date TIMESTAMP
        # );
        # '''

        # create_table_query = '''
        # CREATE TABLE IF NOT EXISTS category (
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     project_id INT NOT NULL,
        #     FOREIGN KEY (project_id) REFERENCES project(id) ON DELETE CASCADE,
        #     name VARCHAR(100) NOT NULL,
        #     info VARCHAR(500)
        # );
        # '''

        # create_table_query = '''
        # CREATE TABLE IF NOT EXISTS state (
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     name VARCHAR(100) NOT NULL,
        #     info VARCHAR(500)
        # );
        # '''

        # create_table_query = '''
        # CREATE TABLE IF NOT EXISTS task_type (
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     name VARCHAR(100) NOT NULL,
        #     info VARCHAR(500)
        # );
        # '''

        # create_table_query = '''
        # CREATE TABLE IF NOT EXISTS calendar_event (
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     sprint_id INT NOT NULL,
        #     FOREIGN KEY (sprint_id) REFERENCES sprint(id) ON DELETE CASCADE,
        #     name VARCHAR(100) NOT NULL,
        #     info VARCHAR(500),
        #     user_host_id INT NOT NULL,
        #     FOREIGN KEY (user_host_id) REFERENCES user(id) ON DELETE CASCADE,
        #     start_date TIMESTAMP,
        #     end_date TIMESTAMP,
        #     transcription_id INT,
        #     FOREIGN KEY (transcription_id) REFERENCES transcription(id) ON DELETE CASCADE
        # );
        # '''

        # create_table_query = '''
        # CREATE TABLE IF NOT EXISTS  transcription(
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     file_reference VARCHAR(255) NOT NULL, 
        #     transcription_text LONGTEXT 
        # );
        # '''

        # create_table_query = '''
        # CREATE TABLE IF NOT EXISTS task (
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     sprint_id INT NOT NULL,
        #     FOREIGN KEY (sprint_id) REFERENCES sprint(id) ON DELETE CASCADE,
        #     name VARCHAR(100) NOT NULL,
        #     info VARCHAR(500),
        #     start_date TIMESTAMP,
        #     end_date TIMESTAMP,
        #     task_type_id INT NOT NULL,
        #     FOREIGN KEY (task_type_id) REFERENCES task_type(id) ON DELETE CASCADE,
        #     category_id INT,
        #     FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE,
        #     state_id INT NOT NULL,
        #     FOREIGN KEY (state_id) REFERENCES state(id) ON DELETE CASCADE
        # );
        # '''
        
        
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS user_task (
            user_id INT NOT NULL,
            task_id INT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE, 
            FOREIGN KEY (task_id) REFERENCES task(id) ON DELETE CASCADE 
        );
        '''


        # create_table_query = '''
        # CREATE TABLE IF NOT EXISTS user_calendar_event (
        #     user_id INT NOT NULL,
        #     calendar_event_id INT NOT NULL,
        #     FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE, 
        #     FOREIGN KEY (calendar_event_id) REFERENCES calendar_event(id) ON DELETE CASCADE 
        # );
        # '''

        cursor.execute(create_table_query)
        print("Tabla `user` creada exitosamente.")
        
        cursor.close()
        connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
