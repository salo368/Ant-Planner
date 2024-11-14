
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def delete_user_action(user_id):
    
    query = f'''
        DELETE FROM user
        WHERE id = {user_id};
    '''
    result = db_model.queryEdit(query)

    return result
