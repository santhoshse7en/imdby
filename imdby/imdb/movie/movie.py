from imdb_py.config import base_uri, imdb_uris, tag_search
from imdb_py.helper_function import (catch, catch_dict, catch_list, digits,
                                     unicode)
from imdb_py.utils import BeautifulSoup, get


# Retrieves IMDb MovieDetails
class movie_info:

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
        movie_tag = catch(lambda: soup.select_one('h1[class=""]'))
        genre_tag = catch(lambda: soup.find(
            'h4', string='Genres:').findNextSiblings('a'))
        rating_tag = catch(lambda: soup.select_one(
            'span[itemprop="ratingValue"]'))
        rating_count_tag = catch(lambda: soup.select_one(
            'span[itemprop="ratingCount"]'))
        metascore_tag = catch(lambda: soup.select_one('.metacriticScore'))
        summary_tag = catch(lambda: soup.select_one('.summary_text'))
        budget_tag = catch(lambda: soup.find('h4', string='Budget:'))
        opening_weekend_usa_tag = catch(
            lambda: soup.find('h4', string='Opening Weekend USA:'))
        gross_usa_tag = catch(lambda: soup.find('h4', string='Gross USA:'))
        cumulative_worldwide_gross_tag = catch(
            lambda: soup.find('h4', string='Cumulative Worldwide Gross:'))
        poster_tag = catch(lambda: soup.select_one('.poster'))
        year_tag = catch(lambda: soup.select_one('span[id="titleYear"]'))
        review_tag = soup.select_one(
            'div[class="titleReviewBarItem titleReviewbarItemBorder"]')
        popularity_tag = soup.find('div', string=tag_search['popularity'])

        """
        :returns: Movie Name if available.
        """
        self.title = catch(lambda: unicode(movie_tag.contents[0]))

        """
        :returns: Genre types for the movie if available.
        """
        self.genre = catch_list(
            lambda: [unicode(genre.get_text()) for genre in genre_tag])
        self.genre_links = catch_list(lambda: [unicode(
            '%s%s' % (base_uri, genre['href'][1:])) for genre in genre_tag])

        """
        :returns: IMDb rating for the movie if available.
        """
        self.rating = catch(lambda: unicode(rating_tag.get_text()))

        """
        :returns: IMDb votes obtained for the movie if available.
        """
        self.votes = catch(lambda: digits(rating_count_tag.get_text()))

        """
        :returns: Metascore of the movie if available.
        """
        self.metascore = catch(lambda: unicode(metascore_tag.get_text()))
        self.metascore_uri = catch(lambda: unicode(
            "%s/%s" % (self.movie_uri, soup.select_one('.metacriticScore').findParent('a')['href'])))

        """
        :returns: Movie User Review info if available.
        """
        self.user_review_count = catch(lambda: digits(
            review_tag.select_one('a[href="reviews"]').get_text()))
        self.user_review_uri = catch(
            lambda: "%s/%s" % (self.movie_uri, review_tag.select_one('a[href="reviews"]')['href']))

        """
        :returns: Movie Critic Review info if available.
        """
        self.critic_review_count = catch(lambda: digits(
            review_tag.select_one('a[href="externalreviews"]').get_text()))
        self.critic_review_uri = catch(
            lambda: "%s/%s" % (self.movie_uri, review_tag.select_one('a[href="externalreviews"]')['href']))

        """
        :returns: Popularity of the movie if available.
        """
        self.popularity_initial = catch(lambda: digits(
            popularity_tag.findNext('span').contents[0]))
        self.popularity_name = catch(lambda: popularity_tag.findNext(
            'span', class_='titleOverviewSprite').findNext('span')['class'][0])
        self.popularity_value = catch(lambda: digits(popularity_tag.findNext(
            'span', class_='titleOverviewSprite').findNext('span').get_text()))

        """
        :returns: Storyline of the movie if available.
        """
        self.storyline = catch(lambda: unicode(summary_tag.get_text()))

        """
        :returns: Budget of the movie if available.
        """
        self.budget = catch(lambda: unicode(budget_tag.nextSibling))

        """
        :returns: Opening Weekend USA of the movie if available.
        """
        self.opening_weekend_usa = catch(
            lambda: unicode(opening_weekend_usa_tag.nextSibling))

        """
        :returns: Gross USA of the movie if available.
        """
        self.gross_usa = catch(lambda: unicode(gross_usa_tag.nextSibling))

        """
        :returns: Cumulative Worldwide Gross of the movie if available.
        """
        self.cumulative_worldwide_gross = catch(
            lambda: unicode(cumulative_worldwide_gross_tag.nextSibling))

        """
        :returns: Movie Poster URL if available.
        """
        self.movie_poster_uri = catch(lambda: unicode(
            '%s%s' % (base_uri, poster_tag.a['href'][1:])))

        """
        :returns: Movie Released Year if available.
        """
        self.movie_release_year = catch(lambda: unicode(year_tag.a.get_text()))
        self.movie_release_year_link = catch(lambda: unicode(
            imdb_uris['year'] % self.movie_release_year))

        """
        :returns: Creates Meta Data from the above info. if available.
        """
        self.imdb_movie_metadata = catch_dict(lambda: {"Movie Name": self.title,
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
