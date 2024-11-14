
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def update_task_action(task_id, attributes):
   
    set_clause = ', '.join([f"{key} = '{value}'" for key, value in attributes.items()])

    query = f'''
        UPDATE task
        SET {set_clause}
        WHERE id = {task_id};
    '''
    result = db_model.queryEdit(query)

    return result
    
