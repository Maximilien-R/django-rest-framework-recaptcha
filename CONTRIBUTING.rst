Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/Maximilien-R/django-rest-framework-recaptcha/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Django REST framework reCAPTCHA could always use more documentation, whether
as part of the official Django REST framework reCAPTCHA docs, in docstrings, or
even on the web in blog posts, articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/Maximilien-R/django-rest-framework-recaptcha/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? The easiest way to work on
``djangorestframework-recaptcha`` for local development is to use Docker.
``djangorestframework-recaptcha`` come with a ``Dockerfile`` and a ``Makefile``
that implements all the needed stuff and helpers to work on this project.

1. Install `Docker <https://docs.docker.com/install/>`_.
2. Fork the ``djangorestframework-recaptcha``
   `GitHub repository <https://github.com/Maximilien-R/django-rest-framework-recaptcha>`_.
3. Clone your fork locally:

.. code-block:: console

    $ git clone git@github.com:your_name_here/django-rest-framework-recaptcha.git

4. Create a branch for local development:

.. code-block:: console

    $ git checkout -b name-of-your-bugfix-or-feature

Now you can make your changes locally.

5. When you're done making changes, check that your changes pass format check,
   flake8, complexity and the tests, including testing other Python versions
   with tox:

.. code-block:: console

    $ make check-format
    $ make style
    $ make complexity
    $ make test-all

6. Format your code and then commit your changes and push your branch to
   GitHub:

.. code-block:: console

    $ make format
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring.
3. The pull request should work for Python 2.7, 3.4, 3.5 and 3.6, and for PyPy.
   Check https://travis-ci.org/Maximilien-R/django-rest-framework-recaptcha/pull_requests
   and make sure that the tests pass for all supported Python versions.
4. Your code need to be formatted. On this project we use the
   `black <https://github.com/ambv/black>`_ code formatter. You can easily
   format your code with this command: ``make format``.

Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in
``HISTORY.rst``). Then run:

.. code-block:: console

    $ make bumpversion -e VERSION_PART=patch # options: major / minor / patch
    $ git push
    $ git push --tags

Travis will then deploy to PyPI if tests pass.

Translations
------------

You can also participate in the project by adding new language or improving
translations.

To add a new language:

.. code-block:: console

    $ make build-translations -e LOCALE=en

To update available languages and check for new strings:

.. code-block:: console

    $ make update-translations

To compile translations:

.. code-block:: console

    $ make compile-translations
