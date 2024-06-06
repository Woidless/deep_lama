run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

restartdb:
	python manage.py makemigrations account
	python manage.py makemigrations base
	python manage.py makemigrations statement
	python manage.py makemigrations django_bot
	python manage.py migrate
	python manage.py createsuperuser

daemon:
	celery -A config multi start worker1 \
    --pidfile="$HOME/run/celery/%n.pid" \
    --logfile="$HOME/log/celery/%n%I.log"

celery:
	celery -A config worker -l info