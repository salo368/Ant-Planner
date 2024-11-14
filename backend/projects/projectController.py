
from fastapi import HTTPException
from projects.readProjectAction import  get_all_projects_action, get_project_action, get_project_users_action, get_project_categories_action
from projects.createProjectAction import create_project_action, create_project_user_action, create_project_category_action
from projects.updateProjectAction import update_project_action, update_project_user_action, update_project_category_action
from projects.deleteProjectAction import delete_project_action, delete_project_user_action, delete_project_category_action
from sprints.readSprintAction import get_sprints_byProject_action
from users.readUserAction import get_user_action

def get_project_controller(params):
    project_id = params.get('id')

    if not project_id:
        raise HTTPException(status_code=400, detail={"error": "Project ID is required."})

    projectInfo = get_project_action(project_id)

    if not projectInfo:  
        raise HTTPException(status_code=404, detail={"error": "No project found with the given ID."})

    return {"project": projectInfo[0]}


def get_all_projects_controller():
    projectsInfo = get_all_projects_action()

    return {"projects": projectsInfo}


def get_project_sprints_controller(params):
    project_id = params.get('id')

    if not project_id:
        raise HTTPException(status_code=400, detail={"error": "Project ID is required."})

    projectInfo = get_project_action(project_id)

    if not projectInfo:  
        raise HTTPException(status_code=404, detail={"error": "No project found with the given ID."})
    
    sprintsData = get_sprints_byProject_action(project_id)

    return {"sprints": sprintsData}


def get_project_users_controller(params):
    project_id = params.get('id')

    if not project_id:
        raise HTTPException(status_code=400, detail={"error": "Project ID is required."})

    if not get_project_action(project_id):  
        raise HTTPException(status_code=404, detail={"error": "No project found with the given ID."})
    
    projectUsers = get_project_users_action(project_id)

    return {"users": projectUsers}


def get_project_category_controller(params):
    project_id = params.get('id')

    if not project_id:
        raise HTTPException(status_code=400, detail={"error": "Project ID is required."})

    if not get_project_action(project_id):  
        raise HTTPException(status_code=404, detail={"error": "No project found with the given ID."})
    
    projectCategories = get_project_categories_action(project_id)

    return {"categories": projectCategories}


def create_project_controller(params):
    required_keys = ['name']

    attributes = {key: value for key, value in params.items() if key in ['name', 'info']}

    missing_keys = [key for key in required_keys if key not in attributes or attributes[key] is None]

    if missing_keys:
        raise HTTPException(status_code=400, detail={"error": f"Required attributes: {', '.join(missing_keys)}."})

    projectInfo = create_project_action(attributes['name'], attributes.get('info', ''))
    
    return {"message": "Project created successfully"}


def create_project_user_controller(params):

    required_keys = ['id', 'user_id', 'role_id']

    attributes = {key: value for key, value in params.items() if key in required_keys}

    missing_keys = [key for key in required_keys if key not in attributes or attributes[key] is None]

    if missing_keys:
        raise HTTPException(status_code=400, detail={"error": f"Required attributes: {', '.join(missing_keys)}."})

    project_id = attributes.get('id')
    user_id = attributes.get('user_id')

    if not get_project_action(project_id):  
        raise HTTPException(status_code=404, detail={"error": "No project found with the given ID."})

    if not get_user_action(user_id):  
        raise HTTPException(status_code=404, detail={"error": "No user found with the given ID."})

    projectInfo = create_project_user_action(project_id, user_id, attributes.get('role_id'))

    return {"message": "User successfully added to the project."}


