sudo python manage.py makemigrations users --no-input
sudo python manage.py makemigrations reviews --no-input
sudo python manage.py makemigrations titles --no-input
sudo python manage.py migrate --noinput
sudo python manage.py collectstatic --no-input
sudo python manage.py loaddata  fixtures.json --no-input
