[![PyPI Version](https://img.shields.io/pypi/v/imdby.svg)](https://pypi.org/project/imdby)
[![Coverage Status](https://coveralls.io/repos/github/santhoshse7en/imdby/badge.svg?branch=master)](https://coveralls.io/github/santhoshse7en/imdby?branch=master)
[![License](https://img.shields.io/pypi/l/imdby.svg)](https://pypi.python.org/pypi/imdby/)
[![Documentation Status](https://readthedocs.org/projects/pip/badge/?version=latest&style=flat)](https://santhoshse7en.github.io/imdby_doc)

# imdby

**imdby** is a Python package useful to retrieve and manage the data of the [IMDb](https://www.imdb.com/) movie database about movies, person, characters, companies, events and news.

| Source         | Link                                       |
| ---            |  ---                                       |
| PyPI:          | https://pypi.org/project/imdby/            |
| Repository:    | https://github.com/santhoshse7en/imdby/    |
| Documentation: | https://santhoshse7en.github.io/imdby_doc/ |

## Main features

* **imdby** is a Python package useful to retrieve and manage the data of the IMDb movie database about movies, person, characters, companies, events and news. 

- Sentiment Analysis for IMDb user reviews is included.

- written in Python 3 (compatible with Python 2.7)

- platform-independent

- can retrieve data from both the IMDb's web server, or a local copy of the database

- simple and complete API


## Dependencies

* beautifulsoup4
* selenium
* chromedriver-binary
* vaderSentiment
* textblob
* pandas

## Installation

Whenever possible, please use the latest version from the repository:

```bash
pip install git+https://github.com/santhoshse7en/imdb
```

But if you want, you can also install the latest release from PyPI:

```bash
pip install imdby
```

## A Glance

Download it by clicking the green download button here on Github. Here's an example that demonstrates how to use imdby:

```python
# create an instance of the IMDb class
from imdb.imdb import IMDb

ia = IMDb()

# get a movie
cast = ia.full_cast_and_crew('tt4154796')

# print the names of the directors of the movie
print('Directors:')
for director in cast.directors:
    print(director)

# search for a person name
people = ia.search_person('Simon Baker')
print(people.person_id, people.person_name)
```

## Getting help
Please refer to the the online documentation on [Read The Docs](https://imdby.readthedocs.io/).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
