FROM nginx:1.17.6

RUN apt-get update --fix-missing && \
  apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY fieldsight-docker/nginx/* /etc/nginx/conf.d/

