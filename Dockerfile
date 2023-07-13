FROM alpine:3.13

WORKDIR /usr/src/crewer

RUN mkdir -p /usr/src/crewer

RUN apk add gcc musl-dev mariadb-connector-c-dev
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN apk add python3-dev
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN python --version

# set python environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

# copy project
COPY . .

RUN mkdir /logs

RUN apk add --update --no-cache nginx
#RUN rm /etc/nginx/conf.d/default.conf
COPY ./deployment/nginx.conf /etc/nginx/nginx.conf
COPY ./deployment/nginx.conf /etc/nginx/conf.d


RUN mkdir -p /etc/nginx/sites-available
RUN mkdir -p /etc/nginx/sites-enabled
RUN mkdir -p /run/nginx
RUN mkdir -p /tmp/nginx
RUN mkdir -p /var/log/gunicorn
RUN mkdir -p /var/log/nginx

COPY ./deployment/django_nginx.conf /etc/nginx/sites-available
RUN ln -s /etc/nginx/sites-available/django_nginx.conf /etc/nginx/sites-enabled/django_nginx.conf
RUN rm -rf /etc/nginx/conf.d

COPY ./bin/start.sh /usr/src/start.sh
RUN echo "HI"
CMD ["sh", "/usr/src/start.sh"]
