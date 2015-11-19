![](https://play.spotify.edgekey.net/site/19b6d34/images/favicon.png)
# api-my-spotify
API to access Spotify informations and other things

## How to use
* Create a virtualenv (I prefer use ``virtualenvwrapper``).
* Fork or clone this repo.
* Install ``requirments.txt`` with ``pip install -r requirments.txt``
* Run the project with ``./api_my_spotify/manage.py runserver --settings=settings.dev`` (Don't forget migrate if necessary)

## ``Makefile`` Tips
``Makefile`` was created to facilitate some commands.
* Execute ``make test`` to run the tests of project
* Execute ``make html`` to exhibit the cover of tests in your browser
* Execute ``make clean`` to clean unecessary files of your project

## TODO
* Make a User's Playlists and Tracks
