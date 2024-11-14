
from db.dbController import DBModel

db_model = DBModel()

def get_task_action(id):
        
    query = f'''
        SELECT * FROM task 
        WHERE id = {id};
    '''
    result = db_model.queryFetch(query)

    return result
 
def get_tasks_bySprint_action(sprint_id):

    query = f'''
        SELECT * FROM task
        WHERE sprint_id = {sprint_id};
    '''
    result = db_model.queryFetch(query)

    return result

def get_task_users_action(task_id):

    query = f'''
        SELECT u.* 
        FROM user_task ut
        JOIN user u ON ut.user_id = u.id
        WHERE task_id = {task_id};
    '''
    result = db_model.queryFetch(query)

    return result