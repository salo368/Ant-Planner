
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def create_project_action(name, info):
 
    query = f'''
        INSERT INTO project (name, info)
        VALUES ('{name}', '{info}');
    '''
    result = db_model.queryEdit(query)

    return result

def create_project_user_action(project_id, user_id, role_id):
 
    query = f'''
        INSERT INTO user_project (project_id, user_id, role_id)
        VALUES ('{project_id}', '{user_id}', '{role_id}');
    '''
    result = db_model.queryEdit(query)

    return result

def create_project_category_action(project_id, name, info):
 
    query = f'''
        INSERT INTO category (project_id, name, info)
        VALUES ('{project_id}', '{name}', '{info}');
    '''
    result = db_model.queryEdit(query)

    return result

