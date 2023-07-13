#python manage.py collectstatic --settings=profile.settings

# python manage.py runserver 0.0.0.0:80 --settings=profile.settings
mkdir -p /var/log/gunicorn
mkdir -p /var/log/nginx
touch /var/log/gunicorn/gunicorn.log
touch /var/log/gunicorn/access.log
touch /var/log/nginx/access.log

mkdir -p /usr/src/crewer/static/events
mkdir -p /usr/src/crewer/static/hotels
mkdir -p /usr/src/crewer/static/users

echo Starting nginx
echo Starting Gunicorn.

if [[ -z "$PF_STATIC_PATH" ]]
then
    export PF_STATIC_PATH=/usr/src/crewer/static
fi

#sed -i "s|NGINX_SERVER_NAME|${SERVERNAME}|g" /etc/nginx/sites-available/django_nginx.conf
#sed -i "s|NGINX_STATIC_PATH|${PF_STATIC_PATH}|g" /etc/nginx/sites-available/django_nginx.conf
export WORKERS_COUNT=6
export GUNICORN_LOG_LEVEL=info
export GUNICORN_TIMEOUT=30


cd /usr/src/crewer/crewer
exec gunicorn crewer.wsgi:application \
    --name crewer \
    --bind unix:/usr/src/crewer/crewer.sock \
    --log-file=/var/log/gunicorn/gunicorn.log \
    --access-logfile=/var/log/gunicorn/access.log &

echo here
exec nginx &
# exec nginx -s reload &
# nginx -g 'pid /tmp/nginx.pid;'

tail -f -n100 /var/log/nginx/access.log
