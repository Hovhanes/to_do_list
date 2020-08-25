# ToDoList

ToDoList helps users organize tasks and not forgot about them.

### RUN WITH DOCKERS
Please make sure you have docker version 19+ and docker-compose  1.26+

* To run with docker in development mode, you should 
set environment variables in file .env (please set POSTGRES_DB=postgres) and
.infrastructure/docker-compose/dev/.env 
* Run following commands
```
cd .infrastructure/docker-compose/dev
docker-compose build
docker-compose up
```

### Create Super User

For create super user run following command and set your credentials

```docker-compose exec development pipenv run python manage.py createsuperuser --email=admin@example.com --username=admin```

# API

### POST /api/v1/tasks
Create Task API

| Body | Description |
| ------ | ------ |
| title | Title |
| description | Description |
| is_done | Is Done boolean field which show task status |
| user | User Id |

### DELETE /api/v1/task/{id}
Delete Task API

| Url Variable | Description |
| ------ | ------ |
| id | Task Id |

### GET /api/v1/tasks/?is_done=true
Get Tasks List API

| Query | Description |
| ------ | ------ |
| is_done | true/false optional parameter for filtering with status |

### GET /api/v1/tasks/{id}
Get Task Detail API

| Url Variable | Description |
| ------ | ------ |
| id | Task ID |


### PUT /api/v1/task/{id}
Update Task API

| Url Variable | Description |
| ------ | ------ |
| id | Task ID |

| Body | Description |
| ------ | ------ |
| title | Title |
| description | Description |
| is_done | Is Done boolean field which show task status |
| user | User Id |

### PATCH /api/v1/task/{id}
Particular Task Update API

| Url Variable | Description |
| ------ | ------ |
| id | Task ID |

| Body | Description |
| ------ | ------ |
| is_done | Is Done boolean field which show task status |

