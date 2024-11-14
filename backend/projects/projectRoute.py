
from fastapi import APIRouter, Request
from projects import projectController as pc

router = APIRouter()

@router.get("/")
async def get_project(request: Request):
    return pc.get_project_controller(request.query_params)

@router.get("/projects/")
async def get_projects():
    return pc.get_all_projects_controller()

@router.get("/users/")
async def get_projects(request: Request):
    return pc.get_project_users_controller(request.query_params)

@router.get("/sprints/")
async def get_projects_sprints(request: Request):
    return pc.get_project_sprints_controller(request.query_params)

@router.get("/categories/")
async def get_projects_categories(request: Request):
    return pc.get_project_category_controller(request.query_params)

@router.post("/")
async def post_project(request: Request):
    return pc.create_project_controller(request.query_params)

@router.post("/user/")
async def post_project_user(request: Request):
    return pc.create_project_user_controller(request.query_params)

@router.post("/category/")
async def post_project_category(request: Request):
    return pc.create_project_category_controller(request.query_params)

@router.patch("/")
async def patch_project(request: Request):
    return pc.update_project_controller(request.query_params)

@router.patch("/user/")
async def patch_project_user(request: Request):
    return pc.update_project_user_controller(request.query_params)

@router.patch("/category/")
async def patch_project_category(request: Request):
    return pc.update_project_category_controller(request.query_params)

@router.delete("/")
async def delete_project(request: Request):
    return pc.delete_project_controller(request.query_params)

@router.delete("/user/")
async def delete_project_user(request: Request):
    return pc.delete_project_user_controller(request.query_params)

@router.delete("/category/")
async def delete_project_category(request: Request):
    return pc.delete_project_category_controller(request.query_params)
