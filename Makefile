up:
	docker compose -f infra/docker-compose.yaml up --build

django_bash:
	docker exec -it storage_django bash

collectstatic:
	docker exec -it storage_django ./manage.py collectstatic --noinput