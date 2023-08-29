# mini-blogger
An app for posting thoughts, news, and more.

## Setting up Development Environment

### Install Docker

### Make sure docker is running

### Run docker-compose up --build

### Visit localhost:8000 to see django instance

### Running django manage commands

You need to connect to the docker instance and then run the command. This allows you to use the correct package versions as 
defined in the docker container.

`docker-compose exec backend bash` to get shell.

From this shell you can run any docker management commands. Note that these commands are not persistent.

## Deploying to Production Environment
