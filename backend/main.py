
from fastapi import FastAPI
from users.userRoute import router as user_router  
from projects.projectRoute import router as project_router  
from sprints.sprintRoute import router as sprint_router  
from tasks.taskRoute import router as task_router
from events.eventRoute import router as event_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Ruta principal de la API"}

app.include_router(project_router, prefix="/project")
app.include_router(sprint_router, prefix="/sprint")
app.include_router(task_router, prefix="/task")
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")