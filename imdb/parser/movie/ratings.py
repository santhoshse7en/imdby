from imdb.utils.config import base_uri, imdb_uris, tag_search
from imdb.utils.helpers import (catch, digits, rating_demo_df,
                                rating_demo_region_df, rating_df, unicode)
from imdb.utils.utils import BeautifulSoup, get, pd, re


# Retrieves IMDb Plot Details
class ratings:

    """
    Collects IMDb Ratings Details of the multi-media content in IMDb when title_id is given.
    :param title_id: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, title_id):
        self.title_id = title_id
        self.ratings_uri = imdb_uris["ratings"] % self.title_id
        soup = BeautifulSoup(get(self.ratings_uri).text, 'lxml')

        """
        :returns: Holds page Info tags
        """
        rating_demo_tag = catch('None', lambda: soup.find(
            'div', string=tag_search['rating_demo']).findNext('table'))

        """
        :returns: Movie Title
        """
        movie_tag = catch(
            'None', lambda: soup.select_one('h3[itemprop="name"]'))
        self.title = catch('None', lambda: unicode(movie_tag.a.get_text()))
        self.title_url = catch('None', lambda: unicode(
            '%s%s' % (base_uri, movie_tag.a['href'][1:])))
        self.year = catch('None', lambda: int(re.findall(
            r"\d+", unicode(movie_tag.select_one('.nobr').get_text()))[0]))

        """
        :returns: Rating Demographics
        """
        self.rating_df = catch('None', lambda: rating_df(rating_demo_tag))
        self.rating_demo_df = catch(
            'None', lambda: rating_demo_df(rating_demo_tag))
        self.rating_demo_us_df = catch(
            'None', lambda: rating_demo_region_df(rating_demo_tag))
        self.rating_math = catch('dict', lambda: {'Arithmetic Mean': rating_demo_tag.findPrevious('table').findNextSibling('div', class_="allText").get_text().split()[3],
                                                  'Median': rating_demo_tag.findPrevious('table').findNextSibling('div', class_="allText").get_text().split()[-1]})

        """
        :returns: Rating
        """
        self.votes = catch('None', lambda: digits(
            soup.select_one('.allText').contents[0]))
        self.rating = catch('None', lambda: float(
            soup.select_one('.allText').contents[2].split()[2:][0]))
