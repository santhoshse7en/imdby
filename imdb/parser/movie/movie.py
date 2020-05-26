from imdb.utils.config import base_uri, imdb_uris, tag_search
from imdb.utils.helpers import catch, digits, unicode
from imdb.utils.utils import BeautifulSoup, get


# Retrieves IMDb MovieDetails
class movie:

    """
    Collects basic movie details of the multi-media content in IMDb when title_id is given.
    :param title_id: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, title_id: str) -> bool:
        self.title_id = title_id
        self.movie_uri = imdb_uris["title"] % self.title_id

        soup = BeautifulSoup(get(self.movie_uri).text, 'lxml')

        """
        :returns: Holds page Info tags
        """
        tags = {'movie': catch('None', lambda: soup.select_one('h1[class=""]')),
                'genre': catch('None', lambda: soup.find('h4', string='Genres:').findNextSiblings('a')),
                'rating': catch('None', lambda: soup.select_one('span[itemprop="ratingValue"]')),
                'votes': catch('None', lambda: soup.select_one('span[itemprop="ratingCount"]')),
                'metascore': catch('None', lambda: soup.select_one('.metacriticScore')),
                'summary': catch('None', lambda: soup.select_one('.summary_text')),
                'budget': catch('None', lambda: soup.find('h4', string='Budget:')),
                'opening_weekend_usa': catch('None', lambda: soup.find('h4', string='Opening Weekend USA:')),
                'gross_usa': catch('None', lambda: soup.find('h4', string='Gross USA:')),
                'cumulative_worldwide_gross': catch('None', lambda: soup.find('h4', string='Cumulative Worldwide Gross:')),
                'poster': catch('None', lambda: soup.select_one('.poster')),
                'year': catch('None', lambda: soup.select_one('span[id="titleYear"]')),
                'review': catch('None', lambda: soup.select_one('div[class="titleReviewBarItem titleReviewbarItemBorder"]')),
                'popularity': catch('None', lambda: soup.find('div', string=tag_search['popularity']))}

        """
        :returns: Movie Name if available.
        """
        self.title = catch('None', lambda: unicode(tags['movie'].contents[0]))

        """
        :returns: Genre types for the movie if available.
        """
        self.genre = catch('list', lambda: [unicode(
            genre.get_text()) for genre in tags['genre']])
        self.genre_links = catch('list', lambda: [unicode(
            '%s%s' % (base_uri, genre['href'][1:])) for genre in tags['genre']])

        """
        :returns: IMDb rating for the movie if available.
        """
        self.rating = catch('None', lambda: unicode(tags['rating'].get_text()))

        """
        :returns: IMDb votes obtained for the movie if available.
        """
        self.votes = catch('None', lambda: digits(tags['votes'].get_text()))

        """
        :returns: Metascore of the movie if available.
        """
        self.metascore = catch('None', lambda: unicode(
            tags['metascore'].get_text()))
        self.metascore_uri = catch('None', lambda: unicode(
            "%s/%s" % (self.movie_uri, tags['metascore'].findParent('a')['href'])))

        """
        :returns: Movie User Review info if available.
        """
        self.user_review_count = catch('None', lambda: digits(
            tags['review'].select_one('a[href="reviews"]').get_text()))
        self.user_review_uri = catch('None', lambda: "%s/%s" % (
            self.movie_uri, tags['review'].select_one('a[href="reviews"]')['href']))

        """
        :returns: Movie Critic Review info if available.
        """
        self.critic_review_count = catch('None', lambda: digits(
            tags['review'].select_one('a[href="externalreviews"]').get_text()))
        self.critic_review_uri = catch('None', lambda: "%s/%s" % (
            self.movie_uri, tags['review'].select_one('a[href="externalreviews"]')['href']))

        """
        :returns: Popularity of the movie if available.
        """
        self.popularity_initial = catch('None', lambda: digits(
            tags['popularity'].findNext('span').contents[0]))
        self.popularity_name = catch('None', lambda: tags['popularity'].findNext(
            'span', class_='titleOverviewSprite').findNext('span')['class'][0])
        self.popularity_value = catch('None', lambda: digits(tags['popularity'].findNext(
            'span', class_='titleOverviewSprite').findNext('span').get_text()))

        """
        :returns: Storyline of the movie if available.
        """
        self.storyline = catch(
            'None', lambda: unicode(tags['summary'].get_text()))

        """
        :returns: Budget of the movie if available.
        """
        self.budget = catch('None', lambda: unicode(
            tags['budget'].nextSibling))

        """
        :returns: Opening Weekend USA of the movie if available.
        """
        self.opening_weekend_usa = catch('None', lambda: unicode(
            tags['opening_weekend_usa'].nextSibling))

        """
        :returns: Gross USA of the movie if available.
        """
        self.gross_usa = catch('None', lambda: unicode(
            tags['gross_usa'].nextSibling))

        """
        :returns: Cumulative Worldwide Gross of the movie if available.
        """
        self.cumulative_worldwide_gross = catch('None', lambda: unicode(
            tags['cumulative_worldwide_gross'].nextSibling))

        """
        :returns: Movie Poster URL if available.
        """
        self.movie_poster_uri = catch('None', lambda: unicode(
            '%s%s' % (base_uri, tags['poster'].a['href'][1:])))

        """
        :returns: Movie Released Year if available.
        """
        self.movie_release_year = catch(
            'None', lambda: unicode(tags['year'].a.get_text()))
        self.movie_release_year_link = catch('None', lambda: unicode(
            imdb_uris['year'] % self.movie_release_year))

        """
        :returns: Creates Meta Data from the above info. if available.
        """
        self.imdb_movie_metadata = catch('dict', lambda: {"Movie Name": self.title,
                                                          "Movie URI": self.movie_uri,
                                                          "Title ID": self.title_id,
                                                          "Rating": self.rating,
                                                          "IMDb Votes": self.votes,
                                                          "Genre": self.genre,
                                                          "Genre Links": self.genre_links,
                                                          "Year": self.movie_release_year,
                                                          "Year Links": self.movie_release_year_link,
                                                          "Metascore": self.metascore,
                                                          "Metascore Link": self.metascore_uri,
                                                          "User Review Count": self.user_review_count,
                                                          "User Review Link": self.user_review_uri,
                                                          "Critic Review Count": self.critic_review_count,
                                                          "Critic Review Link": self.critic_review_uri,
                                                          "Popularity Initial": self.popularity_initial,
                                                          "Popularity Name": self.popularity_name,
                                                          "Popularity value": self.popularity_value,
                                                          "Movie Poster URI": self.movie_poster_uri,
                                                          "Budget": self.budget,
                                                          "Opening Weekend USA": self.opening_weekend_usa,
                                                          "Cumulative Worldwide Gross": self.cumulative_worldwide_gross,
                                                          "Gross USA": self.gross_usa,
                                                          "Storyline": self.storyline})
