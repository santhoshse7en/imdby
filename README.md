[![PyPI Version](https://img.shields.io/pypi/v/imdby.svg)](https://pypi.org/project/imdby)
[![Coverage Status](https://coveralls.io/repos/github/santhoshse7en/imdby/badge.svg?branch=master)](https://coveralls.io/github/santhoshse7en/imdby?branch=master)
[![License](https://img.shields.io/pypi/l/imdby.svg)](https://pypi.python.org/pypi/imdby/)
[![Documentation Status](https://readthedocs.org/projects/pip/badge/?version=latest&style=flat)](https://santhoshse7en.github.io/imdby_doc)

# imdby

**imdby** is a Python package useful to retrieve and manage the data of the [IMDb](https://www.imdb.com/) movie database about movies, people, characters and companies.

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

imdby powers many other software and has been used in various research papers. _`Curious about that`_?    

## Dependencies

* beautifulsoup4
* selenium
* chromedriver-binary
* vaderSentiment
* textblob
* pandas

## Installation

Whenever possible, please use the latest version from the repository::

```bash
pip install git+https://github.com/santhoshse7en/imdb
```

But if you want, you can also install the latest release from PyPI::

```bash
pip install imdby
```

## A Glance

Download it by clicking the green download button here on Github. Here's an example that demonstrates how to use imdby:

```python
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
Directory of IMDb class

![dir](https://user-images.githubusercontent.com/47944792/58303052-eb5d2180-7e0b-11e9-82c1-14627ee73ca3.PNG)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
