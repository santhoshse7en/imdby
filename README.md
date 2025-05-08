[![PyPI Version](https://img.shields.io/pypi/v/imdby.svg?style=flat-square)](https://pypi.org/project/imdby)
[![License](https://img.shields.io/pypi/l/imdby.svg?style=flat-square)](https://pypi.python.org/pypi/imdby/)
[![Documentation Status](https://readthedocs.org/projects/pip/badge/?version=latest\&style=flat-square)](https://santhoshse7en.github.io/imdby_doc)
[![Downloads](https://pepy.tech/badge/imdby/month)](https://pepy.tech/project/imdby)


# 🎬 imdby

**imdby** is a Python package designed to retrieve and manage data from the [IMDb](https://www.imdb.com/) database — including information about movies, people, characters, companies, events, and news.

---

## 🔗 Project Links

| Resource         | Link                                                     |
| ---------------- | -------------------------------------------------------- |
| 📦 PyPI          | [imdby on PyPI](https://pypi.org/project/imdby/)         |
| 🛠 Repository    | [GitHub Repo](https://github.com/santhoshse7en/imdby/)   |
| 📚 Documentation | [imdby Docs](https://santhoshse7en.github.io/imdby_doc/) |

---

## 🚀 Features

* Retrieve and manage comprehensive IMDb data: movies, people, characters, companies, and more.
* Perform sentiment analysis on IMDb user reviews using **VADER** and **TextBlob**.
* Compatible with **Python 3** (and backward-compatible with **Python 2.7**).
* Platform-independent and supports both web scraping and local database querying.
* Clean and easy-to-use API.

---

## 📦 Dependencies

* `beautifulsoup4`
* `selenium`
* `chromedriver-binary`
* `vaderSentiment`
* `textblob`
* `pandas`

---

## 🛠 Installation

Install from the GitHub repository (recommended for the latest updates):

```bash
pip install git+https://github.com/santhoshse7en/imdb
```

Or install the latest release from PyPI:

```bash
pip install imdby
```

---

## ✨ Quick Start

Here's a quick example of how to use **imdby**:

```python
from imdb.imdb import IMDb

# Create an instance
ia = IMDb()

# Fetch full cast and crew of a movie by IMDb ID
cast = ia.full_cast_and_crew('tt4154796')

# Print the directors
print('Directors:')
for director in cast.directors:
    print(director)

# Search for a person
people = ia.search_person('Simon Baker')
print(people.person_id, people.person_name)
```

---

## 🆘 Getting Help

For comprehensive usage guides and API reference, check out the [official documentation](https://imdby.readthedocs.io/).

---

## 🤝 Contributing

We welcome contributions!
If you're planning a significant change, please open an issue first to discuss your ideas.
Make sure to update or add relevant tests.

---

## 👥 Contributors

Big thanks to all the contributors who help make **imdby** better:

* **Sai Harsha Kurapati** – [@harshasic](https://github.com/harshasic)

Want to contribute? Fork the repo and send a pull request!

---

## 📄 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
