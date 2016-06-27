## Django Development With Docker Compose

### Dependencies:

- docker-compose
- fabric


### Instructions

1. Build images - `docker-compose build`
1. Start services - `docker-compose up -d`
1. Create migrations - `docker-compose run web /usr/local/bin/python manage.py migrate`


### Deploy

1. fab --hosts='example.com' deploy