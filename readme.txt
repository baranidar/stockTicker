	This is the instructions for MAC.
	
	1) Install virtual env
	pip install virtualenv 

	2) Create a new virtual env 
	virtualenv stockenv
	
	3) Activate virtualenv
	source stockenv/bin/activate 
	
	4)  Install django 
	 pip install django
	
	5) Install yahoo fin library
	pip install yahoo-fin 
	
	6) Install celery
	pip install celery
	
	7) To generate all dependencies
	pip freeze > requirements.txt 
	
	8) Install redis
	Download latest tar from redis.io
	
	tar xvzf redis-<version>.tar.gz
cd redis-stable
make
	make test
	sudo make install
	
	9) Start Redis server
	redis-server
	
	10) To check if properly installed
	redis-cli ping
	We should get pong
	
	11) Install django celery results
	pip install django-celery-results
	
	12) Install django celery beat
	pip install django-celery-beat
	
	13) Install redis library
	pip install redis
	
	14) Install channels
	pip install channels
	
	15) Install Channels redis
	pip install channels-redis
	
	16) Install asyncio
	pip install asyncio
	
	17) Install simplejson
	pip install simplejson
	
	
To start the app, from inside stockTicker folder

1) Run django application
python manage.py runserver
2) In another window, start celery worker process
celery -A stockTicker.celery worker -l info
3) In a third window, start celery beat
celery -A stockTicker beat -l INFO
4) In terminal or 4ht window, start redis
/Users/<>/Downloads/redis-6.2.6. - folder where redis is installed
redis-server

Instructions
	1) Create two different users and login as those users in two different windows.
	2) Pick different stocks and the tickers should work and do unique pulls of all stocks selected and return only the ones each user selected
