
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def delete_project_action(project_id):
    
    query = f'''
        DELETE FROM project
        WHERE id = {project_id};
    '''
    result = db_model.queryEdit(query)

    return result

def delete_project_user_action(project_id, user_id):
    
    query = f'''
        DELETE FROM user_project
        WHERE project_id = {project_id}
        AND user_id = {user_id};
    '''
    result = db_model.queryEdit(query)

    return result

def delete_project_category_action(category_id):
    
    query = f'''
        DELETE FROM category
        WHERE id = {category_id};
    '''
    result = db_model.queryEdit(query)

    return result