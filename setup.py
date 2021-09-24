#!/usr/bin/env python3
from setuptools import setup

setup(name='dev_aberto_vitorsv1',
      version='0.1',
      packages=['dev_aberto'],
      author='Vitor Satyro Vitturi',
      python_requires='>=3.6',
      scripts=['scripts/hello.py'],
      install_requires=[
          'requests'
      ],
      classifiers=[
          "Programming Language :: Python :: 3",
          "Operating System :: Microsoft :: Windows",
          "Operating System :: POSIX"
      ])
