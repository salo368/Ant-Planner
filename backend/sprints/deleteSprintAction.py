
from db.dbController import DBModel

db_model = DBModel()

def delete_sprint_action(sprint_id):
    
    query = f'''
        DELETE FROM sprint
        WHERE id = {sprint_id};
    '''
    result = db_model.queryEdit(query)

    return result
