
from db.dbController import DBModel

db_model = DBModel()

def update_sprint_action(sprint_id, attributes):

    set_clause = ', '.join([f"{key} = '{value}'" for key, value in attributes.items()])

    query = f'''
        UPDATE sprint
        SET {set_clause}
        WHERE id = {sprint_id};
    '''
    result = db_model.queryEdit(query)

    return result
