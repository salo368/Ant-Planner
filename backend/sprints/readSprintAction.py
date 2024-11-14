
from db.dbController import DBModel
from fastapi import HTTPException

db_model = DBModel()

def get_sprint_action(id):
    
    query = f'''
        SELECT sprint.*, project.name AS project_name
        FROM sprint
        JOIN project ON sprint.project_id = project.id
        WHERE sprint.id = {id};
    '''
    result = db_model.queryFetch(query)

    return result
    
def get_sprints_byProject_action(project_id):

    query = f'''
        SELECT * FROM sprint
        WHERE project_id = {project_id};
    '''
    result = db_model.queryFetch(query)

    return result
        
