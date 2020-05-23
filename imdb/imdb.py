# Movie Related Information
from imdb.parser.character.search_character_id import search_character_id
from imdb.parser.company.search_company_id import search_company_id
from imdb.parser.event.search_event_id import search_event_id
from imdb.parser.movie.company import company
from imdb.parser.movie.critic_reviews import critic_reviews
from imdb.parser.movie.external_reviews import external_reviews
from imdb.parser.movie.external_sites import external_sites
from imdb.parser.movie.full_cast_and_crew import full_cast_and_crew
from imdb.parser.movie.imdb_charts import imdb_charts
from imdb.parser.movie.movie import movie
from imdb.parser.movie.parental_guide import parental_guide
from imdb.parser.movie.plot import plot
from imdb.parser.movie.plot_keywords import plot_keywords
from imdb.parser.movie.ratings import ratings
from imdb.parser.movie.release_info import release_info
from imdb.parser.movie.search_title_id import search_title_id
from imdb.parser.movie.taglines import taglines
from imdb.parser.movie.technical_spec import technical_spec
from imdb.parser.movie.top_india_charts import top_india_charts
from imdb.parser.movie.trending_now_in_india import trending_now_in_india
from imdb.parser.movie.upcoming_releases import upcoming_releases
from imdb.parser.movie.user_reviews import user_reviews
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
        return company(title_id)

    def critic_reviews(self, title_id):
        return critic_reviews(title_id)

    def external_reviews(self, title_id):
        return external_reviews(title_id)

    def external_sites(self, title_id):
        return external_sites(title_id)

    def full_cast_and_crew(self, title_id):
        return full_cast_and_crew(title_id)

    def imdb_charts(self):
        return imdb_charts()

    def movie(self, title_id):
        return movie(title_id)

    def parental_guide(self, title_id):
        return parental_guide(title_id)

    def plot(self, title_id):
        return plot(title_id)

    def plot_keywords(self, title_id):
        return plot_keywords(title_id)

    def ratings(self, title_id):
        return ratings(title_id)

    def release_info(self, title_id):
        return release_info(title_id)

    def taglines(self, title_id):
        return taglines(title_id)

    def technical_spec(self, title_id):
        return technical_spec(title_id)

    def top_india_charts(self):
        return top_india_charts()

    def trending_now_in_india(self):
        return trending_now_in_india()

    def upcoming_releases(self):
        return upcoming_releases()

    def user_reviews(self, title_id, remove_spoiler):
        return user_reviews(title_id, remove_spoiler)


def main():
    IMDb()
