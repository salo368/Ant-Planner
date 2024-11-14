
from fastapi import APIRouter, Request
import sprints.sprintController as sc

router = APIRouter()

@router.get("/")
async def get_sprint(request: Request):

    return sc.get_sprint_controller(request.query_params)


@router.get("/tasks/")
async def get_sprint_tasks(request: Request):

    return sc.get_sprint_tasks_controller(request.query_params)


@router.post("/")
async def post_sprint(request: Request):
    
    return sc.create_sprint_controller(request.query_params)
   

@router.patch("/")
async def patch_sprint(request: Request):
    
    return sc.update_sprint_controller(request.query_params)


@router.delete("/")
async def delete_sprint(request: Request):
    
    return sc.delete_sprint_controller(request.query_params)