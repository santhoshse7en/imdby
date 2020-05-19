from imdby.utils.config import base_uri, imdb_uris
from imdby.utils.helpers import (catch, catch_list, review_df,
                                     sentiment_textblob, unicode, digits)
from imdby.utils.utils import (BeautifulSoup, By, Options,
                           SentimentIntensityAnalyzer, WebDriverWait,
                           chromedriver_binary, ec, get, pd, re, sys, time,
                           webdriver)


# Retrieves IMDb User Reviews
class user_reviews:

    """
    Collects user reviews of the multi media content in IMDb when title_id is given.
    :param user reviews:
        1. Unique identification title_id for every multi media content in IMDb.
        2. Spoiler Reviews enabled using Boolean value
    :returns: Returns all the user reviews.
    """

    def __init__(self, title_id: str, remove_spoiler: False):
        self.title_id = title_id

        if remove_spoiler is False:
            self.user_reviews_url = imdb_uris['reviews'] % self.title_id
        else:
            self.user_reviews_url = imdb_uris['spoiler_reviews'] % self.title_id

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

        # for collection of number of reviews
        reviews_count = digits(soup.select_one('div.header').span.text)

        maxclicks = int(reviews_count)//25

        options = Options()
        options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
        wait = WebDriverWait(browser, 100)
        browser.get(self.user_reviews_url)

        clicks = 0
        while True:
            clicks += 1
            if clicks <= maxclicks:
                wait.until(ec.visibility_of_element_located(
                    (By.CLASS_NAME, "ipl-load-more__button"))).click()
            else:
                break
            sys.stdout.write(
                "\r%s - clicks has made for scrolling out of - %s\r" % (str(clicks), str(maxclicks)))
            sys.stdout.flush()
        time.sleep(1)

        soup = BeautifulSoup(browser.page_source, 'lxml')
        browser.quit()

        container = soup.select('.review-container')
        self.total_user_reviews = len(container)

        analyser = SentimentIntensityAnalyzer()
        neu_sum, neg_sum, compound_sum, pos_sum, count = [0] * 5

        self.user_reviews_df = catch(lambda: review_df(analyser, container))

        self.user_reviews = catch_list(
            lambda: self.user_reviews_df.User_Reviews.tolist())

        for review in self.user_reviews:
            count += 1
            score = analyser.polarity_scores(review)
            neu_sum += score['neu']
            neg_sum += score['neg']
            pos_sum += score['pos']

        if count:
            self.final_sentiment_scores = catch(lambda: {"neu": round(neu_sum / count, 3), "neg": round(
                neg_sum / count, 3), "pos": round(pos_sum / count, 3), "compound": round(compound_sum / count, 3)})
