# Mongo-Docker-Flask
A simple flask server based application for collecting, storing, updating and retrieving data from a Mongo Database.
The application uses Flask server to render dynamic webpages and MongoDB database service to store information

Application needs Docker and a MongoDB service container running in Docker
### Install Docker
[Install Docker](https://docs.docker.com/desktop/windows/install/)
### Pull Mongo DB image
```
docker pull mongo:latest
```
### Create mongo db container and start mongo server
```
docker run -d -p 27017:27017 --name test-mongo mongo:latest
```
### install required libraries
```
python3 -m pip install -r requirments.txt
```
### Now run the application
```
python3 app.py 
```
### navigate to the application main home page
```
http://localhost:5000/
```

