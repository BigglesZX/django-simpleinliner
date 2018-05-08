#!/usr/bin/env python

# FIXME: dirty hack to allow dist building on vagrant
# source: http://bugs.python.org/issue8876
# to build: $ python setup.py register sdist
# then: $ twine upload dist/*
import os
del os.link


import sys
from setuptools import setup, find_packages
from simpleinliner._version import get_version

setup(
    name='django-simpleinliner',
    version=get_version(),
    description='A simple Django app for inlining static files in templates.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='James Tiplady',
    maintainer='James Tiplady',
    license='MIT',
    url='http://github.com/BigglesZX/django-simpleinliner',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django<2.0', 'html>=1.16,<2.0', 'twine'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)
