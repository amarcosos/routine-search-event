.PHONY: test coverage

install:
	sudo docker-compose run --rm server python -m pip install -r requirements-dev.txt --user --upgrade --no-warn-script-location

start:
	sudo docker-compose up server

debug:
	sudo docker-compose run --rm server bash -c "python src/main.py --debug"

coverage:
	sudo docker-compose run --rm testserver bash -c "python -m pytest --cov-report term --cov-report html:coverage --cov-config setup.cfg --cov=src/ test/"

daemon:
	sudo docker-compose up -d server

test:
	sudo docker-compose run --rm testserver

lint:
	sudo docker-compose run --rm server bash -c "python -m flake8 ./src ./test"

safety:
	sudo docker-compose run --rm server bash -c "python vendor/bin/safety check"

db/connect:
	sudo docker-compose exec db psql -Upostgres
