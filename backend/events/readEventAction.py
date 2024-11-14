
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def get_event_action(id):
        
    query = f'''
        SELECT * FROM calendar_event 
        WHERE id = {id};
    '''
    result = db_model.queryFetch(query)

    return result