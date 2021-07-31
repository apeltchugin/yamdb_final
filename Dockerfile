FROM python:3.8.5 
 
WORKDIR /code 
COPY . . 
RUN pip install -r requirements.txt
RUN chmod +x script/django_entrypoint.sh
ENTRYPOINT script/django_entrypoint.sh
