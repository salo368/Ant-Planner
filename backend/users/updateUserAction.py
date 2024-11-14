
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def update_user_action(user_id, attributes):
   
    set_clause = ', '.join([f"{key} = '{value}'" for key, value in attributes.items()])

    query = f'''
        UPDATE user
        SET {set_clause}
        WHERE id = {user_id};
    '''
    result = db_model.queryEdit(query)

    return result
    
