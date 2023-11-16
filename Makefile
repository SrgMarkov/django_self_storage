up:
	docker compose -f infra/docker-compose.yaml up --build

down:
	docker compose -f infra/docker-compose.yaml down

django_bash:
	docker exec -it storage_django bash

collectstatic:
	docker exec -it storage_django ./manage.py collectstatic --noinput