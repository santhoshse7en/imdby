# Movie Related Information
from imdb.parser.character.search_character_id import search_character_id
from imdb.parser.company.search_company_id import search_company_id
from imdb.parser.event.search_event_id import search_event_id
from imdb.parser.movie.company import company as _company
from imdb.parser.movie.critic_reviews import critic_reviews as _critic_reviews
from imdb.parser.movie.external_reviews import external_reviews as _external_reviews
from imdb.parser.movie.external_sites import external_sites as _external_sites
from imdb.parser.movie.full_cast_and_crew import full_cast_and_crew as _full_cast_and_crew
from imdb.parser.movie.imdb_charts import imdb_charts as _imdb_charts
from imdb.parser.movie.movie import movie as _movie
from imdb.parser.movie.parental_guide import parental_guide as _parental_guide
from imdb.parser.movie.plot import plot as _plot
from imdb.parser.movie.plot_keywords import plot_keywords as _plot_keywords
from imdb.parser.movie.ratings import ratings as _ratings
from imdb.parser.movie.release_info import release_info as _release_info
from imdb.parser.movie.search_title_id import search_title_id
from imdb.parser.movie.taglines import taglines as _taglines
from imdb.parser.movie.technical_spec import technical_spec as _technical_spec
from imdb.parser.movie.top_india_charts import top_india_charts as _top_india_charts
from imdb.parser.movie.trending_now_in_india import trending_now_in_india as _trending_now_in_india
from imdb.parser.movie.upcoming_releases import upcoming_releases as _upcoming_releases
from imdb.parser.movie.user_reviews import user_reviews as _user_reviews
from imdb.parser.news.search_news_id import search_news_id
from imdb.parser.person.search_person_id import search_person_id


class IMDb:

    """
    :returns: Search IMDb ID about Movies, Person, Company, Event, Character, News
    """

    def search_movie(self, text):
        return search_title_id(text)

    def search_person(self, text):
        return search_person_id(text)

    def search_company(self, text):
        return search_company_id(text)

    def search_event(self, text):
        return search_event_id(text)

    def search_character(self, text):
        return search_character_id(text)

    def search_news(self, text):
        return search_news_id(text)

    """
    :returns: Parser contains all kind of movie information
    """

    def company(self, title_id):
        return _company(title_id)

    def critic_reviews(self, title_id):
        return _critic_reviews(title_id)

    def external_reviews(self, title_id):
        return _external_reviews(title_id)

    def external_sites(self, title_id):
        return _external_sites(title_id)

    def full_cast_and_crew(self, title_id):
        return _full_cast_and_crew(title_id)

    def imdb_charts(self):
        return _imdb_charts()

    def movie(self, title_id):
        return _movie(title_id)

    def parental_guide(self, title_id):
        return _parental_guide(title_id)

    def plot(self, title_id):
        return _plot(title_id)

    def plot_keywords(self, title_id):
        return _plot_keywords(title_id)

    def ratings(self, title_id):
        return _ratings(title_id)

    def release_info(self, title_id):
        return _release_info(title_id)

    def taglines(self, title_id):
        return _taglines(title_id)

    def technical_spec(self, title_id):
        return _technical_spec(title_id)

    def top_india_charts(self):
        return _top_india_charts()

    def trending_now_in_india(self):
        return _trending_now_in_india()

    def upcoming_releases(self):
        return _upcoming_releases()

    def user_reviews(self, title_id, remove_spoiler):
        return _user_reviews(title_id, remove_spoiler)