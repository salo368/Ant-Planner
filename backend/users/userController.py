
from fastapi import HTTPException
from users.readUserAction import get_user_action, get_all_users_action, get_user_tasks_action
from users.createUserAction import create_user_action
from users.updateUserAction import update_user_action
from users.deleteUserAction import delete_user_action

def get_user_controller(params):
    user_id = params.get('id')

    if not user_id:
        raise HTTPException(status_code=400, detail={"error": "User ID is required."})

    userInfo = get_user_action(user_id)

    if not userInfo:  
        raise HTTPException(status_code=404, detail={"error": "No user found with the given ID."})

    return {"user": userInfo[0]}

def get_all_users_controller():

    usersInfo = get_all_users_action()

    return {"users": usersInfo}

def get_user_tasks_controller(params):

    user_id = params.get('id')

    if not user_id:
        raise HTTPException(status_code=400, detail={"error": "User ID is required."})

    if not get_user_action(user_id):  
        raise HTTPException(status_code=404, detail={"error": "No user found with the given ID."})
    
    tasks = get_user_tasks_action(user_id)

    return {"tasks": tasks}


def create_user_controller(params):
    allowed_keys = ['name', 'last_name', 'email', 'password']

    attributes = {key: value for key, value in params.items() if key in allowed_keys}

    missing_keys = [key for key in allowed_keys if key not in attributes or attributes[key] is None]

    if missing_keys:
        raise HTTPException(status_code=400, detail={"error": f"Required attributes: {', '.join(missing_keys)}."})

    userInfo = create_user_action(attributes['name'], attributes['last_name'], attributes['email'], attributes['password'])
    
    return {"message": "User created successfully"}

def update_user_controller(params):

    allowed_keys = ['name', 'last_name', 'email', 'password']
    user_id = params.get('id')
    
    if not user_id:
        raise HTTPException(status_code=400, detail={"error": "User ID is required."})
    
    attributes = {key: value for key, value in params.items() if key in allowed_keys and value is not None}
    
    if not attributes:
        raise HTTPException(status_code=400, detail={"error": "Some attribute is required (name, last_name, email, password)."})
    
    user = get_user_action(user_id)

    if not user:  
        raise HTTPException(status_code=404, detail={"error": "No user found with the given ID."})
    
    userInfo = update_user_action(user_id, attributes)
    
    return {"message": "User updated successfully"}

def delete_user_controller(params):
    user_id = params.get('id')

    if not user_id:
        raise HTTPException(status_code=400, detail={"error": "User ID is required."})

    user = get_user_action(user_id)

    if not user:  
        raise HTTPException(status_code=404, detail={"error": "No user found with the given ID."})

    userInfo = delete_user_action(user_id)

    return {"message": "User deleted successfully"}