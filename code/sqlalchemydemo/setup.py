import os

from setuptools import setup, find_packages

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
]

setup(name='sqlalchemydemo',
      version='0.1',
      description='SQLAlchemy demo',
      long_description="SQLAlchemy demo",
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Bo Simonsen',
      author_email='bo@geekworld.dk',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='tutorial',
      install_requires = requires,
      entry_points = """\
      [paste.app_factory]
      main = sqlalchemydemo:main
      """,
)
