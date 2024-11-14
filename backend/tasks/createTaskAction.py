
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def create_task_action(sprint_id, name, info, start_date, end_date, task_type_id, category_id, state_id):
    
    query = f'''
        INSERT INTO task (sprint_id, name, info, start_date, end_date, task_type_id, category_id, state_id)
        VALUES ('{sprint_id}', '{name}', '{info}', {f"'{start_date}'" if start_date is not None else 'NULL'}, {f"'{end_date}'" if end_date is not None else 'NULL'}, '{task_type_id}', {f"'{category_id}'" if category_id is not None else 'NULL'}, {state_id});
    '''
    result = db_model.queryEdit(query)
    
    return result

def create_task_user_action(task_id, user_id):

    query = f'''
        INSERT INTO user_task (task_id, user_id)
        VALUES ('{task_id}', '{user_id}');
    '''
    result = db_model.queryEdit(query)
    
    return result