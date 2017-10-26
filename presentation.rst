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
  standard library logging - but briefly

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
:data-y: r-500
:data-z: r-700

.. note::
  spot the bugs (quiet arg, no execute method on conn)

Uh Oh, We better test that!
---------------------------

.. include:: code/testable1.py
  :code: python

-------------

:id: test2
:data-x: r0
:data-y: r0
:data-z: r100

.. include:: code/tests/test_testable1.py
  :code: python
  :start-line: 7

.. note::
  Have to test at a high level.
  Getting coverage is a pain.
  Not checking log levels.

  ...and for each of the copies
  No code re-use, bugs are everywhere
  Fancy transition to show where we started.
  How did we get here? Where do we go next?

--------------

:id: base-class
:data-x: r2300
:data-y: r0
:data-z: r0
:class: side-by-side

Anti-pattern 2: The Base Class
------------------------------


.. include:: code/testable1.py
  :code: python

.. include:: code/base_class.py
  :code: python
  :start-line: 4
  :end-line: 60

--------------

:id: base-script
:data-x: r900
:data-z: r100

.. container:: base_script

  .. include:: code/base_class.py
    :code: python
    :start-line: 61

  .. class:: header

  What's so bad about that?

.. note::
  abstract into classes -> bells-and-whistles class
  end up with infinite plugin methods that are all called
  usually just test the 'do-it' method
  hard to test all the plugin points

--------------

:data-x: r2100
:data-z: r0

Anti-pattern 3: Splitting Configuration
---------------------------------------

.. include:: code/config_split.py
  :code: python

.. note::

  splitting config across objects (config, args, env)

--------------

:data-x: r1700
:class: slide

So how did we get here?
-----------------------

.. container:: sp100

  - Multiple scripts ends up needing framework

.. container:: sp100

  - Each script is usually a single function

.. container:: sp100

  - Much shared config

----------------

:data-y: 0
:data-x: r-5000
:data-z: r2000

----------------

:data-x: r-5000
:data-z: r2000

----------------

:data-x: r-5000
:data-z: r-2000

----------------

:data-x: r-5000
:data-y: r-76
:data-z: r-2200

----------------

:id: simple-function
:data-x: r0
:data-y: r400
:data-z: r0

.. include:: code/insert_note.py
  :code: python


----------------

:data-x: r0
:data-y: r1200
:data-z: r0
:class: side-by-side

A tested function
-----------------


.. include:: code/insert_note.py
  :code: python

.. include:: code/tests/test_insert_note.py
  :code: python
  :start-line: 4

----------------

:class: side-by-side

Components: Argument Parsing
----------------------------


.. include:: code/testable1.py
  :code: python

.. include:: code/components.py
  :code: python
  :start-line: 3
  :end-line: 16

----------------

:class: side-by-side

Components: Config
----------------------------


.. include:: code/testable1.py
  :code: python

.. include:: code/components.py
  :code: python
  :start-line: 17
  :end-line: 31


.. note::
   user preferences woven in here
   mention configurator?

----------------

:class: side-by-side

Components: Logging
----------------------------


.. include:: code/testable1.py
  :code: python

.. include:: code/components.py
  :code: python
  :start-line: 34
  :end-line: 63

----------------

:class: side-by-side

Components: Database
----------------------------


.. include:: code/testable1.py
  :code: python

.. include:: code/components.py
  :code: python
  :start-line: 64

----------------

.. container:: box

  .. class:: header

    How do we wire all that together?

----------------

:class: side-by-side

Manually?
---------

.. include:: code/manual.py
  :code: python
  :start-line: 7
  :end-line: 25

.. include:: code/manual.py
  :code: python
  :start-line: 26


.. note::

 what about those ellipsis?
 how do we know we got the stuff in the __main__ block right?

----------------

:class: slide

Mush
----

* Dependency injection

* Components specify their resources

  * what do they need?

  * what do they produce?

* Runners link those together




--------------


Structure
=========

- runners
- configuring resources
- assemble and clone
- factory function

- testing (should test runn

concepts:

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

mush
------------

* https://pypi.python.org/pypi/testfixtures
* search for "testfixtures python"

testfixtures
------------

* https://pypi.python.org/pypi/testfixtures
* search for "testfixtures python"

mortar_rdb
----------

* https://pypi.python.org/pypi/testfixtures
* search for "testfixtures python"

Chris Withers
-------------

* chris@withers.org / cwithers@jumptrading.com
* @chriswithers13

.. note:: 

   configurator? Roll links into "options" section?
