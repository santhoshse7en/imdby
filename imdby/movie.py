from imdby.utils import *


# Retrieves IMDb MovieDetails
class movie:

    """
    Collects basic movie details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, titleid):
        self.titleid = titleid
        self.movie_url = "https://www.imdb.com/title/%s" % str(self.titleid)
        soup = BeautifulSoup(get(self.movie_url).text, 'lxml')

        """
        :returns: Movie Name if available.
        """
        try:
            self.title = soup.select_one('h1[class=""]').contents[0].strip()
        except:
            self.title = None

        """
        :returns: Genre types for the movie if available.
        """
        try:
            self.genre = [soup.find('h4', string='Genres:').findNextSiblings('a')[i].text.strip() for i in range(len(soup.find('h4', string='Genres:').findNextSiblings('a')))]
        except:
            self.genre = None

        """
        :returns: IMDb rating for the movie if available.
        """
        try:
            self.rating = soup.select_one('span[itemprop="ratingValue"]').text.strip()
        except:
            self.rating = None

        """
        :returns: IMDb votes obtained for the movie if available.
        """
        try:
            self.votes = soup.select_one('span[itemprop="ratingCount"]').text.strip()
        except:
            self.votes = None

        """
        :returns: Metascore of the movie if available.
        """
        try:
            self.metascore = soup.select_one('.metacriticScore').text.replace(u'\xa0', u' ').strip()
        except:
            self.metascore = None

        """
        :returns: Storyline of the movie if available.
        """
        try:
            self.storyline = soup.select_one('.summary_text').text.strip()
        except:
            self.storyline = None

        """
        :returns: Budget of the movie if available.
        """
        try:
            self.budget = soup.find('h4', string='Budget:').nextSibling.replace(u'\xa0', u' ').strip()
        except:
            self.budget = None

        """
        :returns: Opening Weekend USA of the movie if available.
        """
        try:
            self.opening_weekend_usa = soup.find('h4', string='Opening Weekend USA:').nextSibling.replace(u'\xa0', u' ').strip()
        except:
            self.opening_weekend_usa = None

        """
        :returns: Gross USA of the movie if available.
        """
        try:
            self.gross_usa = soup.find('h4', string='Gross USA:').nextSibling.replace(u'\xa0', u' ').strip()
        except:
            self.gross_usa = None

        """
        :returns: Cumulative Worldwide Gross of the movie if available.
        """
        try:
            self.cumulative_worldwide_gross = soup.find('h4', string='Cumulative Worldwide Gross:').nextSibling.replace(u'\xa0', u' ').strip()
        except:
            self.cumulative_worldwide_gross = None

        """
        :returns: Movie Poster URL if available.
        """
        try:
            self.movie_poster_url = 'https://www.imdb.com%s' % soup.select_one('.poster').a['href']
        except:
            self.movie_poster_url = None

        """
        :returns: Movie Released Year if available.
        """
        try:
            self.movie_release_year = soup.select_one('span[id="titleYear"]').a.text.strip()
        except:
            self.movie_release_year = None

        """
        :returns: Creates Meta Data from the above info. if available.
        """
        try:
            self.imdb_movie_metadata = {"Movie Name" : self.title,
                                        "Title ID" : self.titleid,
                                        "Rating" : self.rating,
                                        "IMDb Votes" : self.votes,
                                        "Genre" : self.genre,
                                        "Year" : self.movie_release_year,
                                        "Metascore" : self.metascore,
                                        "Movie Poster URL" : self.movie_poster_url,
                                        "Budget" : self.budget,
                                        "Opening Weekend USA" : self.opening_weekend_usa,
                                        "Cumulative Worldwide Gross" : self.cumulative_worldwide_gross,
                                        "Gross USA" : self.gross_usa,
                                        "Storyline" : self.storyline,
                                        "Movie URL" : self.movie_url}
        except:
            self.imdb_movie_metadata = None

        print("\rBasic Movie Info Extraction Completed\r", end="\r", flush=True)
