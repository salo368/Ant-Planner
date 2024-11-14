# Base de Datos - Estructura de Tablas

## Tablas

### User
Esta tabla almacena la información de los usuarios registrados en el sistema.

- **id** (id)
- **name** (string)
- **last_name** (string)
- **email** (string) \<unique\>
- **password** (string) -hash-

### User_Project
Esta tabla vincula usuarios con proyectos y define su rol dentro de los mismos.

- **user_id** (id) --> User
- **project_id** (id) --> Project
- **role_id** (id) --> Role

### Role
Esta tabla define los roles que pueden asumir los usuarios en los proyectos.

#### Types: OWNER/MANAGER/LEADER/DEV

- **id**: (id)
- **name** (string) \<unique\>
- **info** (string)

### User_Task
Esta tabla relaciona usuarios con tareas en un proyecto.

- **project_id** (id) --> Project
- **user_id** (id) --> User
- **task_id** (id) --> Task

### Task_type
Esta tabla define los tipos de tareas disponibles en el sistema.

#### Types: NEW/BUG/UPDATE/TEST/IMPROVE/DOC

- **id** (id)
- **name** (string) \<unique\>
- **info** (string)

### Task
Esta tabla almacena la información relacionada con las tareas del proyecto.

- **id** (id)
- **project_id** (id) --> Project
- **sprint_id** (id) --> Sprint
- **name** (string) \<unique per project\>
- **info** (string)
- **end_date** (date)
- **task_type_id** (id) --> Task
- **category_id** (id) --> Category
- **approx_duration** (time)
- **state_id** (id) --> State

### Project
Esta tabla almacena la información de los proyectos.

- **id** (id)
- **name** (string)
- **info** (string)

### Task_dependency
Esta tabla define las dependencias entre tareas.

- **task_prev_id** (id) --> Task
- **task_next_id** (id) --> Task

### Sprint
Esta tabla almacena la información de los sprints dentro de un proyecto.

- **id** (id)
- **project_id** (id) --> Project
- **name** (string)
- **number** (int) \<unique per project\>
- **info** (string)
- **start_date** (date)
- **end_date** (date)

### Category
Esta tabla define las categorías de las tareas dentro de un proyecto.

- **id** (id)
- **project_id** (id) --> Project
- **name** (string) \<unique per project\>
- **info** (string)

### State
Esta tabla almacena los diferentes estados que pueden tener las tareas.

#### Types: TO DO/IN PROGRESS/PAUSED/VERIFY/DONE/

- **id** (id)
- **name** (string) \<unique\>
- **info** (string)

### Calendar_event
Esta tabla almacena los eventos calendario de un proyecto.

- **id** (id)
- **project_id** (id) --> Project
- **name** (string)
- **info** (string)
- **user_host_id** (id) --> User
- **start_date** (date)
- **end_date** (date)

### User_Calendar_event
Esta tabla relaciona usuarios con eventos calendario de un proyecto.

- **calendar_event_id** (id) --> Calendar_event
- **user_id** (id) --> User
