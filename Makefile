RED=\033[0;31m
BLUE=\033[0;34m
NC=\033[0m

all:
	docker compose -f ./Compose/docker-compose.yml up -d --build;
down:
	docker compose -f ./Compose/docker-compose.yml down;

re: fclean all

clean:
	docker compose -f ./Compose/docker-compose.yml -v --remove-orphans

fclean: down
	docker system prune -af

.PHONY: all down re clean fclean