===========================
DRF reCAPTCHA field Package
===========================

.. image:: https://badge.fury.io/py/django-drf-recaptcha-field.svg
    :target: https://badge.fury.io/py/django-drf-recaptcha-field

.. image:: https://travis-ci.org/Maximilien-R/django-drf-recaptcha-field.svg?branch=master
    :target: https://travis-ci.org/Maximilien-R/django-drf-recaptcha-field

.. image:: https://coveralls.io/repos/github/Maximilien-R/django-drf-recaptcha-field/badge.svg?branch=master
    :target: https://coveralls.io/github/Maximilien-R/django-drf-recaptcha-field?branch=master

.. image:: https://readthedocs.org/projects/django-drf-recaptcha-field/badge/?version=latest
    :target: https://django-drf-recaptcha-field.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

DRF reCAPTCHA field provides you a serializer field to handle and validate
Google reCAPTCHA response.

Documentation
-------------

The full documentation is at https://django-drf-recaptcha-field.readthedocs.io.

Requirements
------------

* Python: 2.7, 3.4, 3.5, 3.6
* Django: 1.10, 1.11, 2.0
* Django REST framework: 3.4, 3.5, 3.6, 3.7, 3.8

Installation
------------

To install DRF reCAPTCHA field, run this command in your terminal:

.. code-block:: console

    $ pip install django-drf-recaptcha-field

This is the preferred method to install DRF reCAPTCHA field, as it will always
install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/

Register and obtain your reCAPTCHA crendentials at
https://www.google.com/recaptcha/admin.

Once registered and your reCAPTCHA application created, copy/paste your Google
reCAPTCHA secret key to the ``DRF_RECAPTCHA_FIELD_SECRET_KEY`` setting:

.. code-block:: python

    DRF_RECAPTCHA_FIELD_SECRET_KEY = "<your_reCAPTCHA_secret_key>"

Usage
-----

To use DRF reCAPTCHA field within your project you'll need to import and add
the ``ReCaptchaField`` serializer field into the wanted serializer. For example:

.. code-block:: python

    from rest_framework import serializers
    from drf_recaptcha_field import ReCaptchaField


    class MySerializer(serializers.Serializer):
        recaptcha = ReCaptchaField()
