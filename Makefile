test:
		coverage run --source="api_my_spotify/api" --omit="../../**migrations**, ../../**tests**" ./api_my_spotify/manage.py test -v 2 --settings=settings.test --failfast
		coverage report -m

html:
		coverage html
		open htmlcov/index.html

clean:
		find . -name "*.pyc" -exec rm -rf {} \;
		rm -rf htmlcov/
		rm -rf .coverage
		rm -rf *.log