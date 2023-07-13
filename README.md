# crewer
Resource staffing app which allocates resources based on availability, skills, and schedule

## tech stack used

The project uses python as backend with the django framework for serving requests and the django rest framework to maintain restful standards

Postgres database is used to model the relations between various aspects of staffing

nginx is used to serve the backend and docker is used to make the deployment and sharing of code easier

- python
- django
- django-rest-framework
- postgres
- nginx
- docker

## Diagrams

model schema and the interaction diagrams can be found in the root of the project as 'database_diagram.png' and 'interaction_diagram.png'


## Docker deployment

the docker images are located at the given repository

https://hub.docker.com/repository/docker/thedoodler/crewer/tags?page=1&ordering=last_updated

To check out the server using docker
change into the deployment folder of the project

'''
cd deployment
docker compose up -d
'''

will start the application on port 8090

The project already has data for full functionality.

to test this use

http://localhost:8090/auth/login

resource1 - morbidgame1!
resource2 - gamidmorb1!

manager1 - morbidgame1!
manager2 - gamidmorb1!

mysuperuser - dundermuffin1!


## URL List

login - http://localhost:8090/auth/login
logout - http://localhost:8090/auth/logout
register - http://localhost:8090/auth/register/
profile - http://localhost:8090/auth/users/profile/
skills - http://localhost:8090/tasks/skills/
task list - http://localhost:8090/tasks/
project list - http://localhost:8090/projects/
project task list - http://localhost:8090/projects/tasks/1
project allocation - http://localhost:8090/projects/allocate/3/

\*each list can also be viewed in detail by adding the model number after the url


The postman collection can be founnd in the /crewer_postman directory