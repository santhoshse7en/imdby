from imdb.utils.config import base_uri, imdb_uris
from imdb.utils.helpers import catch, unicode
from imdb.utils.utils import BeautifulSoup, get, re


# Retrieves IMDb Taglines
class taglines:

    """
    Collects tagline details of the multi-media content in IMDb when title_id is given.
    :param title_id: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, title_id: str) -> bool:
        self.title_id = title_id
        self.taglines_uri = imdb_uris["taglines"] % self.title_id

        soup = BeautifulSoup(get(self.taglines_uri).text, 'lxml')

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
        :returns: Holds page Info tags
        """
        taglines_tag = catch('None', lambda: soup.select_one(
            '#taglines_content').select('.soda'))

        """
        returns: taglines if available
        """
        self.taglines = catch('list', lambda: [unicode(
            tagline.get_text()) for tagline in taglines_tag])

        """
        :returns: Creates Dict from the above info. if available.
        """
        self.imdb_taglines_metadata = catch('dict', lambda: {"Movie Name": self.title,
                                                             "Movie URI": self.title_url,
                                                             "Title ID": self.title_id,
                                                             "Year": self.year,
                                                             "Movie Taglines URI": self.taglines_uri,
                                                             "Taglines": self.taglines})
