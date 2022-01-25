:: This is a comment ::
:: run this in cmd terminal
set Moneyconfig=dev
python manage.py runserver --port 5000 --host "0.0.0.0"
:: gunicorn --bind 0.0.0.0:5000 wsgi:app
:: run the above command if you have ubuntu