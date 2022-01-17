
What is happening in this code?

- [ ] A call to 127.0.0.1:8000 initiates the stock picker wherein the desired stocks can be picked.
- [ ] Upon clicking submit with the desired stocks, a call to Stockticker view is initiated. 
- [ ] Stockticker view makes a multiple thread call to the yahoo fin library to get the stocks. We are using yahoo fin library as it is free and can be used for learning purposes. If we can purchase real time updates, we could bring all data at once into a DB and then can query the DB.
- [ ] As the first set of data is sent to the UI, a web socket connection is initiated using javascript.
- [ ] Through routing.py, web socket automatically navigates to the consumers WS (consumers.py) where we have the web socket methods.

Web Socket Connect
- [ ] In the web socket connect, Django first connects to a room group.
- [ ] Django then requests Celery Beat to create a periodic task which takes a schedule (running once every 10 seconds) and the query string (stocks picked) as arguments. Celery Beat uses Redis as a message broker to queue the tasks which will get executed in a FIFO manner by handing the same over to Celery.
- [ ] We also create a dictionary of user/stock in the sql lite db using stockDetail table so we only send the stocks that a specific user requested.

Task
The periodic task calls the update_stock method in tasks.py which calls the yahoo fin python library in multiple threads and returns the result to the room group.

Web Socket receive
- [ ] We send the message we receive in the room group from the task through the web socket to the UI.

Web Socket disconnect
- [ ] When the user navigates away from the In this method, we remove the user/stock combination from the stockDetail table so we do not query those stocks again unless they are used by another user. We also leave the room group.



Note: It is a good idea to always to clear all periodic tasks, intervals and task results before starting celery and redis.Have the main app running and use the admin panel to delete all of them beforehand.

------------------------------------------------------------------------------------------------------------------------------------------------------------------
The below set of instructions would slightly differ for windows machines.
	
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
