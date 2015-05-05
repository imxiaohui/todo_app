APPNAME = endlesstodolist

test: manage.py
	python manage.py runserver

rebuild: manage.py
	python manage.py makemigrations ${APPNAME}
	python manage.py migrate
