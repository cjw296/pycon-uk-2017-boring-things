Want to view the presentation?
------------------------------

http://slides.simplistix.co.uk/PyConUK2017-boring-things

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
  export DB_NAME={test postgres db name}
  export DB_USER={test postgres db user}
  export DB_PASSWORD={test postgres db password}
  export PYTHONPATH=.
  pytest


Build it?
---------

bin/hovercraft presentation.rst build

