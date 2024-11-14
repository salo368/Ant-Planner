
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def create_user_action(name, last_name, email, password):
    
    query = f'''
        INSERT INTO user (name, last_name, email, password)
        VALUES ('{name}', '{last_name}', '{email}', '{password}');
    '''
    result = db_model.queryEdit(query)

    return result