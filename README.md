<h1 align="center"> &#128013; Hexagonal architecture in Python</h1> 

<p align="center">
    Example of a <strong>Python application using Domain-Driven Design</strong> keeping the structure as simple as possible.
</p>

## Environment setup

### Needed tools

* [Install Docker](https://www.docker.com/get-started)
* Clone this repository `https://github.com/yulio94/python-ddd-example`
* Move to the root project folder: `cd python-ddd-example`

### Environment configuration

* Go to env_variables directory `cd compose/env_variables`
* Copy env files like this: `cp db.env.example db.env && cp rabbit.env.example rabbit.env`

### Run project

* Run `docker-compose up --build`
* Go to your browser and type `http://localhost:8001` or `http://localhost:8000`

## Special thanks to:

[CodelyTv](https://codely.tv/)