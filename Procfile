release: python manage.py makemigrations && python manage.py migrate --fake-initial
web: gunicorn icard.wsgi:application --bind 0.0.0.0:$PORT
