from imdb.utils.config import base_uri, imdb_uris
from imdb.utils.helpers import catch, top_250
from imdb.utils.utils import BeautifulSoup, get, pd, re


# Retrieves IMDb Top India Charts Details
class top_india_charts:

    """
    Collects top india charts details of the multi-media content in IMDb.
    """

    def __init__(self):
        self.top_rated_indian_movies_url = imdb_uris["top-rated-indian-movies"]
        self.top_rated_tamil_movies_url = imdb_uris["top-rated-tamil-movies"]
        self.top_rated_telugu_movies_url = imdb_uris["top-rated-telugu-movies"]
        self.top_rated_malayalam_movies_url = imdb_uris["top-rated-malayalam-movies"]

        indian_soup = BeautifulSoup(
            get(self.top_rated_indian_movies_url).text, 'lxml')
        tamil_soup = BeautifulSoup(
            get(self.top_rated_tamil_movies_url).text, 'lxml')
        telugu_soup = BeautifulSoup(
            get(self.top_rated_telugu_movies_url).text, 'lxml')
        malayalam_soup = BeautifulSoup(
            get(self.top_rated_malayalam_movies_url).text, 'lxml')

        """
        :returns: top_rated_indian_movies DataFrame
        """
        self.top_rated_indian_movies_df = catch('None', lambda: top_250(indian_soup))

        """
        :returns: top_rated_tamil_movies DataFrame
        """
        self.top_rated_tamil_movies_df = catch('None', lambda: top_250(tamil_soup))

        """
        :returns: top_rated_telugu_movies DataFrame
        """
        self.top_rated_telugu_movies_df = catch('None', lambda: top_250(telugu_soup))

        """
        :returns: top_rated_malayalam_movies DataFrame
        """
        self.top_rated_malayalam_movies_df = catch('None', lambda: top_250(malayalam_soup))
