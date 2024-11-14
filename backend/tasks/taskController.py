
from fastapi import HTTPException
from datetime import datetime
from tasks.readTaskAction import get_task_action, get_task_users_action
from tasks.createTaskAction import create_task_action, create_task_user_action
from tasks.updateTaskAction import update_task_action
from tasks.deleteTaskAction import delete_task_action, delete_task_user_action
from users.readUserAction import get_user_action
from sprints.readSprintAction import get_sprint_action

def get_task_controller(params):
    task_id = params.get('id')

    if not task_id:
        raise HTTPException(status_code=400, detail={"error": "Task ID is required."})

    taskInfo = get_task_action(task_id)

    if not taskInfo:  
        raise HTTPException(status_code=404, detail={"error": "No task found with the given ID."})

    return {"task": taskInfo[0]}


def get_task_users_controller(params):
    task_id = params.get('id')

    if not task_id:
        raise HTTPException(status_code=400, detail={"error": "Task ID is required."})

    task = get_task_action(task_id)

    if not task:  
        raise HTTPException(status_code=404, detail={"error": "No task found with the given ID."})
    
    users = get_task_users_action(task_id)

    return {"users": users}


def create_task_controller(params):
    required_keys = ['sprint_id', 'name', 'task_type_id']
    attributes = {key: value for key, value in params.items() if key in ['sprint_id', 'name', 'info', 'start_date', 'end_date', 'task_type_id', 'category_id', 'state_id']}
    missing_keys = [key for key in required_keys if key not in attributes or attributes[key] is None]

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

    if missing_keys:
        raise HTTPException(status_code=400, detail={"error": f"Required attributes: {', '.join(missing_keys)}."})
    
    if not get_sprint_action(attributes['sprint_id']):  
        raise HTTPException(status_code=404, detail={"error": "A valid sprint ID is required."})

    projectInfo = create_task_action(attributes['sprint_id'], attributes['name'], attributes.get('info', '') , attributes.get('start_date', None),  attributes.get('end_date', None),  attributes.get('task_type_id', ''), attributes.get('category_id', None), attributes.get('state_id', '1'))
    
    return {"message": "Task created successfully"}


def create_task_user_controller(params):
    required_keys = ['id', 'user_id']
    attributes = {key: value for key, value in params.items() if key in ['id', 'user_id']}
    missing_keys = [key for key in required_keys if key not in attributes or attributes[key] is None]

    if missing_keys:
        raise HTTPException(status_code=400, detail={"error": f"Required attributes: {', '.join(missing_keys)}."})
    
    if not get_task_action(attributes['id']):  
        raise HTTPException(status_code=404, detail={"error": "A valid task ID is required."})
    
    if not get_user_action(attributes['user_id']):  
        raise HTTPException(status_code=404, detail={"error": "A valid user ID is required."})

    create_task_user_action(attributes['id'], attributes['user_id'])
    
    return {"message": "Task assigned to user successfully"}


def update_task_controller(params):

    allowed_keys = ['name', 'info', 'start_date', 'end_date', 'task_type_id', 'category_id', 'state_id']
    task_id = params.get('id')
    attributes = {key: value for key, value in params.items() if key in allowed_keys and value is not None}

    if not task_id:
        raise HTTPException(status_code=400, detail={"error": "Task ID is required."})

    def validate_date(date_str):
        for date_format in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
            try:
                return datetime.strptime(date_str, date_format)
            except ValueError:
                continue
        raise HTTPException(status_code=400, detail={"error": f"Invalid date format. Expected 'YYYY-MM-DD HH:MM:SS' or 'YYYY-MM-DD'."})
    
    if not attributes:
        raise HTTPException(status_code=400, detail={"error": f"Some attribute is required ({', '.join(allowed_keys)})."})

    if 'start_date' in attributes and attributes['start_date']:
        validate_date(attributes['start_date'])

    if 'end_date' in attributes and attributes['end_date']:
        validate_date(attributes['end_date'])
    
    task = get_task_action(task_id)

    if not task:  
        raise HTTPException(status_code=404, detail={"error": "No task found with the given ID."})
    
    userInfo = update_task_action(task_id, attributes)
    
    return {"message": "Task updated successfully"}


def delete_task_controller(params):
    task_id = params.get('id')

    if not task_id:
        raise HTTPException(status_code=400, detail={"error": "Task ID is required."})

    task = get_task_action(task_id)

    if not task:  
        raise HTTPException(status_code=404, detail={"error": "No task found with the given ID."})

    taskInfo = delete_task_action(task_id)

    return {"message": "Task deleted successfully"}


def delete_task_user_controller(params):
    required_keys = ['id', 'user_id']
    attributes = {key: value for key, value in params.items() if key in ['id', 'user_id']}
    missing_keys = [key for key in required_keys if key not in attributes or attributes[key] is None]

    if missing_keys:
        raise HTTPException(status_code=400, detail={"error": f"Required attributes: {', '.join(missing_keys)}."})
    
    if not get_task_action(attributes['id']):  
        raise HTTPException(status_code=404, detail={"error": "A valid task ID is required."})
    
    if not get_user_action(attributes['user_id']):  
        raise HTTPException(status_code=404, detail={"error": "A valid user ID is required."})

    delete_task_user_action(attributes['id'], attributes['user_id'])

    return {"message": "User deleted from task successfully"}