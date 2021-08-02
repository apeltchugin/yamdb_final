[![yamdb_final-master Actions Status](https://github.com/apeltchugin/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)

# yamdb_final
yamdb_final
### Описание
Учебный проект "деплой на сервер", по теме Git Actions / Docker / Docker Hab, контейнеры создаются на базе учебного проекта api_yamdb.  
Образ сохраняется в облако DockerHub как apelt/yamdb_final:latest дальше разворачивается на сервере, согласно yamdb_workflow.yaml


### Технологии
Python 3.8.5
Django 3.0.5
Postgres 12.4
Gunicorn 20.0.4
Nginx 1.19.3
Docker-compose 3.8
Docker Server 20.10.7

### Запуск проекта
-  Создаём миграции
docker-compose exec web python manage.py makemigrations users
docker-compose exec web python manage.py makemigrations review
docker-compose exec web python manage.py makemigrations titles

- Запускаем миграцию
docker-compose exec web python manage.py migrate --noinput

- Создаём суперюзера
docker-compose exec web python manage.py createsuperuser

- Собираем статику
docker-compose exec web python manage.py collectstatic --no-input

- При жалании наполяем базу из фикстуры
docker-compose exec web python manage.py loaddata  fixtures.json
