.PHONY: test coverage

install:
	sudo docker-compose run --rm routine python -m pip install -r requirements-dev.txt --user --upgrade --no-warn-script-location

start:
	sudo docker-compose up routine

coverage:
	sudo docker-compose run --rm testroutine bash -c "python -m pytest --cov-report term --cov-report html:coverage --cov-config setup.cfg --cov=src/ test/"

daemon:
	sudo docker-compose up -d routine

test:
	sudo docker-compose run --rm testroutine

lint:
	sudo docker-compose run --rm routine bash -c "python -m flake8 ./src ./test"

safety:
	sudo docker-compose run --rm routine bash -c "python vendor/bin/safety check"

db/connect:
	sudo docker-compose exec db psql -Upostgres
