# Mongo-Docker-Flask
A simple flask server based application for collecting data, storing and retrieving it from a Mongo Database
### Pull Mongo DB image
```
docker pull mongo:4.2
```
### Create mongo db container and start mongo server
```
docker run -d --name=mongo-db --expose=27017 mongo:4.2 
docker run -d -p 27017:27017 --name test-mongo mongo:latest
```