def create_project_category_controller(params):
    
    required_keys = ['name', 'id']

    attributes = {key: value for key, value in params.items() if key in ['name', 'info', 'id']}

    missing_keys = [key for key in required_keys if key not in attributes or attributes[key] is None]

    if missing_keys:
        raise HTTPException(status_code=400, detail={"error": f"Required attributes: {', '.join(missing_keys)}."})
    
    if not get_project_action(attributes['id']):  
        raise HTTPException(status_code=404, detail={"error": "No project found with the given ID."})
    
    projectInfo = create_project_category_action(attributes['id'], attributes['name'], attributes.get('info', ''))

    return {"message": "Project category created successfully"}


def update_project_controller(params):
    allowed_keys = ['name', 'info']
    project_id = params.get('id')
    
    if not project_id:
        raise HTTPException(status_code=400, detail={"error": "Project ID is required."})
    
    attributes = {key: value for key, value in params.items() if key in allowed_keys and value is not None}
    
    if not attributes:
        raise HTTPException(status_code=400, detail={"error": "Some attribute is required (name, info)."})
    
    project = get_project_action(project_id)

    if not project:  
        raise HTTPException(status_code=404, detail={"error": "No project found with the given ID."})

    projectInfo = update_project_action(project_id, attributes)
    
    return {"message": "Project updated successfully"}


def update_project_category_controller(params):
    allowed_keys = ['name', 'info']
    category_id = params.get('category_id')
    
    if not category_id:
        raise HTTPException(status_code=400, detail={"error": "Category ID is required."})
    
    attributes = {key: value for key, value in params.items() if key in allowed_keys and value is not None}
    
    if not attributes:
        raise HTTPException(status_code=400, detail={"error": f"Some attribute is required ({', '.join(allowed_keys)})."})
    
    #Validar que exista la categoria

    projectInfo = update_project_category_action(category_id, attributes)
    
    return {"message": "Project category updated successfully"}


def update_project_user_controller(params):

    required_keys = ['id', 'user_id', 'role_id']

    attributes = {key: value for key, value in params.items() if key in required_keys}

    missing_keys = [key for key in required_keys if key not in attributes or attributes[key] is None]

    if missing_keys:
        raise HTTPException(status_code=400, detail={"error": f"Required attributes: {', '.join(missing_keys)}."})

    project_id = attributes.get('id')
    user_id = attributes.get('user_id')

    if not get_project_action(project_id):  
        raise HTTPException(status_code=404, detail={"error": "No project found with the given ID."})

    if not get_user_action(user_id):  
        raise HTTPException(status_code=404, detail={"error": "No user found with the given ID."})

    projectInfo = update_project_user_action(project_id, user_id, attributes.get('role_id'))

    return {"message": "User role successfully updated."}


def delete_project_controller(params):
    project_id = params.get('id')

    if not project_id:
        raise HTTPException(status_code=400, detail={"error": "Project ID is required."})
    
    project = get_project_action(project_id)

    if not project:  
        raise HTTPException(status_code=404, detail={"error": "No project found with the given ID."})

    projectInfo = delete_project_action(project_id)

    return {"message": "Project deleted successfully"}


def delete_project_user_controller(params):

    required_keys = ['id', 'user_id']

    attributes = {key: value for key, value in params.items() if key in required_keys}

    missing_keys = [key for key in required_keys if key not in attributes or attributes[key] is None]

    if missing_keys:
        raise HTTPException(status_code=400, detail={"error": f"Required attributes: {', '.join(missing_keys)}."})

    project_id = attributes.get('id')
    user_id = attributes.get('user_id')

    if not get_project_action(project_id):  
        raise HTTPException(status_code=404, detail={"error": "No project found with the given ID."})

    if not get_user_action(user_id):  
        raise HTTPException(status_code=404, detail={"error": "No user found with the given ID."})

    projectInfo = delete_project_user_action(project_id, user_id)

    return {"message": "User successfully removed from the project."}


def delete_project_category_controller(params):

    category_id = params.get('category_id')

    if not category_id:
        raise HTTPException(status_code=400, detail={"error": "Category ID is required."})

    categoryInfo = delete_project_category_action(category_id)

    return {"message": "Category successfully removed from the project."}

