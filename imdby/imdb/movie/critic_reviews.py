from imdby.utils.config import base_uri, imdb_uris, tag_search
from imdby.utils.helpers import catch, catch_dict, critic_df, digits, unicode
from imdby.utils.utils import BeautifulSoup, get, pd, re


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
        critic_tag = soup.select('tr[itemprop="reviews"]')

        """
        :returns: Movie Title
        """
        movie_tag = soup.select_one('h3[itemprop="name"]')
        self.title = catch(lambda: unicode(movie_tag.a.get_text()))
        self.title_url = catch(lambda: unicode(
            '%s%s' % (base_uri, movie_tag.a['href'][1:])))
        self.year = catch(lambda: int(re.findall(
            r"\d+", unicode(movie_tag.select_one('.nobr').get_text()))[0]))

        """
        :returns: Critic Review Demographics
        """
        self.critic_reviews_df = catch(lambda: critic_df(critic_tag))
