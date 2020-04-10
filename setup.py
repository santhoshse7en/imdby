"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/santhoshse7en/imdby
"""
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

# Always prefer setuptools over distutils
import setuptools

keywords = ['imdby', 'imdb', 'movie', 'people', 'database', 'cinema', 'film', 'person',
            'cast', 'actor', 'actress', 'director', 'sql', 'character',
            'company', 'package', 'plain text data files',
            'keywords', 'top250', 'bottom100', 'xml', 'bs4']

setuptools.setup(
    name="imdby",
    version="0.1.5",
    python_requires='>=3.5',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="M Santhosh Kumar",
    author_email="santhoshse7en@gmail.com",
    description="Python package to access the IMDb's database",
    url="https://github.com/santhoshse7en/imdby",
    platforms = 'any',
    keywords = keywords,
    install_requires=['beautifulsoup4', 'pandas', 'selenium', 'vaderSentiment', 'textblob', 'chromedriver-binary'],
    packages=setuptools.find_packages(),
    classifiers=['Development Status :: 4 - Beta',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Communications :: Email',
          'Topic :: Office/Business',
          'Topic :: Software Development :: Bug Tracking',
          ],
)
