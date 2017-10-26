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

* Dependency injection framework

* Components specify their resources

  * what do they need?

  * what do they produce?

* Runners link those together

--------------

:data-y: r0
:data-x: r1500

Runners
-------

.. code-block:: python

  from mush import Runner

  def func1():
      print('func1')

  def func2():
      print('func2')


  runner = Runner()
  runner.add(func1)
  runner.add(func2)

.. container:: box

  ::

    >>> runner()
    func1
    func2

--------------

Labels
------

.. code-block:: python

  from mush import Runner

  def func1():
      print('func1')

  def func2():
      print('func2')

  def func2():
      print('func3')


  runner = Runner()
  runner.add(func1)
  runner.add_label('middle')
  runner.add(func2)

  runner['middle'].add(func3)

.. container:: box

  ::

    >>> runner()
    func1
    func3
    func2


--------------

Configuring Resources
---------------------

.. code-block:: python

  def apple_tree():
      print('I made an apple')
      return Apple()

  def magician(fruit: Apple) -> 'citrus':
      print('I turned {0} into an orange'.format(fruit))
      return Orange()

  def juicer(fruit1: Apple, fruit2: 'citrus'):
      print('I made juice out of {0} and {1}'.format(fruit1, fruit2))
      return Juice()

.. container:: box

  ::

    >>> runner = Runner(apple_tree, magician, juicer)
    >>> runner()
    I made an apple
    I turned an apple into an orange
    I made juice out of an apple and an orange
    a refreshing fruit beverage

--------------

Declarative Configuration
-------------------------

.. code-block:: python

  from mush import requires, returns

  def apple_tree():
      print('I made an apple')
      return Apple()

  @requires(Apple)
  @returns('citrus')
  def magician(fruit):
      print('I turned {0} into an orange'.format(fruit))
      return Orange()

  @requires(fruit1=Apple, fruit2='citrus')
  def juicer(fruit1, fruit2):
      print('I made juice out of {0} and {1}'.format(fruit1, fruit2))
      return Juice()

.. container:: box

  ::

    >>> runner = Runner(apple_tree, magician, juicer)
    >>> runner()
    I made an apple
    I turned an apple into an orange
    I made juice out of an apple and an orange
    a refreshing fruit beverage

--------------

Default Configuration
---------------------

.. code-block:: python

  def apple_tree() -> 'apple':
      print('I made an apple')
      return Apple()

  def magician(apple) -> 'citrus':
      print('I turned {0} into an orange'.format(apple))
      return Orange()

  def juicer(apple, citrus):
      print('I made juice out of {0} and {1}'.format(apple, citrus))
      return Juice()

.. container:: box

  ::

    >>> runner = Runner(apple_tree, magician, juicer)
    >>> runner()
    I made an apple
    I turned an apple into an orange
    I made juice out of an apple and an orange
    a refreshing fruit beverage

--------------

Explicit Configuration
----------------------

.. code-block:: python

  from mush import Runner, requires

  def apple_tree():
      print('I made an apple')
      return Apple()

  def magician(fruit):
      print('I turned {0} into an orange'.format(fruit))
      return Orange()

  def juicer(fruit1, fruit2):
      print('I made juice out of {0} and {1}'.format(fruit1, fruit2))

  runner = Runner()
  runner.add(apple_tree)
  runner.add(magician, requires=Apple, returns='citrus')
  runner.add(juicer, requires(fruit1=Apple, fruit2='citrus'))

.. container:: box

  ::

    >>> runner()
    I made an apple
    I turned an apple into an orange
    I made juice out of an apple and an orange

----------------

:data-x: r0
:data-y: r1200

Back to our tested function...
------------------------------

.. include:: code/insert_note_mush.py
  :code: python

----------------

:class: side-by-side

Assemble and Clone
------------------

.. include:: code/manual.py
  :code: python
  :start-line: 7
  :end-line: 25

.. include:: code/assemble_and_clone.py
  :code: python
  :start-line: 5
  :end-line: 37

----------------

:class: side-by-side

Assemble and Clone
------------------

.. include:: code/assemble_and_clone.py
  :code: python
  :start-line: 5
  :end-line: 37

.. include:: code/assemble_and_clone.py
  :code: python
  :start-line: 47

----------------

:class: side-by-side

Runner Factory
--------------

.. include:: code/assemble_and_clone.py
  :code: python
  :start-line: 5
  :end-line: 37

.. include:: code/runner_factory.py
  :code: python
  :start-line: 5
  :end-line: 39

----------------

:class: side-by-side

Runner Factory
--------------

.. include:: code/runner_factory.py
  :code: python
  :start-line: 5
  :end-line: 39

.. include:: code/runner_factory.py
  :code: python
  :start-line: 50

----------------

:class: side-by-side

Testing the Base Runner
-----------------------

.. include:: code/assemble_and_clone.py
  :code: python
  :start-line: 5
  :end-line: 37

.. container:: box

  - This is still a pain to test

  - But you only have to do it once

  - Component tests do heavy lifting

----------------

:id: testing-scripts

Testing the Scripts
-------------------

.. container:: box

  - How do we test these?

  - Have we wired up resources correctly?

.. include:: code/assemble_and_clone.py
  :code: python
  :start-line: 47

----------------

:id: testing-scripts-2

Testing the Scripts
-----------------------


.. container:: sub-box

  .. include:: code/assemble_and_clone.py
    :code: python
    :start-line: 47

  .. include:: code/tests/test_assemble_and_clone.py
    :code: python
    :start-line: 11
    :end-line: 32

.. container:: sub-box

  .. include:: code/tests/test_assemble_and_clone.py
    :code: python
    :start-line: 32

--------------

:id: summary
:class: slide

Summary
=======

.. container:: sp100

  - keep your tasks and framework separate
  - abstract and test framework components separately
  - have one source of framework configuration information
  - if using mush
    - use lots of labels
    - write a "run with" helper

----------------

:class: slide options-slide

Tools I've Used
===============

mush
----

* https://mush.readthedocs.io
* search for "mush python"

testfixtures
------------

* http://testfixtures.readthedocs.io/
* search for "testfixtures python"

----------------

:class: slide options-slide

Options
=======

command line processing
-----------------------

- argparse

  - standard library

- click

  - http://click.pocoo.org/
  - search for "click python"

----------------

:class: slide options-slide

Options
=======

config files
------------

- ConfigParser

  - standard library

- PyYAML

  - https://github.com/yaml/pyyaml
  - google for "python yaml"

- configurator

  - https://github.com/Simplistix/configurator
  - not finished yet

----------------

:class: slide options-slide

Options
=======

validation
----------

- voluptuous

  - http://marshmallow.readthedocs.io/
  - search for "python marshmallow"

- mushroom

  - http://marshmallow.readthedocs.io/
  - search for "python marshmallow"

----------------

:class: slide
:id: questions

Questions
=========

?

----------

:class: slide

Thanks
=======

.. container:: sp100

  Getting hold of me:

  * chris@withers.org
  * cwithers@jumptrading.com
  * @chriswithers13
