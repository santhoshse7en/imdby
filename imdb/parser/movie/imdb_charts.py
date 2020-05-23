from imdb.utils.config import base_uri, imdb_uris
from imdb.utils.helpers import catch, top_250, top_box_office
from imdb.utils.utils import BeautifulSoup, get, pd, re


# Retrieves IMDb Charts Details
class imdb_charts:

    """
    Collects top rated movies details of the multi-media content in IMDb.
    """

    def __init__(self):

        self.top_rated_movies_url = imdb_uris["top"]
        self.top_rated_english_movies_url = imdb_uris["top-english-movies"]
        self.top_box_office_us_url = imdb_uris["boxoffice"]
        self.most_popular_movies_url = imdb_uris["moviemeter"]
        self.lowest_rated_movies_url = imdb_uris["bottom"]
        self.top_rated_tv_shows_url = imdb_uris["toptv"]
        self.most_popular_tv_shows_url = imdb_uris["tvmeter"]

        top_soup = BeautifulSoup(get(self.top_rated_movies_url).text, 'lxml')
        box_office_soup = BeautifulSoup(
            get(self.top_box_office_us_url).text, 'lxml')
        most_popular_movies_soup = BeautifulSoup(
            get(self.most_popular_movies_url).text, 'lxml')
        bottom_soup = BeautifulSoup(
            get(self.lowest_rated_movies_url).text, 'lxml')
        toptv_soup = BeautifulSoup(
            get(self.top_rated_tv_shows_url).text, 'lxml')
        most_popular_tv_shows_soup = BeautifulSoup(
            get(self.most_popular_tv_shows_url).text, 'lxml')
        top_english_soup = BeautifulSoup(
            get(self.top_rated_english_movies_url).text, 'lxml')

        """
        :returns: top_rated_movies DataFrame
        """
        self.top_rated_movies_df = catch(lambda: top_250(
            top_soup.select_one('.lister-list').select('tr')))

        """
        :returns: top_rated_english_movies DataFrame
        """
        self.top_rated_english_movies_df = catch(lambda: top_250(
            top_english_soup.select_one('.lister-list').select('tr')))

        """
        :returns: lowest_rated_movies DataFrame
        """
        self.lowest_rated_movies_df = catch(lambda: top_250(
            bottom_soup.select_one('.lister-list').select('tr')))

        """
        :returns: most_popular_movies DataFrame
        """
        self.most_popular_movies_df = catch(lambda: top_250(
            most_popular_movies_soup.select_one('.lister-list').select('tr')))

        """
        :returns: top_rated_tv_shows DataFrame
        """
        self.top_rated_tv_shows_df = catch(lambda: top_250(
            toptv_soup.select_one('.lister-list').select('tr')))

        """
        :returns: most_popular_tv_shows DataFrame
        """
        self.most_popular_tv_shows_df = catch(lambda: top_250(
            most_popular_tv_shows_soup.select_one('.lister-list').select('tr')))

        """
        :returns: top_box_office_us_movies DataFrame
        """
        box_office = catch(
            lambda: box_office_soup.select_one('#boxoffice').h4.text)
        date = catch(lambda: box_office[11:-6].split(' - '))
        self.top_box_office_df = catch(lambda: top_box_office(
            box_office_soup.select_one('tbody').select('tr'), box_office, date))
