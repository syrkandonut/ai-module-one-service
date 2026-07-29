EXEC = docker exec -it 
LOGS = docker logs
ENV = --env-file .env
COMPOSE_FILE = docker/docker-compose.yml
APP_CONTAINER = app-backend

.PHONY: build
build: 
	docker compose -f ${COMPOSE_FILE} ${ENV} up --build -d

.PHONY: down
down:
	docker compose -f ${COMPOSE_FILE} ${ENV} down

.PHONY: shell
shell:
	${EXEC} ${APP_CONTAINER} bash

.PHONY: logs
logs:
	docker logs ${APP_CONTAINER} -f