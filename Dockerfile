FROM python:3.8.5 
 
WORKDIR /code 
COPY . . 
RUN pip install -r requirements.txt 
RUN chmod +x migrate.sh
ENTRYPOINT  migrate.sh