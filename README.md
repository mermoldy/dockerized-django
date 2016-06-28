## Django Development With Docker Compose

### Dependencies:

- docker-compose
- fabric


### Run locally

1. Build images - `docker-compose build`
1. Start services - `docker-compose up -d`
1. Go to shell - `docker-compose run django bash`


### Deploy

1. fab --hosts='example.com' deploy