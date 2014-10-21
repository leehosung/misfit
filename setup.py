#!/usr/bin/env python

from setuptools import setup

setup(name='misfit',
      version='0.1',
      description='Misfit Client API',
      author='lee ho sung',
      author_email='lee.ho.sung@gmail.com',
      url='https://github.com/leehosung/misfit',
      packages=['misfit'],
      install_requires=open('requirements.txt').read(),
      long_description=open('README.md').read(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      license='MIT'
      )

