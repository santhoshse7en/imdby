from imdby.utils import *


# Retrieves IMDb Critic Reviews
class critic_reviews:

    """
    Collects critic reviews of the multi media content in IMDb when titleid is given.
    :param user reviews: Unique identification titleid for every multi media content in IMDb.
    :returns: Returns all the user reviews.
    """

    def __init__(self, titleid):
        self.titleid = titleid
        self.user_reviews_url = "https://www.imdb.com/title/%s/externalreviews" % self.titleid

        # Creating soup for the website
        soup = BeautifulSoup(get(self.user_reviews_url).text, 'lxml')

        """
        :returns: movie title if available.
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        """
        :returns: total critic reviews if available.
        """
        try:
            self.critic_reviews_count = int(''.join(i for i in soup.select_one('.desc').text if i.isdigit()))
        except:
            self.critic_reviews_count = None

        """
        :returns: critics reviews link if available.
        """
        try:
            links = soup.select_one("#external_reviews_content").findNext("ul").select("li")
            self.critic_reviews_df = pd.DataFrame(columns=['Title', 'URL'])

            for item in links:
                try:
                    self.critic_reviews_df.loc[len(self.critic_reviews_df)] = [item.a.text.strip(),
                                                                               get('https://www.imdb.com%s' % item.a['href']).url]
                except:
                    pass
        except:
            self.critic_reviews_df = None

        print("\rCritic Reviews Extraction Completed\r", end="\r", flush=True)

# main class which passes the titleid to indiviual class
class imdb:
    def __init__(self, titleid):
        start_time = datetime.now()
        critic_reviews.__init__(self, titleid)

        time_delta = datetime.now() - start_time
        print("\rCalculating time taken for critic reviews extraction : %s  seconds\r" % (time_delta.seconds), end="\r", flush=True)
