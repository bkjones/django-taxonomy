#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-taxonomy',
    version='0.0.1',
    description='A flexible taxonomy approach for Django.',
    author='Brian K. Jones',
    author_email='???',
    url='http://github.com/bkjones/django-taxonomy',
    packages=[
        'taxonomy',
        'haystack.templatetags',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        # 'License :: OSI Approved :: BSD License', - Don't know what license the code is under. Scary!
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)