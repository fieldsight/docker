# Environment variables

**All files within `./envfiles` folder should be copied to `current location(i.e. ./)`.** 

for unix users

``` cp -r ./envfiles/ ./ ```

They are only templates and must be modified to fit your needs.


Paths in composer files `../docker-compose.*.yml` are set to use this path.
If you want to use another path, be sure to update composer files.


For information on the Docker Compose environment files,
see: [https://docs.docker.com/compose/compose-file/#envfile](https://docs.docker.com/compose/compose-file/#envfile).
