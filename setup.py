import os
from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "sphinxwepayapi",
    version = "0.0.1",
    author = "Giovanni Briggs",
    author_email = "gbriggs2012@gmail.com",
    description = ("Sphinx directive to create links to WePay API documentation"),
    license = "BSD",
    keywords = "wepay wepay-docs sphinx",
    url = "https://github.com/Jalepeno112/SphinxWePayApi",
    packages=['sphinxwepayapi'],
    long_description=read('README.rst')
)
