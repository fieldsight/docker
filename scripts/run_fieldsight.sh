#python manage.py migrate --noinput
#python manage.py fieldsight_default_commands
#python manage.py create_default_superuser
python manage.py migrate --noinput
python manage.py delete_permission
python manage.py collectstatic --noinput
export C_FORCE_ROOT="true"
screen -dmS screen_celery_fieldsight bash -c 'celery -A onadata worker -l Info; exec bash'
python manage.py runserver 0.0.0.0:8001

