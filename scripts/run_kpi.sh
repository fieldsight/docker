npm install -g
npm run build
python manage.py migrate --noinput
python manage.py collectstatic --noinput
export C_FORCE_ROOT="true"
screen -dmS screen_celery_kpi bash -c 'celery -A kobo worker -l Info; exec bash'
python manage.py runserver 0.0.0.0:8000

