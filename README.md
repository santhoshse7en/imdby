<div align="center">

# 🎬 imdby

**Scrape the IMDb database from Python — movies, people, companies, events, characters, news, charts, and reviews — no official API key required.**

[![PyPI Version](https://img.shields.io/pypi/v/imdby.svg?style=flat-square)](https://pypi.org/project/imdby/)
[![Python Versions](https://img.shields.io/pypi/pyversions/imdby.svg?style=flat-square)](https://pypi.org/project/imdby/)
[![Downloads](https://static.pepy.tech/badge/imdby/month)](https://pepy.tech/project/imdby)
[![License: MIT](https://img.shields.io/pypi/l/imdby.svg?style=flat-square)](https://github.com/santhoshse7en/imdby/blob/master/LICENSE)

[![GitHub Stars](https://img.shields.io/github/stars/santhoshse7en/imdby.svg?style=social\&label=Star)](https://github.com/santhoshse7en/imdby/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/santhoshse7en/imdby.svg?style=social\&label=Fork)](https://github.com/santhoshse7en/imdby/fork)
[![Open Issues](https://img.shields.io/github/issues/santhoshse7en/imdby.svg?style=flat-square)](https://github.com/santhoshse7en/imdby/issues)
[![Last Commit](https://img.shields.io/github/last-commit/santhoshse7en/imdby.svg?style=flat-square)](https://github.com/santhoshse7en/imdby/commits/master)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](#-contributing)

If **imdby** saves you time, please consider giving it a ⭐ — it helps others discover the project.

</div>

---

## 📑 Table of Contents

- [Why imdby?](#-why-imdby)
- [Features](#-features)
- [Dependencies](#-dependencies)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [API Overview](#-api-overview)
- [Getting Help](#-getting-help)
- [Contributing](#-contributing)
- [Star History](#-star-history)
- [Contributors](#-contributors)
- [License](#-license)

---

## 💡 Why imdby?

IMDb doesn't offer a public API, and existing solutions are often abandoned or limited to a narrow slice of the site. **imdby** scrapes IMDb's own pages directly and hands the result back as ready-to-use Python objects and `pandas` DataFrames — no scraping boilerplate, no API key, no rate-limit approval process.

---

## 🚀 Features

* Retrieve IMDb data for a title: overview, plot, plot keywords, taglines, full cast & crew, company credits, release info, ratings breakdown, parental guide, technical specs, critic reviews, and external reviews/sites.
* Retrieve IMDb charts: Top 250, Top 250 (English), Bottom 100, box office, MovieMeter/TVMeter, Top TV, and India-specific charts (Tamil, Telugu, Malayalam, trending, upcoming).
* Scrape a title's user reviews and score them with **VADER** and **TextBlob** sentiment analysis.
* Look up IMDb IDs for a title, person, company, event, character, or news item by search text.
* Results come back as plain Python objects and `pandas` DataFrames, ready for further analysis.
* Compatible with **Python 3.10+** (tested through Python 3.14).

---

## 📦 Dependencies

* `beautifulsoup4` + `lxml` — HTML parsing
* `requests` — HTTP requests
* `selenium` — used only by `user_reviews()` to load additional review pages. Requires a local
  **Google Chrome** install; the matching chromedriver is downloaded automatically by Selenium's
  built-in Selenium Manager, so no separate driver package is needed.
* `pandas` — tabular results
* `nltk` (VADER) + `textblob` — review sentiment analysis. The VADER lexicon is downloaded
  automatically on first use.
* `unidecode` — text normalization

---

## 📥 Installation

Install the latest release from PyPI:

```bash
pip install imdby
```

Or install from GitHub for the latest, unreleased changes:

```bash
pip install git+https://github.com/santhoshse7en/imdby
```

---

## ✨ Quick Start

```python
from imdb.imdb import IMDb

ia = IMDb()

# Fetch full cast and crew of a movie by IMDb ID
cast = ia.full_cast_and_crew('tt4154796')

print('Directors:')
for director in cast.directors_name:
    print(director)

# Fetch core movie details
movie = ia.movie('tt4154796')
print(movie.title, movie.rating, movie.genre)

# Browse the IMDb Top 250 as a DataFrame
charts = ia.imdb_charts()
print(charts.top_rated_movies_df.head())

# Search for a person (prompts for a serial number from the printed matches)
people = ia.search_person('Simon Baker')
print(people.person_id, people.name)
```

> **Note:** the `search_*` methods (`search_movie`, `search_person`, `search_company`, `search_event`,
> `search_character`, `search_news`) and `upcoming_releases()` are interactive — they print numbered
> suggestions to the console and use `input()` to read your selection.

---

## 📖 API Overview

All methods are called on an `IMDb()` instance.

### Search (interactive, resolves a name to an IMDb ID)

| Method                    | Returns (key attributes)                     |
| ------------------------- | --------------------------------------------- |
| `search_movie(text)`      | `.title_name`, `.title_id`                    |
| `search_person(text)`     | `.name`, `.person_id`                         |
| `search_company(text)`    | `.company_name`, `.company_id`                |
| `search_event(text)`      | `.event_name`, `.event_id`                    |
| `search_character(text)`  | `.character_name`, `.character_id`            |
| `search_news(text)`       | `.news_title`, `.news_id`                     |

### Title details (take a `title_id`, e.g. `'tt4154796'`)

| Method                      | Data                                                        |
| ---------------------------- | ------------------------------------------------------------ |
| `movie(title_id)`            | Title, rating, votes, genres, metascore, budget/gross, storyline |
| `plot(title_id)`             | Plot summary and synopsis                                    |
| `plot_keywords(title_id)`    | Plot keyword list                                             |
| `taglines(title_id)`         | Taglines list                                                 |
| `full_cast_and_crew(title_id)` | Directors, writers, cast, producers, music, cinematography, editing, casting |
| `company(title_id)`          | Production companies, distributors, special effects, other companies |
| `release_info(title_id)`     | Release dates by country, India release date, "Also Known As" titles |
| `ratings(title_id)`          | Rating breakdown by demographic and region                    |
| `parental_guide(title_id)`   | MPAA rating, certificates, and content advisories (nudity, violence, profanity, alcohol, frightening, spoilers) |
| `technical_spec(title_id)`   | Runtime, sound mix, color, aspect ratio, camera, film format   |
| `critic_reviews(title_id)`   | Critic review scores and summaries                             |
| `external_reviews(title_id)` | Links to external critic reviews                               |
| `external_sites(title_id)`   | Official sites, miscellaneous sites, photos, video links        |
| `user_reviews(title_id, remove_spoiler)` | User reviews with per-review and aggregate sentiment scores (uses Selenium/Chrome) |

### Charts and listings (no arguments)

| Method                     | Data                                                          |
| --------------------------- | -------------------------------------------------------------- |
| `imdb_charts()`             | Top 250, Top 250 (English), Bottom 100, box office, MovieMeter, Top TV, TVMeter |
| `top_india_charts()`        | Top rated Indian, Tamil, Telugu, and Malayalam movies            |
| `trending_now_in_india()`   | Upcoming, popular Tamil/Telugu/India/global/Hindi titles          |
| `upcoming_releases()`       | Interactive: pick a region, then lists upcoming releases there   |

---

## 🆘 Getting Help

* 📚 [Official documentation](https://santhoshse7en.github.io/imdby_doc/)
* 🐛 [Report a bug or request a feature](https://github.com/santhoshse7en/imdby/issues)

---

## 🤝 Contributing

Contributions of all sizes are welcome — bug fixes, new IMDb pages, documentation, or tests.

1. Fork the repo and clone your fork.
2. Create a virtual environment and install in editable mode with dev tools:

   ```bash
   pip install -e ".[dev]"
   ```
3. Make your changes, then lint and verify the package still builds cleanly:

   ```bash
   ruff check imdb/
   python -m build
   python -m twine check dist/*
   ```
4. Open a pull request describing what changed and why.

If you're planning a significant change, please open an issue first to discuss your approach.

---

## ⭐ Star History

See how **imdby**'s stars have grown over time: [Star History for santhoshse7en/imdby](https://star-history.com/#santhoshse7en/imdby&Date)

---

## 👥 Contributors

Big thanks to all the contributors who help make **imdby** better:

* **M Santhosh Kumar** – [@santhoshse7en](https://github.com/santhoshse7en) (author & maintainer)
* **Sai Harsha Kurapati** – [@harshasic](https://github.com/harshasic)

Want to see your name here? Check out the [Contributing](#-contributing) section and send a pull request!

---

## 📄 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
