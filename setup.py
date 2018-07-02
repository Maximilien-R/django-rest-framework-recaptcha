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
    keywords="django rest framework recaptcha",
    author="Maximilien Raulic",
    author_email="maximilien.raulic@gmail.com",
    url="https://github.com/Maximilien-R/django-rest-framework-recaptcha",
    license="MIT",
    install_requires=[
        "django>=1.10",
        "djangorestframework>=3",
        "django-appconf",
        "django-ipware>=2.0.2",
    ],
    extras_require={
        "complexity": ["xenon==0.5.4"],
        "documentation": ["Sphinx==1.7.5"],
        "formatting": ["black==18.6b2"],
        "style": ["flake8==3.5.0"],
        "testing": [
            "pytest==3.6.1",
            "pytest-cov==2.5.1",
            "pytest-django==3.3.0",
            "tox==3.0.0",
        ],
        "publishing": ["twine==1.11.0"],
        "versioning": ["bumpversion==0.5.3"],
    },
    packages=find_packages(include=["rest_framework_recaptcha"]),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
