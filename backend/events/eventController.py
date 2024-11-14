
from fastapi import HTTPException
from datetime import datetime
from events.readEventAction import get_event_action
from events.createEventAction import create_event_action
from users.updateUserAction import update_user_action
from users.deleteUserAction import delete_user_action
from sprints.readSprintAction import get_sprint_action
from users.readUserAction import get_user_action

def get_event_controller(params):
    event_id = params.get('id')

    if not event_id:
        raise HTTPException(status_code=400, detail={"error": "Event ID is required."})

    eventInfo = get_event_action(event_id)

    if not eventInfo:  
        raise HTTPException(status_code=404, detail={"error": "No event found with the given ID."})

    return {"event": eventInfo[0]}


def create_event_controller(params):
    required_keys = ['name', 'sprint_id', 'user_host_id', 'start_date', 'end_date']
    attributes = {key: value for key, value in params.items() if key in ['name', 'info', 'sprint_id', 'user_host_id', 'start_date', 'end_date']}
    missing_keys = [key for key in required_keys if key not in attributes or attributes[key] is None]

    if missing_keys:
        raise HTTPException(status_code=400, detail={"error": f"Required attributes: {', '.join(missing_keys)}."})
    
    if not get_sprint_action(attributes['sprint_id']):  
        raise HTTPException(status_code=404, detail={"error": "A valid sprint ID is required."})
    
    if not get_user_action(attributes['user_host_id']):  
        raise HTTPException(status_code=404, detail={"error": "A valid user ID is required."})
    
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

    create_event_action(attributes['name'], attributes.get('info', ''), attributes['sprint_id'],  attributes['user_host_id'],  attributes.get('start_date', None),  attributes.get('end_date', None))
    
    return {"message": "Calendar event created successfully"}


# def update_event_controller(params):
#     allowed_keys = ['name', 'info', 'start_date', 'end_date']
#     event_id = params.get('id')
#     attributes = {key: value for key, value in params.items() if key in allowed_keys and value is not None}

#     if not event_id:
#         raise HTTPException(status_code=400, detail={"error": "Event ID is required."})

#     def validate_date(date_str):
#         for date_format in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
#             try:
#                 return datetime.strptime(date_str, date_format)
#             except ValueError:
#                 continue
#         raise HTTPException(status_code=400, detail={"error": f"Invalid date format. Expected 'YYYY-MM-DD HH:MM:SS' or 'YYYY-MM-DD'."})
    
#     if not attributes:
#         raise HTTPException(status_code=400, detail={"error": f"Some attribute is required ({', '.join(allowed_keys)})."})

#     if 'start_date' in attributes and attributes['start_date']:
#         validate_date(attributes['start_date'])

#     if 'end_date' in attributes and attributes['end_date']:
#         validate_date(attributes['end_date'])
    
#     task = get_task_action(task_id)

#     if not task:  
#         raise HTTPException(status_code=404, detail={"error": "No task found with the given ID."})
    
#     userInfo = update_task_action(task_id, attributes)
    
#     return {"message": "Calendar event updated successfully"}
    

# def delete_user_controller(params):
#     user_id = params.get('id')

#     if not user_id:
#         raise HTTPException(status_code=400, detail={"error": "User ID is required."})

#     user = get_user_action(user_id)

#     if not user:  
#         raise HTTPException(status_code=404, detail={"error": "No user found with the given ID."})

#     userInfo = delete_user_action(user_id)

#     return {"message": "User deleted successfully"}