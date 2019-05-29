from imdby.utils import *

# Retrieves IMDb Trending Now in India Details
class trending_now_in_india:

    """
    Collects trending_now_in_india details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self):
        base_url = "https://www.imdb.com/india/"

        self.upcoming_movies_url =  base_url + "upcoming"
        self.popular_tamil_url = base_url + "tamil"
        self.popular_telugu_url = base_url + "telugu"
        self.popular_india_url = base_url + "released"
        self.popular_global_url = base_url + "global"
        self.popular_hindi_url = base_url + "hindi"

        upcoming_soup = BeautifulSoup(get(self.upcoming_movies_url).text, 'lxml')
        popular_tamil_soup = BeautifulSoup(get(self.popular_tamil_url).text, 'lxml')
        popular_telugu_soup = BeautifulSoup(get(self.popular_telugu_url).text, 'lxml')
        popular_india_soup = BeautifulSoup(get(self.popular_india_url).text, 'lxml')
        popular_global_soup = BeautifulSoup(get(self.popular_global_url).text, 'lxml')
        popular_global_soup = BeautifulSoup(get(self.popular_hindi_url).text, 'lxml')

        """
        :returns: Upcoming DataFrame
        """
        try:
            upcoming_movies = upcoming_soup.select_one('#trending-container').select('.trending-list-rank-item-data-container')
            self.upcoming_movies_df = pd.DataFrame(columns=['Rank', 'Name', 'ID', '% OF TOP 10 PAGE VIEWS'])

            for i in range(len(upcoming_movies)):
                try:
                    self.upcoming_movies_df.loc[len(self.upcoming_movies_df)] = [upcoming_movies[i].select_one('.trending-list-rank-item-rank-position').text,
                                                                                 upcoming_movies[i].select_one('.trending-list-rank-item-name').text,
                                                                                 upcoming_movies[i].select_one('.trending-list-rank-item-name').a['href'][7:16],
                                                                                 upcoming_movies[i].select_one('.trending-list-rank-item-share').text]
                except:
                    pass
        except:
            self.upcoming_movies_df = None

        """
        :returns: popular_tamil_movies DataFrame
        """
        try:
            popular_tamil_movies = popular_tamil_soup.select_one('#trending-container').select('.trending-list-rank-item-data-container')
            self.popular_tamil_movies_df = pd.DataFrame(columns=['S.No.', 'Name', 'ID', 'Share'])

            for i in range(len(popular_tamil_movies)):
                try:
                    self.popular_tamil_movies_df.loc[len(self.popular_tamil_movies_df)] = [popular_tamil_movies[i].select_one('.trending-list-rank-item-rank-position').text,
                                                                                           popular_tamil_movies[i].select_one('.trending-list-rank-item-name').text,
                                                                                           popular_tamil_movies[i].select_one('.trending-list-rank-item-name').a['href'][7:16],
                                                                                           popular_tamil_movies[i].select_one('.trending-list-rank-item-share').text]
                except:
                    pass
        except:
            self.popular_tamil_movies_df = None

        """
        :returns: popular_telugu_movies DataFrame
        """
        try:
            popular_telugu_movies = popular_telugu_soup.select_one('#trending-container').select('.trending-list-rank-item-data-container')
            self.popular_telugu_movies_df = pd.DataFrame(columns=['S.No.', 'Name', 'ID', 'Share'])

            for i in range(len(popular_telugu_movies)):
                try:
                    self.popular_telugu_movies_df.loc[len(self.popular_telugu_movies_df)] = [popular_telugu_movies[i].select_one('.trending-list-rank-item-rank-position').text,
                                                                                             popular_telugu_movies[i].select_one('.trending-list-rank-item-name').text,
                                                                                             popular_telugu_movies[i].select_one('.trending-list-rank-item-name').a['href'][7:16],
                                                                                             popular_telugu_movies[i].select_one('.trending-list-rank-item-share').text]
                except:
                    pass
        except:
            self.popular_telugu_movies_df = None

        """
        :returns: Popular India DataFrame
        """
        try:
            popular_india_movies = popular_india_soup.select_one('#trending-container').select('.trending-list-rank-item-data-container')
            self.popular_india_movies_df = pd.DataFrame(columns=['Rank', 'Name', 'ID', '% OF TOP 10 PAGE VIEWS'])

            for i in range(len(popular_india_movies)):
                try:
                    self.popular_india_movies_df.loc[len(self.popular_india_movies_df)] = [popular_india_movies[i].select_one('.trending-list-rank-item-rank-position').text,
                                                                                           popular_india_movies[i].select_one('.trending-list-rank-item-name').text,
                                                                                           popular_india_movies[i].select_one('.trending-list-rank-item-name').a['href'][7:16],
                                                                                           popular_india_movies[i].select_one('.trending-list-rank-item-share').text]
                except:
                    pass
        except:
            self.popular_india_movies_df = None

        """
        :returns: Poppular Global DataFrame
        """
        try:
            popular_global_movies = popular_global_soup.select_one('#trending-container').select('.trending-list-rank-item-data-container')
            self.popular_global_movies_df = pd.DataFrame(columns=['Rank', 'Name', 'ID', '% OF TOP 10 PAGE VIEWS'])

            for i in range(len(popular_global_movies)):
                try:
                    self.popular_global_movies_df.loc[len(self.popular_global_movies_df)] = [popular_global_movies[i].select_one('.trending-list-rank-item-rank-position').text,
                                                                                             popular_global_movies[i].select_one('.trending-list-rank-item-name').text,
                                                                                             popular_global_movies[i].select_one('.trending-list-rank-item-name').a['href'][7:16],
                                                                                             popular_global_movies[i].select_one('.trending-list-rank-item-share').text]
                except:
                    pass
        except:
            self.popular_global_movies_df = None

        """
        :returns: Poppular Hindi DataFrame
        """
        try:
            popular_hindi_movies = popular_global_soup.select_one('#trending-container').select('.trending-list-rank-item-data-container')
            self.popular_hindi_movies_df = pd.DataFrame(columns=['Rank', 'Name', 'ID', '% OF TOP 10 PAGE VIEWS'])

            for i in range(len(popular_hindi_movies)):
                try:
                    self.popular_hindi_movies_df.loc[len(self.popular_hindi_movies_df)] = [popular_hindi_movies[i].select_one('.trending-list-rank-item-rank-position').text,
                                                                                           popular_hindi_movies[i].select_one('.trending-list-rank-item-name').text,
                                                                                           popular_hindi_movies[i].select_one('.trending-list-rank-item-name').a['href'][7:16],
                                                                                           popular_hindi_movies[i].select_one('.trending-list-rank-item-share').text]
                except:
                    pass
        except:
            self.popular_hindi_movies_df = None

        sys.stdout.write('\r' + str("Trending Now in India Extraction Completed") +  '\r')
        sys.stdout.flush()

# main class which passes the titleid to indiviual class
class imdb:
    def __init__(self):
        start_time = datetime.now()
        trending_now_in_india.__init__(self)

        time_delta = datetime.now() - start_time
        sys.stdout.write('\r' + str("Calculating time taken for Trending Now in India extraction") + ":  " + str(time_delta.seconds) +  "  seconds" +  '\r')
        sys.stdout.flush()
