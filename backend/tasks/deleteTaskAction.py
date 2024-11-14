
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def delete_task_action(task_id):
    
    query = f'''
        DELETE FROM task
        WHERE id = {task_id};
    '''
    result = db_model.queryEdit(query)

    return result

def delete_task_user_action(task_id, user_id):

    query = f'''
        DELETE FROM user_task
        WHERE task_id = {task_id}
        AND user_id = {user_id};
    '''
    result = db_model.queryEdit(query)

    return result