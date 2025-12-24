lint:
	python -m pre_commit run --all-files

makemigrations:
	uv run src/django_project/manage.py makemigrations

migrate:
	uv run src/django_project/manage.py migrate

createsuperuser:
	uv run src/django_project/manage.py createsuperuser
