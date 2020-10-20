release: python manage.py migrate --noinput
  web: gunicorn shore.wsgi --log-file -
