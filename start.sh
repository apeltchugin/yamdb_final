python manage.py makemigrations users --no-input
python manage.py makemigrations reviews --no-input
python manage.py makemigrations titles --no-input
python manage.py migrate --noinput
python manage.py collectstatic --no-input
python manage.py loaddata  fixtures.json --no-input
