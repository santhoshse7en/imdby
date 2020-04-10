from imdby.utils import *


# Retrieves IMDb Taglines
class taglines:

    """
    Collects tagline details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, titleid):
        self.titleid = titleid
        self.taglines_url = "https://www.imdb.com/title/" + str(self.titleid) + "/taglines"
        soup = BeautifulSoup(get(self.taglines_url).text, 'lxml')
        taglines = soup.select_one('#taglines_content').select('.soda')

        """
        returns: Movie Title if available
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        """
        returns: taglines if available
        """
        try:
            self.taglines = [' '.join(taglines[i].text.split()) for i in range(len(taglines))]
        except:
            self.taglines = None

        """
        :returns: Creates Dict from the above info. if available.
        """
        try:
            self.imdb_taglines_metadata = {"Movie Title" : self.title,
                                           "Title ID" : self.titleid,
                                           "Movie Taglines URL" : self.taglines_url,
                                           "Taglines" : self.taglines}
        except:
            self.imdb_taglines_metadata = None

        print("\rTaglines Extraction Completed\r", end="\r", flush=True)
