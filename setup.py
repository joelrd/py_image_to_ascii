# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='py_image_to_ascii',
    version='1.0.0',
    description='Python 3.7 based programs to convert images to ascii.',
    long_description=readme,
    author='Henry Rojas',
    author_email='henry@henryrojasdev.com',
    url='https://github.com/joelrd/py_image_to_ascii',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
