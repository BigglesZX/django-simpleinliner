#!/usr/bin/env python

''' XXX: allow dist building on vagrant
    source: http://bugs.python.org/issue8876

    To make a new release:
    1. Bump version number in _version.py
    2. Update CHANGELOG
    3. $ git commit ...
    4. $ git tag -a x.x.x  # see `git tags` for latest
    5. $ git push origin master
    6. $ git push --tags
    7. $ python setup.py register sdist
    8. $ twine upload dist/*
'''
import os
del os.link

from setuptools import setup, find_packages  # noqa: E402
from simpleinliner._version import get_version  # noqa: E402

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
    python_requires='>=2.6,<4',
    install_requires=['Django>=1.10', 'six>=1.12.0'],
    extras_require={
        'dev': [
            'flake8>=3.7.7',
            'setuptools>=41.0.0',
            'twine>=1.13.0',
            'wheel>=0.33.1',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
    ],
)
