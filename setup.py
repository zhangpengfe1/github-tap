#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='github-tap',
      version='0.0.1',
      description='Singer.io tap for extracting data from the GitHub API',
      author='Stitch',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['github_tap'],
      install_requires=[
          'singer-python==5.12.1',
          'requests==2.20.0'
      ],
      extras_require={
          'dev': [
              'pylint',
              'ipdb',
              'nose',
          ]
      },
      entry_points='''
          [console_scripts]
          github-tap=github_tap:main
      ''',
      packages=['github_tap'],
      package_data = {
          'github_tap': ['github_tap/schemas/*.json']
      },
      include_package_data=True
)
