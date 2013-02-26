import os
from setuptools import setup, find_packages

PROJECT = {{ app_name }}
URL='https://bitbucket.org/dries/%s' % PROJECT,


# Use the docstring of the __init__ file to be the description
DESC = " ".join(__import__(PROJECT).__doc__.splitlines()).strip()

def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    """Return the README file contents. Supports text,rst, and markdown"""
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file(name)
    return ''


setup(
    name=PROJECT,
    version=__import__(PROJECT).__version__,
    url=URL,
    author='Dries Desmet',
    author_email='dries@urga.be',
    description=DESC,
    long_description=get_readme(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_file('requirements.txt'),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Framework :: Django',
    ],
)
