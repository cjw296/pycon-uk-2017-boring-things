.. title: Make all the Boring Things Go Away

:data-transition-duration: 150
:skip-help: true
:css: presentation.css


-------------

:id: title
:class: slide

Making all the Boring Things Go Away
====================================


Chris Withers

.. class:: grey

  Jump Trading

.. note::

  Who am I?
  Everyone has to write scripts, the tend to
  grow like mould...

--------------

A Simple Script for a Simple Task
---------------------------------

.. include:: code/simple1.py
  :code: python

.. note:: but users want a test db

--------------

Another environment
-------------------

.. include:: code/simple2.py
  :code: python

.. note:: but users can't tell what's going on

--------------

What's going on?
----------------

.. include:: code/simple3.py
  :code: python

.. note:: print statements everywhere

--------------

We need a real database!
------------------------

.. include:: code/simple4.py
  :code: python

.. note::
  and that means we need a config file
  ...but our args are now crazy

--------------

I don't know how to use this!
-----------------------------

.. include:: code/simple5.py
  :code: python

.. note::
  add argparse

--------------

Its too verbose!
-----------------------------

.. include:: code/simple6.py
  :code: python

.. note::
  "I only want that when I'm debugging"
  standard library logging

--------------

I want to do something different!
---------------------------------


.. include:: code/simple6.py
  :code: python
  :class: code1

.. note::
  Copy and copy and copy...

--------------

:id: copy1
:data-x: r900
:data-y: r24
:data-z: r500

.. include:: code/simple6.py
  :code: python

--------------

:id: copy2
:data-x: r0
:data-y: r0
:data-z: r0

.. include:: code/simple6.py
 :code: python

-------------

:id: copy3
:data-x: r0
:data-y: r400
:data-z: r200

.. include:: code/simple6.py
 :code: python
 :class: example1

.. include:: code/simple6.py
 :code: python
 :class: example2

.. include:: code/simple6.py
 :code: python
 :class: example3

-------------

:id: bug
:data-x: r0
:data-y: r0
:data-z: r0

-------------

:id: test1
:data-x: r2500
:data-y: r-424
:data-z: r-700

Uh Oh, We better test that!
---------------------------

.. include:: code/testable1.py
  :code: python

.. note::
  ...and for each of the copies
  Have to test at a high level.
  No code re-use, bugs are everywhere
  Fancy transition to show where we started.
  How did we get here? Where do we go next?

-------------

:id: test2
:data-x: r0
:data-y: r0
:data-z: r0

--------------

:data-x: r3000
:data-y: r0
:data-z: r0

Now we have two problems...
---------------------------

... note::
  abstract into classes -> god class

  splitting config across objects (config, args, env)

--------------






To Cover
--------

command line option processing,
config files,
user preferences,
logging,
structuring code for testability.

--------------


Structure
=========

anecdotal script:
- no testing
- add copy
- add config
- print everywhere

antipatterns:
- c'n'p code
- god class
- mention clean code?
- splitting config across objects (config, args, etc)

concepts:

- structure for testing -> dependency injection
- one source of config, layered from sources
- test the components
- assemble into a runner
- have a high-level test of that
- abstract out common bits
- use lots of mush labels

----------------

Options
=======

command line processing:
- click
- argparse

config file:
- raw
- ConfigParser (stdlib, terrible)
- ZConfig (?!)
- configurator

validation:
- voluptuous
- mushroom(?!)
- other ones

user preferences:
- config files
- env vars

logging:
- structlog
- shoehorn
- logbook



----------------

:class: slide
:id: questions

Questions
=========

?

----------

:id: links
:class: slide

Links
=======

testfixtures
------------

* https://pypi.python.org/pypi/testfixtures
* search for "testfixtures python"

mock
----

* http://docs.python.org/dev/library/unittest.mock
* search for "python mock"

Chris Withers
-------------

* chris@withers.org
* @chriswithers13

.. note:: 

   testfixtures and mock are available separately, py25 - py33

   READ THE DOCS - context managers, decorators, etc

   newer unittest features only really fully there in py33
   unittest2 may bring a lot of it?
