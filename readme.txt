1) Run django application

python manage.py runserver

2) In another window, start celery worker process

celery -A stockTicker.celery worker -l info

3) In a third window, start celery beat

 celery -A stockTicker beat -l INFO

4) In terminal or 4ht window, start redis
/Users/aditibaranidar/Downloads/redis-6.2.6
redis-server
