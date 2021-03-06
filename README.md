# ToDoList

ToDoList helps users organize tasks and not forgot about them.

### RUN DEVELOPMENT WITH DOCKERS
Please make sure you have docker version 19+ and docker-compose  1.26+

* To run with docker in development mode, you should 
set environment variables in file .env.dev
* Run following commands
```
cd .infrastructure/docker-compose/dev
docker-compose build
docker-compose up  
```

*  Create Super User for dev

For create super user run following command without down the container and set your credentials

```docker-compose exec development pipenv run python manage.py createsuperuser --email=admin@example.com --username=admin```

* Use django admin panel for create users  
http://localhost:8000/admin/

Only in dev mode (debug=True) you can  

* Use session auth for login in rest browsable api instead of jwt  
http://localhost:8000/api/v1/session-auth/login

* Use autogenerated swagger for see documentation  
http://localhost:8000/api/v1/docs/  
http://localhost:8000/api/v1/redoc/  

* Open http://localhost:8000/ in browser

### RUN PRODUCTION WITH DOCKERS

* To run with docker in production mode, you should 
set environment variables in file .env.prod
* Run following commands
```
cd .infrastructure/docker-compose/prod
docker-compose build
docker-compose up -d
```

*  Create Super User for prod

For create super user run following command without down the container and set your credentials

```docker-compose exec production pipenv run python manage.py createsuperuser --email=admin@example.com --username=admin```

* Run migrations
```
docker-compose exec production pipenv run python manage.py migrate --noinput
```

* Run tests
```
docker-compose exec production pipenv run python manage.py test --noinput
```

* Use django admin panel for create users  
http://localhost:1337/admin/  

* Open http://localhost:1337/ in browser
