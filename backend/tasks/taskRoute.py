
from fastapi import APIRouter, Request
import tasks.taskController as tp

router = APIRouter()

@router.get("/")
async def get_task(request: Request):

    return tp.get_task_controller(request.query_params)


@router.get("/users/")
async def get_task_users(request: Request):

    return tp.get_task_users_controller(request.query_params)


@router.post("/")
async def post_task(request: Request):
    
    return tp.create_task_controller(request.query_params)
   

@router.post("/user/")
async def post_task_user(request: Request):
    
    return tp.create_task_user_controller(request.query_params)

@router.patch("/")
async def patch_task(request: Request):
    
    return tp.update_task_controller(request.query_params)


@router.delete("/")
async def delete_task(request: Request):
    
    return tp.delete_task_controller(request.query_params)


@router.delete("/user/")
async def delete_task_user(request: Request):
    
    return tp.delete_task_user_controller(request.query_params)