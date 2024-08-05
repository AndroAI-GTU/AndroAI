all:
	docker compose up --build

clean:
	docker compose down

fclean:
	docker system prune -af
	rm -rf nest-app/node_modules
	rm -rf nest-app/dist
	rm -rf nest-app/tmp
	rm -rf react-app/node_modules
	rm -rf react-app/dist

re: clean all

.PHONY: all re clean