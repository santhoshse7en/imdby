from imdb.utils.config import base_uri, imdb_uris
from imdb.utils.helpers import catch, trending_now, trending_now_df
from imdb.utils.utils import BeautifulSoup, get


# Retrieves IMDb Trending Now in India Details
class trending_now_in_india:

    """
    Collects trending_now_in_india details of the multi-media content in IMDb.
    """

    def __init__(self):

        self.upcoming_movies_url = imdb_uris["upcoming"]
        self.popular_tamil_url = imdb_uris["tamil"]
        self.popular_telugu_url = imdb_uris["telugu"]
        self.popular_india_url = imdb_uris["released"]
        self.popular_global_url = imdb_uris["global"]
        self.popular_hindi_url = imdb_uris["hindi"]

        upcoming_soup = BeautifulSoup(
            get(self.upcoming_movies_url).text, 'lxml')
        popular_tamil_soup = BeautifulSoup(
            get(self.popular_tamil_url).text, 'lxml')
        popular_telugu_soup = BeautifulSoup(
            get(self.popular_telugu_url).text, 'lxml')
        popular_india_soup = BeautifulSoup(
            get(self.popular_india_url).text, 'lxml')
        popular_global_soup = BeautifulSoup(
            get(self.popular_global_url).text, 'lxml')
        popular_hindi_soup = BeautifulSoup(
            get(self.popular_hindi_url).text, 'lxml')

        """
        :returns: Upcoming DataFrame
        """
        self.upcoming_movies_df = catch(
            lambda: trending_now_df(trending_now(upcoming_soup)))

        """
        :returns: popular_tamil_movies DataFrame
        """
        self.popular_tamil_movies_df = catch(
            lambda: trending_now_df(trending_now(popular_tamil_soup)))

        """
        :returns: popular_telugu_movies DataFrame
        """
        self.popular_telugu_movies_df = catch(
            lambda: trending_now_df(trending_now(popular_telugu_soup)))

        """
        :returns: Popular India DataFrame
        """
        self.popular_india_movies_df = catch(
            lambda: trending_now_df(trending_now(popular_india_soup)))

        """
        :returns: Poppular Global DataFrame
        """
        self.popular_global_movies_df = catch(
            lambda: trending_now_df(trending_now(popular_global_soup)))

        """
        :returns: Poppular Hindi DataFrame
        """
        self.popular_hindi_movies_df = catch(
            lambda: trending_now_df(trending_now(popular_hindi_soup)))
