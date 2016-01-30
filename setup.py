#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='nonilnil',
    # GETTING-STARTED: set your app version:
    version='1.02',
    # GETTING-STARTED: set your app description:
    description='nonilnil OpenShift App',
    # GETTING-STARTED: set author name (your name):
    author='Brendan Sleight',
    # GETTING-STARTED: set author email (your email):
    author_email='example@example.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.8.4',
        'django-mailgun==0.8.0',
        'django-registration-redux==1.2',
        'requests==2.9.1',
        'six==1.10.0',
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
