# Installation

This part of the documentation covers the installation of newspaper. The first step to using any software package is getting it properly installed.

## Dependencies

* beautifulsoup4
* selenium
* chromedriver-binary
* vaderSentiment
* textblob
* pandas

## Distribute & Pip

Installing imdby is simple with pip.

```bash
$ pip install imdby
```

## Get the Code

imdby is actively developed on GitHub, where the code is [always available](https://github.com/santhoshse7en/imdby).

You can clone the public repository:

```bash
git clone git://github.com/santhoshse7en/imdby.git
```

Once you have a copy of the source, you can embed it in your Python package, or install it into your site-packages easily:

```bash
$ pip install -r requirements.txt
$ python setup.py install
```

Feel free to give our testing suite a shot:

```bash
$ python imdby/imdb.py
```
