
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def create_sprint_action(name, info, project_id, start_date, end_date):
    
    query = f'''
        INSERT INTO sprint (project_id, name, info, start_date, end_date)
        VALUES ('{project_id}', '{name}', '{info}', {f"'{start_date}'" if start_date is not None else 'NULL'}, {f"'{end_date}'" if end_date is not None else 'NULL'});
    '''
    result = db_model.queryEdit(query)
    
    return result
        
    