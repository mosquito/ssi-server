# encoding: utf-8

from __future__ import absolute_import, print_function

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


__version__ = '0.1.1'
__author__ = 'Dmitry Orlov <me@mosquito.su>'

_requirements = open('requirements.txt', 'rb').read().split('\n')

setup(name='ssi-server',
    version=__version__,
    author=__author__,
    author_email='me@mosquito.su',
    license="MIT",
    description="Simple SSI (Server Side Includes) server. For developers only.",
    platforms="all",
    url="http://github.com/mosquito/ssi-server",
    classifiers=[
      'Environment :: Console',
      'Programming Language :: Python',
    ],
    long_description=open('README.rst').read(),
    scripts=['bin/ssi-server',],
    install_requires=_requirements,
    requires=['Python (>2.6)']
)
