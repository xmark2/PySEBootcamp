
### How to build and run container
    # sudo docker build -t myapp:latest .
    # sudo docker run -d --name ourfirstapplication -p 8080:8080 myfirstapp:latest

    ## all together
    # sudo docker rm myapp && sudo docker build -t myapp:latest . && sudo docker run --name myapp -p 8080:8080 myapp:latest


### How to stop container
    # sudo aa-remove-unknown
    # sudo docker kill myapp

### How to run docker-compose
    # sudo docker-compose up --build

### How to run docker-compose dameon mode
    # sudo docker-compose up --build -d

### How to run docker-compose dameon mode from folder/different path
    # sudo docker-compose -f testdc/docker-compose.yaml up -d

### How to stop docker-compose
    # sudo docker-compose down

## How to remove volume/database
    # sudo docker-compose down -v

## How to fix docker-compose down
    # sudo apt-get purge --auto-remove apparmor
    # sudo service docker restart
    # sudo docker system prune --all --volumes

## How to run test environment of docker-compose
    # sudo docker-compose exec -T app-test pytest tests

## How to run a service in dameon/background mode with docker-compose
    # sudo docker-compose up -d postgresdb
    # sudo docker-compose up -d servicename

## How to init alembic to continue Database as left?
    ## alembic init alembic

## How to start migrate with alembic?
    ## source .env-migrations-local
    ## alembic revision --autogenerate -m "Creating first tables"
    ## alembic upgrade head
    ## alembic downgrade -1

   