lint:
	uv run pre-commit run --all-files

makemigrations:
	uv run src/djangoproject/manage.py makemigrations

migrate:
	uv run src/djangoproject/manage.py migrate

createsuperuser:
	uv run src/djangoproject/manage.py createsuperuser

run:
	uv run src/djangoproject/manage.py runserver
