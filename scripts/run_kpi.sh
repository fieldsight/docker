python manage.py migrate --noinput
npm install
npm run build
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000

