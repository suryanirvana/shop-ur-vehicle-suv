GOTO BEGIN 
This cmd file is created by Fransiscus Emmmanuel Bunaren to automatically call the coverage library
https://www.bedjango.com/blog/package-week-coverage-django/
coverage run --source='.' manage.py test the-app-you-want-to-test
python -m coverage run --source='./app' manage.py test

:BEGIN
python -m coverage run --include='suv/*' manage.py test
python -m coverage report -m
python -m coverage erase