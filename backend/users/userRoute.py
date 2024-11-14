
from fastapi import APIRouter, Request
import users.userController as up

router = APIRouter()

@router.get("/")
async def get_user(request: Request):

    return up.get_user_controller(request.query_params)


@router.get("/tasks/")
async def get_user_tasks(request: Request):

    return up.get_user_tasks_controller(request.query_params)


@router.get("/users/")
async def get_users():

    return up.get_all_users_controller()


@router.post("/")
async def post_user(request: Request):
    
    return up.create_user_controller(request.query_params)
   

@router.patch("/")
async def patch_user(request: Request):
    
    return up.update_user_controller(request.query_params)


@router.delete("/")
async def delete_user(request: Request):
    
    return up.delete_user_controller(request.query_params)