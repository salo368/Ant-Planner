
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def get_project_action(id):
    
    query = f'''
        SELECT * FROM project 
        WHERE id = {id};
    '''
    result = db_model.queryFetch(query)

    return result
    
def get_all_projects_action():

    query = f'''
        SELECT * FROM project;
    '''
    result = db_model.queryFetch(query)

    return result

def get_project_users_action(id):
    
    query = f'''
        SELECT u.*, r.name AS role
        FROM user_project up
        JOIN user u ON up.user_id = u.id
        JOIN role r ON up.role_id = r.id
        WHERE up.project_id = {id};
    '''
    result = db_model.queryFetch(query)

    return result

def get_project_categories_action(id):
    
    query = f'''
        SELECT * FROM category
        WHERE project_id = {id};
    '''
    result = db_model.queryFetch(query)

    return result