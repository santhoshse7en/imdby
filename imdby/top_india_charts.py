from imdby.utils import *

# Retrieves IMDb Top India Charts Details
class top_india_charts:

    """
    Collects top india charts details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self):
        base_url = "https://www.imdb.com/india/"

        self.top_rated_indian_movies_url = base_url + "top-rated-indian-movies"
        self.top_rated_tamil_movies_url = base_url + "top-rated-tamil-movies"
        self.top_rated_telugu_movies_url = base_url + "top-rated-telugu-movies"
        self.top_rated_malayalam_movies_url = base_url + "top-rated-malayalam-movies"

        indian_soup = BeautifulSoup(get(self.top_rated_indian_movies_url).text, 'lxml')
        tamil_soup = BeautifulSoup(get(self.top_rated_tamil_movies_url).text, 'lxml')
        telugu_soup = BeautifulSoup(get(self.top_rated_telugu_movies_url).text, 'lxml')
        malayalam_soup = BeautifulSoup(get(self.top_rated_malayalam_movies_url).text, 'lxml')

        """
        :returns: top_rated_indian_movies DataFrame
        """
        try:
            top_250 = indian_soup.select_one('.lister-list').select('tr')
            ranks, names, ids, directors, main_cast, years, ratings, rating_stats, posters = [], [], [], [], [], [], [], [], []

            for i in range(len(top_250)):
                title = top_250[i].select_one('.titleColumn')
                poster = top_250[i].select_one('.posterColumn')
                rating = top_250[i].select_one('.ratingColumn')

                try:
                    ranks.append(' '.join(title.contents[0].split()).replace('.',''))
                except:
                    ranks.append(None)

                try:
                    names.append(title.a.text)
                except:
                    names.append(None)

                try:
                    ids.append(poster.a['href'][7:16])
                except:
                    ids.append(None)

                try:
                    directors.append([item.replace(' (dir.)', '').strip() for item in title.a['title'].split(',') if ' (dir.)' in item])
                except:
                    directors.append(None)

                try:
                    main_cast.append([item.strip() for item in title.a['title'].split(',') if ' (dir.)' not in item])
                except:
                    main_cast.append(None)

                try:
                    years.append(re.findall("\d+", title.select_one('.secondaryInfo').text)[0])
                except:
                    years.append(None)

                try:
                    ratings.append(rating.strong.text)
                except:
                    ratings.append(None)

                try:
                    rating_stats.append(rating.strong['title'])
                except:
                    rating_stats.append(None)

                try:
                    posters.append(poster.a.img['src'])
                except:
                    posters.append(None)

            self.top_rated_indian_movies_df = pd.DataFrame({'Rank' : ranks, 'Name' : names, 'ID' : ids,
                                                            'Director' : directors, 'Main Cast' : main_cast,
                                                            'Year' : years, 'Rating' : ratings, 'Rating_Stats' : rating_stats,
                                                            'Poster' : posters})
        except:
            self.top_rated_indian_movies_df = None


        """
        :returns: top_rated_tamil_movies DataFrame
        """
        try:
            top_250 = tamil_soup.select_one('.lister-list').select('tr')
            ranks, names, ids, directors, main_cast, years, ratings, rating_stats, posters = [], [], [], [], [], [], [], [], []

            for i in range(len(top_250)):
                title = top_250[i].select_one('.titleColumn')
                poster = top_250[i].select_one('.posterColumn')
                rating = top_250[i].select_one('.ratingColumn')

                try:
                    ranks.append(' '.join(title.contents[0].split()).replace('.',''))
                except:
                    ranks.append(None)

                try:
                    names.append(title.a.text)
                except:
                    names.append(None)

                try:
                    ids.append(poster.a['href'][7:16])
                except:
                    ids.append(None)

                try:
                    directors.append([item.replace(' (dir.)', '').strip() for item in title.a['title'].split(',') if ' (dir.)' in item])
                except:
                    directors.append(None)

                try:
                    main_cast.append([item.strip() for item in title.a['title'].split(',') if ' (dir.)' not in item])
                except:
                    main_cast.append(None)

                try:
                    years.append(re.findall("\d+", title.select_one('.secondaryInfo').text)[0])
                except:
                    years.append(None)

                try:
                    ratings.append(rating.strong.text)
                except:
                    ratings.append(None)

                try:
                    rating_stats.append(rating.strong['title'])
                except:
                    rating_stats.append(None)

                try:
                    posters.append(poster.a.img['src'])
                except:
                    posters.append(None)

            self.top_rated_tamil_movies_df = pd.DataFrame({'Rank' : ranks, 'Name' : names, 'ID' : ids,
                                                           'Director' : directors, 'Main Cast' : main_cast,
                                                           'Year' : years, 'Rating' : ratings, 'Rating_Stats' : rating_stats,
                                                           'Poster' : posters})
        except:
            self.top_rated_tamil_movies_df = None

        """
        :returns: top_rated_telugu_movies DataFrame
        """
        try:
            top_250 = telugu_soup.select_one('.lister-list').select('tr')
            ranks, names, ids, directors, main_cast, years, ratings, rating_stats, posters = [], [], [], [], [], [], [], [], []

            for i in range(len(top_250)):
                title = top_250[i].select_one('.titleColumn')
                poster = top_250[i].select_one('.posterColumn')
                rating = top_250[i].select_one('.ratingColumn')

                try:
                    ranks.append(' '.join(title.contents[0].split()).replace('.',''))
                except:
                    ranks.append(None)

                try:
                    names.append(title.a.text)
                except:
                    names.append(None)

                try:
                    ids.append(poster.a['href'][7:16])
                except:
                    ids.append(None)

                try:
                    directors.append([item.replace(' (dir.)', '').strip() for item in title.a['title'].split(',') if ' (dir.)' in item])
                except:
                    directors.append(None)

                try:
                    main_cast.append([item.strip() for item in title.a['title'].split(',') if ' (dir.)' not in item])
                except:
                    main_cast.append(None)

                try:
                    years.append(re.findall("\d+", title.select_one('.secondaryInfo').text)[0])
                except:
                    years.append(None)

                try:
                    ratings.append(rating.strong.text)
                except:
                    ratings.append(None)

                try:
                    rating_stats.append(rating.strong['title'])
                except:
                    rating_stats.append(None)

                try:
                    posters.append(poster.a.img['src'])
                except:
                    posters.append(None)

            self.top_rated_telugu_movies_df = pd.DataFrame({'Rank' : ranks, 'Name' : names, 'ID' : ids,
                                                            'Director' : directors, 'Main Cast' : main_cast,
                                                            'Year' : years, 'Rating' : ratings, 'Rating_Stats' : rating_stats,
                                                            'Poster' : posters})
        except:
            self.top_rated_telugu_movies_df = None

        """
        :returns: top_rated_malayalam_movies DataFrame
        """
        try:
            top_250 = malayalam_soup.select_one('.lister-list').select('tr')
            ranks, names, ids, directors, main_cast, years, ratings, rating_stats, posters = [], [], [], [], [], [], [], [], []

            for i in range(len(top_250)):
                title = top_250[i].select_one('.titleColumn')
                poster = top_250[i].select_one('.posterColumn')
                rating = top_250[i].select_one('.ratingColumn')

                try:
                    ranks.append(' '.join(title.contents[0].split()).replace('.',''))
                except:
                    ranks.append(None)

                try:
                    names.append(title.a.text)
                except:
                    names.append(None)

                try:
                    ids.append(poster.a['href'][7:16])
                except:
                    ids.append(None)

                try:
                    directors.append([item.replace(' (dir.)', '').strip() for item in title.a['title'].split(',') if ' (dir.)' in item])
                except:
                    directors.append(None)

                try:
                    main_cast.append([item.strip() for item in title.a['title'].split(',') if ' (dir.)' not in item])
                except:
                    main_cast.append(None)

                try:
                    years.append(re.findall("\d+", title.select_one('.secondaryInfo').text)[0])
                except:
                    years.append(None)

                try:
                    ratings.append(rating.strong.text)
                except:
                    ratings.append(None)

                try:
                    rating_stats.append(rating.strong['title'])
                except:
                    rating_stats.append(None)

                try:
                    posters.append(poster.a.img['src'])
                except:
                    posters.append(None)

            self.top_rated_malayalam_movies_df = pd.DataFrame({'Rank' : ranks, 'Name' : names, 'ID' : ids,
                                                               'Director' : directors, 'Main Cast' : main_cast,
                                                               'Year' : years, 'Rating' : ratings, 'Rating_Stats' : rating_stats,
                                                               'Poster' : posters})
        except:
            self.top_rated_malayalam_movies_df = None

        sys.stdout.write('\r' + str("Top India Charts Extraction Completed") +  '\r')
        sys.stdout.flush()

# main class which passes the titleid to indiviual class
class imdb:
    def __init__(self):
        start_time = datetime.now()
        top_india_charts.__init__(self)

        time_delta = datetime.now() - start_time
        sys.stdout.write('\r' + str("Calculating time taken for Top India Charts extraction") + ":  " + str(time_delta.seconds) +  "  seconds" +  '\r')
        sys.stdout.flush()
