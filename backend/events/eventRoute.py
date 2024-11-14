
from fastapi import APIRouter, Request
import events.eventController as ec

router = APIRouter()

@router.get("/")
async def get_event(request: Request):

    return ec.get_event_controller(request.query_params)


@router.post("/")
async def post_event(request: Request):
    
    return ec.create_event_controller(request.query_params)
   
# @router.patch("/")
# async def patch_event(request: Request):
    
#     return ec.update_event_controller(request.query_params)


# @router.delete("/")
# async def delete_event(request: Request):
    
#     return ec.delete_event_controller(request.query_params)