from imdb.utils.config import base_uri, imdb_uris, tag_search
from imdb.utils.helpers import catch, critic_df, digits, unicode
from imdb.utils.utils import BeautifulSoup, get, pd, re


# Retrieves IMDb Plot Details
class critic_reviews:

    """
    Collects IMDb Ratings Details of the multi-media content in IMDb when title_id is given.
    :param title_id: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, title_id):
        self.title_id = title_id
        self.ratings_uri = imdb_uris["criticreviews"] % self.title_id
        soup = BeautifulSoup(get(self.ratings_uri).text, 'lxml')

        """
        :returns: Holds page Info tags
        """
        critic_tag = catch('None', lambda: soup.select(
            'tr[itemprop="reviews"]'))
        movie_tag = catch(
            'None', lambda: soup.select_one('h3[itemprop="name"]'))

        """
        :returns: Movie Title
        """
        self.title = catch('None', lambda: unicode(movie_tag.a.get_text()))
        self.title_url = catch('None', lambda: unicode(
            '%s%s' % (base_uri, movie_tag.a['href'][1:])))
        self.year = catch('None', lambda: int(re.findall(
            r"\d+", unicode(movie_tag.select_one('.nobr').get_text()))[0]))

        """
        :returns: Critic Review Demographics
        """
        self.critic_reviews_df = catch('None', lambda: critic_df(critic_tag))
