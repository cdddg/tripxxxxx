FROM    python:3.7.5

ENV     PYTHONUNBUFFERED  1
ENV     LOCAL_DB_HOST     db

WORKDIR /src
COPY    ./src /src
COPY    ./requirements.txt /src/
COPY    ./wait-for-it.sh /src/

RUN     pip install -r /src/requirements.txt --no-cache-dir
RUN     chmod +x /src/wait-for-it.sh


CMD     ["sh", "-c", "python manage.py runserver 0.0.0.0:8000 --noreload --settings=project.settings.$BUILD_ENV"]

EXPOSE  8000
