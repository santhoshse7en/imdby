# imbpy

**imdby** is a Python package useful to retrieve and manage the data of the [IMDb](https://www.imdb.com/) movie database about movies, people, characters and companies.

## Main features

- written in Python 3 (compatible with Python 2.7)

- platform-independent

- can retrieve data from both the IMDb's web server, or a local copy of the database

- released under the terms of the MIT license

imbpy powers many other software and has been used in various research papers. _`Curious about that`_?    


## Installation

Whenever possible, please use the latest version from the repository::

```bash
pip install git+https://github.com/santhoshse7en/imdb
```

But if you want, you can also install the latest release from PyPI::

```bash
pip install imbpy
```

## Usage

Download it by clicking the green download button here on Github. Here's an example that demonstrates how to use imdby:

```python
# create an instance of the IMDb class
from imdb import imdb

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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
