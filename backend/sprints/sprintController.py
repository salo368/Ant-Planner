
from fastapi import HTTPException
from datetime import datetime
from sprints.readSprintAction import get_sprint_action
from sprints.createSprintAction import create_sprint_action
from sprints.updateSprintAction import update_sprint_action
from sprints.deleteSprintAction import delete_sprint_action
from projects.readProjectAction import get_project_action
from tasks.readTaskAction import get_tasks_bySprint_action

def get_sprint_controller(params):
    sprint_id = params.get('id')

    if not sprint_id:
        raise HTTPException(status_code=400, detail={"error": "Sprint ID is required."})

    sprintInfo = get_sprint_action(sprint_id)

    if not sprintInfo:  
        raise HTTPException(status_code=404, detail={"error": "No sprint found with the given ID."})

    return {"sprint": sprintInfo[0]}


def get_sprint_tasks_controller(params):
    sprint_id = params.get('id')

    if not sprint_id:
        raise HTTPException(status_code=400, detail={"error": "Sprint ID is required."})

    if not get_sprint_action(sprint_id):  
        raise HTTPException(status_code=404, detail={"error": "No sprint found with the given ID."})
    
    tasks = get_tasks_bySprint_action(sprint_id)

    return {"tasks": tasks}


def create_sprint_controller(params):
    required_keys = ['name', 'project_id', 'start_date', 'end_date']
    attributes = {key: value for key, value in params.items() if key in ['name', 'info', 'project_id', 'start_date', 'end_date']}
    missing_keys = [key for key in required_keys if key not in attributes or attributes[key] is None]

    if missing_keys:
        raise HTTPException(status_code=400, detail={"error": f"Required attributes: {', '.join(missing_keys)}."})
    
    def validate_date(date_str):
        for date_format in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
            try:
                return datetime.strptime(date_str, date_format)
            except ValueError:
                continue
        raise HTTPException(status_code=400, detail={"error": f"Invalid date format. Expected 'YYYY-MM-DD HH:MM:SS' or 'YYYY-MM-DD'."})

    if 'start_date' in attributes and attributes['start_date']:
        validate_date(attributes['start_date'])

    if 'end_date' in attributes and attributes['end_date']:
        validate_date(attributes['end_date'])

    project = get_project_action(attributes['project_id'])

    if not project:  
        raise HTTPException(status_code=404, detail={"error": "A valid project ID is required."})

    sprintInfo = create_sprint_action(attributes['name'], attributes.get('info', ''), attributes['project_id'], attributes.get('start_date', None),  attributes.get('end_date', None))
    
    return {"message": "Sprint created successfully"}


def update_sprint_controller(params):
    allowed_keys = ['name', 'info', 'start_date', 'end_date']
    sprint_id = params.get('id')
    
    if not sprint_id:
        raise HTTPException(status_code=400, detail={"error": "Sprint ID is required."})
    
    attributes = {key: value for key, value in params.items() if key in allowed_keys and value is not None}
    
    if not attributes:
        raise HTTPException(status_code=400, detail={"error": "Some attribute is required (name, info, start_date, end_date)."})
    
    sprint = get_sprint_action(sprint_id)

    if not sprint:  
        raise HTTPException(status_code=404, detail={"error": "No sprint found with the given ID."})
    
    def validate_date(date_str):
        for date_format in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
            try:
                return datetime.strptime(date_str, date_format)
            except ValueError:
                continue
        raise HTTPException(status_code=400, detail={"error": f"Invalid date format. Expected 'YYYY-MM-DD HH:MM:SS' or 'YYYY-MM-DD'."})

    if 'start_date' in attributes:
        validate_date(attributes['start_date'])

    if 'end_date' in attributes and attributes['end_date']:
        validate_date(attributes['end_date'])

    sprintInfo = update_sprint_action(sprint_id, attributes)
    
    return {"message": "Sprint updated successfully"}


def delete_sprint_controller(params):
    sprint_id = params.get('id')

    if not sprint_id:
        raise HTTPException(status_code=400, detail={"error": "Sprint ID is required."})
    
    sprint = get_sprint_action(sprint_id)

    if not sprint:  
        raise HTTPException(status_code=404, detail={"error": "No sprint found with the given ID."})

    sprintInfo = delete_sprint_action(sprint_id)

    return {"message": "Sprint deleted successfully"}