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
