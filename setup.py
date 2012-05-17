from setuptools import setup, find_packages
import os

version = '0.0'

def _read(name):
    try:
        return open(os.path.join(os.path.dirname(__file__), name)).read()
    except IOError:
        return ''

readme = _read('README.rst')

requires = [
    "SQLAlchemy",
]

tests_require = [
    "nose",
    "coverage",
    "mock",
]

setup(name='MySQLAlchemy',
      version=version,
      description="",
      long_description=readme,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires + tests_require,
      extras_require={
        "testing": requires + tests_require,
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
