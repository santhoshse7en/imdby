from imdb.utils.config import base_uri, imdb_uris
from imdb.utils.helpers import catch, unicode
from imdb.utils.utils import BeautifulSoup, get, re


# Retrieves IMDb Plot Keywords Details
class plot_keywords:

    """
    Collects IMDb Plot Keywords Details of the multi-media content in IMDb when title_id is given.
    :param title_id: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, title_id):
        self.title_id = title_id
        self.plot_keywords_url = imdb_uris["keywords"] % self.title_id
        soup = BeautifulSoup(get(self.plot_keywords_url).text, 'lxml')

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
        :returns: Movie Plot Keywords
        """
        block = catch('None', lambda: soup.select('td.soda'))
        self.plot_keywords = catch(
            'list', lambda: [tag['data-item-keyword'] for tag in block])

        """
        :returns: Creates Dict from the above info. if available.
        """
        self.imdb_plot_Keywords_metadata = catch('dict', lambda: {"Movie Name": self.title,
                                                                  "Movie URI": self.title_url,
                                                                  "Title ID": self.title_id,
                                                                  "Year": self.year,
                                                                  "Movie Plot Keywords URL": self.plot_keywords_url,
                                                                  "Plot Keywords": self.plot_keywords})
