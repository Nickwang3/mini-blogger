# mini-blogger
An app for posting thoughts, news, and more.

## Setting up Development Environment

### Install Docker

### Run docker-compose up --build

### Visit localhost:8000 to see django instance

### Running django admin commands to create new apps

You need to connect to the docker instance and then run the command. This allows you to use the correct package versions as 
defined in the docker container.

`docker-compose exec backend bash` to get shell.
`python3 backend/manage.py startapp <app_name>` to create a new app with the files generated.

## Deploying to Production Environment
