Installation
============

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

Settings
========

``DRF_RECAPTCHA_VERIFY_ENDPOINT``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

API endpoint to which to send the information to validate the reCAPTCHA
response token.
The default value is `https://www.google.com/recaptcha/api/siteverify`
(cf. `reCAPTCHA documentation <https://developers.google.com/recaptcha/docs/verify>`_).

``DRF_RECAPTCHA_SECRET_KEY``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Secret key of `your reCAPTCHA application <https://www.google.com/recaptcha/admin>`_.
Don't forget to fill in this settings with your reCAPTCHA application secret
key.
