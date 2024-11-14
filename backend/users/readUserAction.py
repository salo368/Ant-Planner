
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def get_user_action(id):
        
    query = f'''
        SELECT * FROM user 
        WHERE id = {id};
    '''
    result = db_model.queryFetch(query)

    return result
 
    
def get_all_users_action():

    query = f'''
        SELECT * FROM user;
    '''
    result = db_model.queryFetch(query)

    return result


def get_user_tasks_action(user_id):

    query = f'''
        SELECT t.* 
        FROM user_task ut
        JOIN task t ON ut.task_id = t.id
        WHERE user_id = {user_id};
    '''
    result = db_model.queryFetch(query)

    return result