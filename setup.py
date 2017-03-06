from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='perspective',
    version='0.1b',
    description='A package for interfacing with Google\'s Perspective API',
    long_description=long_description,
    url='https://github.com/conway/perspective',
    author='Jake Conway',
    author_email='jake.h.conway@gmail.com',
    license='UNLICENSE',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    keywords=['google', 'perspective api', 'perspective', 'natural language', 'anti-harassment', 'google apis'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests']
)