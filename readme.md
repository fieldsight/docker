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
2. Run the containers
   ``` docker-compose -f docker-compose.backend.yaml -f docker-compose.frontend.yaml up -d ```


