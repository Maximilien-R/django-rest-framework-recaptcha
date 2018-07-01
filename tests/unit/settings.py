# -*- coding: utf-8
from __future__ import absolute_import, unicode_literals

import django

DEBUG = True

USE_TZ = True

SECRET_KEY = "1ws*(=vz7@)albx#ltw9#azm$&y4-w73_mof+n39+9dhtlsdi7"

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = []

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()

DRF_RECAPTCHA_VERIFY_ENDPOINT = "DRF_RECAPTCHA_VERIFY_ENDPOINT"

DRF_RECAPTCHA_SECRET_KEY = "DRF_RECAPTCHA_SECRET_KEY"
