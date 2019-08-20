# -*- coding: utf-8 -*-

# Learn more: https://github.com/chandramgc/pylive/blob/master/README.md

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pylive',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Girish Mallula',
    author_email='chandramgc@gmail.com',
    url='https://github.com/chandramgc/pylive',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
