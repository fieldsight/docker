python manage.py migrate --noinput
python manage.py fieldsight_default_commands
python manage.py create_default_superuser
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8001
# start the celery 
export C_FORCE_ROOT='true'
celery -A onadata worker -l Info
