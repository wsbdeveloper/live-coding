
# application dev
run-flask-dev:
	@poetry run python app.py

# application prd
gunicorn-prod:
	@gunicorn -w 2 app.py -b 0.0.0.0:443


# builders
docker-up:
	docker-compose up -d

docker-down:
	docker-compose down