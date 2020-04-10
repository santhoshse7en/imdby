from imdby.utils import *


# Retrieves IMDb Plot Details
class plot:

    """
    Collects IMDb Plot Details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, titleid):
        self.titleid = titleid
        self.plot_url = "https://www.imdb.com/title/%s/plotsummary" % self.titleid
        soup = BeautifulSoup(get(self.plot_url).text, 'lxml')

        """
        :returns: Movie Title
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        """
        :returns: Movie Plot
        """
        try:
            self.plot = ' '.join(soup.select_one('#synopsis').findNext('ul').text.split()).replace("\'", " ")
        except:
            self.plot = None

        """
        :returns: Movies Summaries
        """
        try:
            block = soup.select_one('#summaries').findNext('ul').select('li')
            self.summaries = [' '.join(block[i].text.split()) for i in range(len(block))]
        except:
            self.summaries = None

        """
        :returns: Creates Dict from the above info. if available.
        """
        try:
            self.imdb_plot_metadata = {"Movie Name" : self.title,
                                       "Title ID" : self.titleid,
                                       "Movie Plot URL" : self.plot_url,
                                       "Plot" : self.plot,
                                       "Summaries" : self.summaries}
        except:
            self.imdb_plot_metadata = None

        print("\rPlot Extraction Completed\r", end="\r", flush=True)
