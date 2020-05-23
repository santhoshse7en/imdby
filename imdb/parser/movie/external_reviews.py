from imdb.utils.config import base_uri, imdb_uris
from imdb.utils.helpers import catch, catch_list, dataframe_data, unicode
from imdb.utils.utils import BeautifulSoup, get, pd, re


# Retrieves IMDb Critic Reviews
class external_reviews:

    """
    Collects critic reviews of the multi media content in IMDb when title_id is given.
    :param user reviews: Unique identification title_id for every multi media content in IMDb.
    :returns: Returns all the user reviews.
    """

    def __init__(self, title_id):
        self.title_id = title_id
        self.user_reviews_url = imdb_uris['externalreviews'] % self.title_id

        # Creating soup for the website
        soup = BeautifulSoup(get(self.user_reviews_url).text, 'lxml')

        """
        :returns: movie title if available.
        """
        movie_tag = soup.select_one('h3[itemprop="name"]')
        self.title = catch(lambda: unicode(movie_tag.a.get_text()))
        self.title_url = catch(lambda: unicode(
            '%s%s' % (base_uri, movie_tag.a['href'][1:])))
        self.year = catch(lambda: int(re.findall(
            r"\d+", unicode(movie_tag.select_one('.nobr').get_text()))[0]))

        """
        :returns: total critic reviews if available.
        """
        self.external_reviews_count = catch(lambda: int(
            ''.join(i for i in soup.select_one('.desc').text if i.isdigit())))

        """
        :returns: critics reviews link if available.
        """
        try:
            links = soup.select_one(
                "#external_reviews_content").findNext("ul").select("li")
            self.external_reviews_df = pd.DataFrame(
                columns=['Title', 'Critic', 'IMDb_URI'])

            for item in links:
                text = catch(lambda: unicode(item.get_text()))
                start = catch(lambda: text.find('['))
                end = catch(lambda: text.find(']'))

                self.external_reviews_df.loc[len(self.external_reviews_df)] = [catch(lambda: unicode(text[:start-1])),
                                                                           catch(lambda: unicode(text[start+1:end])),
                                                                           catch(lambda: unicode('%s%s' % (base_uri, item.a['href'][1:])))]
            self.external_reviews_df = dataframe_data(self.external_reviews_df)
        except:
            self.external_reviews_df = None
