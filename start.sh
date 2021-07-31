sudo python manage.py makemigrations users --no-input
sudo python manage.py makemigrations reviews --no-input
sudo python manage.py makemigrations titles --no-input
sudo python manage.py migrate --noinput
sudo python manage.py collectstatic --no-input
sudo python manage.py loaddata  fixtures.json --no-input
sudo gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000