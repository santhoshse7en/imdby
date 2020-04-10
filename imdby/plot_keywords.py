from imdby.utils import *


# Retrieves IMDb Plot Keywords Details
class plot_keywords:

    """
    Collects IMDb Plot Keywords Details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, titleid):
        self.titleid = titleid
        self.plot_keywords_url = "https://www.imdb.com/title/%s/keywords" % self.titleid 
        soup = BeautifulSoup(get(self.plot_keywords_url).text, 'lxml')

        """
        :returns: Movie Title
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        """
        :returns: Movie Plot Keywords
        """
        try:
            block = soup.select('td.soda')
            self.plot_keywords = [block[i]['data-item-keyword'] for i in range(len(block))]
        except:
            self.plot_keywords = None

        """
        :returns: Creates Dict from the above info. if available.
        """
        try:
            self.imdb_plot_Keywords_metadata = {"Movie Name" : self.title,
                                                "Title ID" : self.titleid,
                                                "Movie Plot Keywords URL" : self.plot_keywords_url,
                                                "Plot Keywords" : self.plot_keywords}
        except:
            self.imdb_plot_Keywords_metadata = None

        print("\rPlot Keywords Extraction Completed\r", end="\r", flush=True)
