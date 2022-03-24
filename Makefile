run:
	@docker-compose -f docker-compose.yml up

down:
	@docker-compose -f docker-compose.yml down -v

requirements:
	@poetry export -o requirements.txt --without-hashes --dev

migrate:
	@python manage.py migrate

test:
	@docker exec -it testbackend_container python manage.py test parking_api.apps.parking
