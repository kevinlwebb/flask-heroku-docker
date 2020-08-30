# Docker Application

## Local Testing Instructions

1. Change into the `app` directory
```
cd app
```
2. Build based on `Docker` file
```
docker build -t flask-template:latest .
```
3. Start Docker application
```
docker run -d -p 5000:5000 flask-template
```
4. Check status of Docker applications
```
docker ps -a
```
5. Stop application
```
docker stop [YOUR CONTAINER NUMBER HERE]
```

or

1. Set current directory and project directy
2. Start with Docker Compose
```
docker-compose up
```
3. To rebuild this image you must use 
```
docker-compose build
```
or 
```
docker-compose up --build
```


## Upload to Heroku

1. Sign in
```
heroku container:login
```
2. Create Heroku application
```
heroku create creativeappname
```
3. Change into the `dockerapp` directory
```
cd dockerapp
```
4. Push contents to Heroku
```
heroku container:push web --app creativeappname
```
5. Release contents to Heroku
```
heroku container:release web --app creativeappname
```
6. Check out your website: https://creativeappname.herokuapp.com

## Resources
- [Simple Guide for Docker Flask](https://codefresh.io/docker-tutorial/hello-whale-getting-started-docker-flask/)
- [Containerise your Python Flask using Docker and deploy it onto Heroku](https://medium.com/@ksashok/containerise-your-python-flask-using-docker-and-deploy-it-onto-heroku-a0b48d025e43)
- [How To Set Up Flask with MongoDB and Docker](https://www.digitalocean.com/community/tutorials/how-to-set-up-flask-with-mongodb-and-docker)