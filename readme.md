[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Fieldsight Docker 
=======================


**Front end services**

 1. Fieldsight
 2. Fieldsight Form-builder
 3. Enketo 
 4. Nginx proxy server

**Backend services**

 1. Mongo
 2. Postgis(postgres extension)
 3. Redis

Setting up docker
==================

1. Copy the sample envfiles from envfiles folder and edit with valid credintials
	``` cp -r ./envfiles/ ./ ```

2. Change the value in envfiles. envfiles folder consists of two environment file db.txt for database config and env.txt for system config. Please change as required.

3. Run the containers
   ``` docker-compose -f docker-compose.backend.yaml -f docker-compose.frontend.yaml up -d ```

4. Check all containers are up
   ``` docker ps -a ``` 

#### Basic troubleshooting

Sometimes if the migration fails inside the container, it fails to start. Make sure the postgres container is running and to migrate in the fieldisht_web container

``` docker run -it fieldsight_web bash 
	python manage.py migrate
```

To create the default user to login
```
	docker run -it fieldsight_web bash 
	python manage.py fieldsight_default_commands
    python manage.py create_default_superuser

```

This will create the default user name and password

> username: admin
> password: 123456




