Want to view the presentation?
------------------------------

http://slides.simplistix.co.uk/PyConUK2017-boring-things/#/title

Develop it?
-----------

::

  python3.6 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt

Test it?
--------

In the root of the repository clone::

  picky
  export DB_URL={sqlalchemy url for test postgres db}
  export PYTHONPATH=. pytest


Build it?
---------

bin/hovercraft presentation.rst ~/Dropbox/Presentations/PyCon2017-boring-things

