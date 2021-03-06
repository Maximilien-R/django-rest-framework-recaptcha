#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

from setuptools import find_packages, setup

_BASE_FILE = os.path.abspath(os.path.dirname(__file__))


def _get_version(*file_paths):
    """
    Returns the version of the package.
    :param file_paths: path to the file containing the version number
    :return: string
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


_VERSION = _get_version("rest_framework_recaptcha", "__init__.py")

with open(os.path.join(_BASE_FILE, "README.rst")) as f:
    _README = f.read().strip()

with open(os.path.join(_BASE_FILE, "HISTORY.rst")) as f:
    _HISTORY = f.read().replace(".. :changelog:", "").strip()


_DESCRIPTION = """reCAPTCHA field for Django REST framework serializers."""

setup(
    name="djangorestframework-recaptcha",
    version=_VERSION,
    description=_DESCRIPTION,
    long_description=_README + "\n\n" + _HISTORY,
    long_description_content_type="text/x-rst",
    keywords="django rest framework recaptcha",
    author="Maximilien Raulic",
    author_email="maximilien.raulic@gmail.com",
    url="https://github.com/Maximilien-R/django-rest-framework-recaptcha",
    license="MIT",
    install_requires=[
        "django>=1.10",
        "djangorestframework>=3",
        "django-appconf",
        "django-ipware>=2.1.0",
        "pytz",
    ],
    extras_require={
        "development": [
            "bandit==1.5.1",
            "black==18.9b0",
            "bumpversion==0.5.3",
            "flake8==3.6.0",
            "isort==4.3.4",
            "pytest-cov==2.6.1",
            "pytest-django==3.4.7",
            "pytest==4.3.0",
            "safety==1.8.5",
            "Sphinx==1.8.4",
            "tox==3.7.0",
            "twine==1.13.0",
            "xenon==0.5.5",
        ],
    },
    packages=find_packages(include=["rest_framework_recaptcha"]),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
