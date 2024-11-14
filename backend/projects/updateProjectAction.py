
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def update_project_action(project_id, attributes):
   
    set_clause = ', '.join([f"{key} = '{value}'" for key, value in attributes.items()])

    query = f'''
        UPDATE project
        SET {set_clause}
        WHERE id = {project_id};
    '''
    result = db_model.queryEdit(query)

    return result

def update_project_user_action(project_id, user_id, role_id):

    query = f'''
        UPDATE user_project
        SET role_id = {role_id}
        WHERE project_id = {project_id}
        AND user_id = {user_id};
    '''
    result = db_model.queryEdit(query)

    return result

def update_project_category_action(category_id, attributes):
   
    set_clause = ', '.join([f"{key} = '{value}'" for key, value in attributes.items()])

    query = f'''
        UPDATE category
        SET {set_clause}
        WHERE id = {category_id};
    '''
    result = db_model.queryEdit(query)

    return result