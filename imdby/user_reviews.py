from imdby.utils import *


# Retrieves IMDb User Reviews
class user_reviews:

    """
    Collects user reviews of the multi media content in IMDb when titleid is given.
    :param user reviews: Unique identification titleid for every multi media content in IMDb.
    :returns: Returns all the user reviews.
    """

    def __init__(self, titleid):
        self.titleid = titleid
        self.user_reviews_url = "https://www.imdb.com/title/" + str(self.titleid) + "/reviews?spoiler=hide&sort=helpfulnessScore&dir=desc&ratingFilter=0"

        # Creating soup for the website
        soup = BeautifulSoup(get(self.user_reviews_url).text, 'lxml')

        """
        :returns: movie title if available.
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        # for collection of number of reviews
        reviews_count = int(''.join(i for i in soup.select_one('div.header').span.text if i.isdigit()))

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
                more_button = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "ipl-load-more__button"))).click()
            else:
                break
            sys.stdout.write('\r' + str(clicks) + ' - ' + 'clicks has made for scrolling out of' + ' - ' + str(maxclicks))
            sys.stdout.flush()
        time.sleep(1)

        soup = BeautifulSoup(browser.page_source, 'lxml')
        browser.quit()

        user_reviews_count = soup.select('.text')
        self.user_reviews_count = len(user_reviews_count)
        sys.stdout.write('\r' + "\n" + str("total user reviews without spoilers are") + " : " + str(len(user_reviews_count)) + '\r')
        sys.stdout.flush()

        analyser = SentimentIntensityAnalyzer()
        neu_sum, neg_sum, compound_sum, pos_sum, count = 0,0,0,0,0

        self.user_reviews = [' '.join(item.text.split()) for item in user_reviews_count]
        sentiment_score = [analyser.polarity_scores(self.user_reviews[i])['compound'] for i in range(len(self.user_reviews))]
        polarity_score = [analyser.polarity_scores(self.user_reviews[i]) for i in range(len(self.user_reviews))]

        sentiment = []
        for item in user_reviews_count:
            analysis = TextBlob(' '.join(item.text.split()))
            # set sentiment
            if analysis.sentiment.polarity > 0:
                sentiment.append('positive')
            elif analysis.sentiment.polarity == 0:
                sentiment.append('neutral')
            else:
                sentiment.append('negative')

        self.user_reviews_df = pd.DataFrame({'Tweets' : self.user_reviews, 'Sentiment' : sentiment, 'Sentiment Score' : sentiment_score, 'Polarity Scorce' : polarity_score})

        for i in range(len(self.user_reviews)):
            count += 1
            score = analyser.polarity_scores(self.user_reviews[i])
            neu_sum += score['neu']
            neg_sum += score['neg']
            pos_sum += score['pos']

        if count:
            self.final_sentiment_scores = {"neu" : round(neu_sum / count, 3), "neg" : round(neg_sum / count, 3), "pos" : round(pos_sum / count, 3), "compound" : round(compound_sum / count, 3)}
        else:
            self.final_sentiment_scores = None

        sys.stdout.write('\r' + str("User Review Extraction Completed") +  '\r')
        sys.stdout.flush()

# main class which passes the titleid to indiviual class
class imdb:
    def __init__(self, titleid):
        start_time = datetime.now()
        user_reviews.__init__(self, titleid)

        time_delta = datetime.now() - start_time
        print("\rCalculating time taken for user review extraction : %s  seconds" % (time_delta.seconds), end="\r", flush=True)
