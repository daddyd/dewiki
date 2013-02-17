import os
from setuptools import setup, find_packages

version = '0.1.0'
readme = os.path.join(os.path.dirname(__file__), 'README.md')
long_desc = open(readme).read() + '\n\n'

setup(name = 'dewiki',
      version = version,
      description = 'Python module to remove wiki markup',
      long_description = long_desc,
      classifiers = [
                     "Programming Language :: Python",
                     ("Topic :: Software Development :: Libraries :: Python Modules"),
                     ],
      keywords = "wiki",
      author = "Dirk Dierickx",
      author_email = 'dirk.dierickx@gmail.com',
      url = 'https://github.com/daddyd/dewiki',
      license = 'GPL',
      packages = find_packages()
      )
