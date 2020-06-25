# FTLProject

## Motive
	
	Django project structure and listing api	


## Setup

	Linux
	
	- install python3
	command - sudo apt install python3.6

	- install pip 
	command - sudo apt-get install python3-pip

	- install git
	command - sudo apt install git-all

	
	- clone repository 
	command - git clone https://github.com/vishalbende/FTLProject.git

	- create virtualenv outside the project folder
	command - virtualenv -p python3 ftl_env
	
	- go to the project folder
	
	- activate virtual environment 
	command - source ../ftl_env/bin/activate

	- install requirements.txt by pip
	command - pip install -r requirements.txt

	- check everything is ok or not by running django project
	command -  python manage.py runserver

	- export django setting module
	command - export DJANGO_SETTINGS_MODULE=ftlproject.settings.local


	- do the migrations
	command :-
	python manage.py migrate	
	python manage.py makemigrations ftl_app
	python manage.py migrate

	- add dummy data 
	command - python manage.py dummy_data 10 ( 10 is the number of records of user you want to add, it can be any integer )

	
	- run the server agin 
	command - python manage.py runserver 

	- check url is working or not on browser
	URL : http://127.0.0.1:8000/ftl-api/members/
	
	

	

	


