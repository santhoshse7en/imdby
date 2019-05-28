[![PyPI Version](https://img.shields.io/pypi/v/imdby.svg)](https://pypi.org/project/imdby)
[![Coverage Status](https://coveralls.io/repos/github/santhoshse7en/imdby/badge.svg?branch=master)](https://coveralls.io/github/santhoshse7en/imdby?branch=master)
[![License](https://img.shields.io/pypi/l/imdby.svg)](https://pypi.python.org/pypi/imdby/)
[![Documentation Status](https://readthedocs.org/projects/pip/badge/?version=latest&style=flat)](https://santhoshse7en.github.io/imdby_doc)

## Getting started

## Welcome to imdby

imdby is a Python3 library! [View on Github here](https://github.com/santhoshse7en/imdby).

| Source         | Link                                       |
| ---            |  ---                                       |
| PyPI:          | https://pypi.org/project/imdby/            |
| Repository:    | https://github.com/santhoshse7en/imdby/    |
| Documentation: | https://santhoshse7en.github.io/imdby_doc/ |

## Main features

* **imdby** is a Python package useful to retrieve and manage the data of the IMDb movie database about movies, people, characters and companies. Sentiment Analysis for IMDb user reviews is included.

- **imdby** package can be very easily used by programmers and developers to provide access to the IMDb's data to their programs.

- Platform-independent and written in Python 3 it can retrieve data from both the IMDb's web server and a local copy of the whole database.

- Some simple example scripts - useful for the end users - are included in this package;

imdby powers many other software and has been used in various research papers. _Curious about that?_

## A Glance

```Python
# create an instance of the IMDb class
from imdby.imdb import imdb

# get a movie
details = imdb('tt4154796')

# print the names of the directors of the movie
print('Directors:')
for i in range(len(details.directors)):
    print(details.directors[i])

# print the genres of the movie
print('Genres:')
for i in range(len(details.genre)):
    print(details.genre[i])
```
