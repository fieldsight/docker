#ssl certificate for local configuration

To enable the https for the development i.e. for test run the following command to create the ssl certificate. Sample localhost.conf is inside certs folder. Donot copy the sample certificate file, create one.

```
 sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt -config localhost.conf
```
Copy the certificate file to /etc/ssl/certs

``` cp localhost.crt /etc/ssl/certs/
    cp localhost.key /etc/ssl/private/
```



