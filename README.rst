===============================
Django REST framework reCAPTCHA
===============================

.. image:: https://badge.fury.io/py/django-rest-framework-recaptcha.svg
    :target: https://badge.fury.io/py/django-rest-framework-recaptcha

.. image:: https://travis-ci.org/Maximilien-R/django-rest-framework-recaptcha.svg?branch=master
    :target: https://travis-ci.org/Maximilien-R/django-rest-framework-recaptcha

.. image:: https://coveralls.io/repos/github/Maximilien-R/django-rest-framework-recaptcha/badge.svg?branch=master
    :target: https://coveralls.io/github/Maximilien-R/django-rest-framework-recaptcha?branch=master

.. image:: https://readthedocs.org/projects/django-rest-framework-recaptcha/badge/?version=latest
    :target: https://django-rest-framework-recaptcha.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Django REST framework reCAPTCHA provides you a serializer field to handle and
validate Google reCAPTCHA response.

Documentation
-------------

The full documentation is at https://django-rest-framework-recaptcha.readthedocs.io.

Requirements
------------

* Python: 2.7, 3.4, 3.5, 3.6
* Django: 1.10, 1.11, 2.0
* Django REST framework: 3.4, 3.5, 3.6, 3.7, 3.8

Installation
------------

To install Django REST framework reCAPTCHA, run this command in your terminal:

.. code-block:: console

    $ pip install djangorestframework-recaptcha

This is the preferred method to install Django REST framework reCAPTCHA, as it
will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/

Once the ``djangorestframework-recaptcha`` installed, add it to your
``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        "rest_framework_recaptcha",
        ...
    )

Next, register yourself and obtain your reCAPTCHA credentials at
https://www.google.com/recaptcha/admin.

Finally, copy/paste your Google reCAPTCHA secret key to the
``DRF_RECAPTCHA_SECRET_KEY`` setting:

.. code-block:: python

    DRF_RECAPTCHA_SECRET_KEY = "<your_reCAPTCHA_secret_key>"

Usage
-----

To use Django REST framework reCAPTCHA within your project you'll need to
import and add the ``ReCaptchaField`` serializer field into the wanted
serializer. For example:

.. code-block:: python

    from rest_framework import serializers
    from rest_framework_recaptcha import ReCaptchaField


    class MySerializer(serializers.Serializer):
        recaptcha = ReCaptchaField()
