This project is no longer maintained!
=======================

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
 4. Memcached
 5. Celery
 


Setting up docker
==================

1. Copy the sample envfiles from envfiles folder and edit with valid credintials

	``` cp -r ./envfiles/ ./ ```

2. Change the value in envfiles. envfiles folder consists of two environment file db.txt for database config and env.txt for system config. Please change as required.

3. Get inside the nginx folder and change servername as required

   ``` cd nginx ```
   
4. Change the glcoud credintials. Filedsight uses the google bucket storage to store  
  media file, Google drive and sheet services for reports and auto sync data to sheets.

   ```
     cd ./fixes
     cp credentials_sample.json ./credentials.json
     cp service_account_sample.json ./service_account.json
     cp settings_sample.yaml ./settings.yaml
     
   ```
   Replace the content of copy of sample with actual project credentails.

5. Run the containers

   ``` docker-compose -f docker-compose.backend.yaml -f docker-compose.frontend.yaml up -d ```

6. Check all containers are up

   ``` docker ps -a ``` 
   
7. Run migration inside fieldsight_web container

  ``` docker run -it fieldsight_web bash 
      python manage.py migrate
  ```
8. create the default user

 ```
      docker run -it fieldsight_web bash 
      python manage.py fieldsight_default_commands
      python manage.py create_default_superuser
```
This will create the default user name and password

  username: admin
  password: 123456

#### Basic troubleshooting

- Failing the postgres to up can cause the migration fail and shows the internal 
  server error display in browser. Check if postgres is running or not

  ``` docker inspect -f '{{.State.Running}}' fieldsight_postgis ```

- If Enketo keeps on failing, see the docker log

  ``` docker logs -f --tail 100 fieldsight_enketo ```

- Enketo failed to up if it donot find the config files. Make sure the config file 
  exists in ```./fixes/config.json ``` . Another reason for enketo failing is if it doesnot find the redis host. Make sure to add the redis service name as host in ```config.json```

- If nginx is already running on local machine stop it as the nginx is used here for 
  reverse proxy. Check status

  ``` sudo service nginx status ```

- Stop nginx 

  ``` sudo service nginx stop ```

  Alternatively, it can be avoided by changing the port mount in 
  ``` docker-compose-frontend.yaml ``` for nginx.

- For permission issues in credintials json files in ``` ./fixes/gloud/ ```

  ``` sudo chmod -R +x ./fixes/gcloud/. ```




