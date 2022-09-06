from gettext import find
from setuptools import setup, find_packages

setup(name='tripleagentz3',
      packages=find_packages(),
      install_requires=[
        "z3-solver==4.11.2.0"
      ]
     )