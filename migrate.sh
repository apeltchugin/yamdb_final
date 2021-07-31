python manage.py makemigrations users --no-input
python manage.py makemigrations reviews --no-input
python manage.py makemigrations titles --no-input
python manage.py migrate --noinput
python manage.py collectstatic --no-input
gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
