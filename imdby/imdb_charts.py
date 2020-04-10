from imdby.utils import *


# Retrieves IMDb Charts Details
class imdb_charts:

    """
    Collects top rated movies details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self):
        base_url = "https://www.imdb.com/chart/"

        self.top_rated_movies_url = base_url + "top"
        self.top_rated_english_movies_url = base_url + "top-english-movies"
        self.top_box_office_us_url = base_url + "boxoffice"
        self.most_popular_movies_url = base_url + "moviemeter"
        self.lowest_rated_movies_url = base_url + "bottom"
        self.top_rated_tv_shows_url = base_url + "toptv"
        self.most_popular_tv_shows_url = base_url + "tvmeter"

        top_soup = BeautifulSoup(get(self.top_rated_movies_url).text, 'lxml')
        box_office_soup = BeautifulSoup(get(self.top_box_office_us_url).text, 'lxml')
        most_popular_movies_soup = BeautifulSoup(get(self.most_popular_movies_url).text, 'lxml')
        bottom_soup = BeautifulSoup(get(self.lowest_rated_movies_url).text, 'lxml')
        toptv_soup = BeautifulSoup(get(self.top_rated_tv_shows_url).text, 'lxml')
        most_popular_tv_shows_soup = BeautifulSoup(get(self.most_popular_tv_shows_url).text, 'lxml')
        top_english_soup = BeautifulSoup(get(self.top_rated_english_movies_url).text, 'lxml')

        """
        :returns: top_rated_movies DataFrame
        """
        try:
            top_250 = top_soup.select_one('.lister-list').select('tr')
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

            self.top_rated_movies_df = pd.DataFrame({'Rank' : ranks, 'Name' : names, 'ID' : ids,
                                                     'Director' : directors, 'Main Cast' : main_cast,
                                                     'Year' : years, 'Rating' : ratings, 'Rating_Stats' : rating_stats,
                                                     'Poster' : posters})
        except:
            self.top_rated_movies_df = None

        """
        :returns: top_box_office_us_movies DataFrame
        """
        try:
            top_250 = box_office_soup.select_one('tbody').select('tr')
            names, ids, directors, main_cast, posters, weekend, gross, week = [], [], [], [], [], [], [], []

            for i in range(len(top_250)):
                title = top_250[i].select_one('.titleColumn')
                poster = top_250[i].select_one('.posterColumn')
                rating = top_250[i].select('.ratingColumn')
                weeks = top_250[i].select_one('.weeksColumn')

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
                    weekend.append(' '.join(rating[0].text.split()))
                except:
                    weekend.append(None)

                try:
                    gross.append(' '.join(rating[1].text.split()))
                except:
                    gross.append(None)

                try:
                    week.append(weeks.text)
                except:
                    week.append(None)

                try:
                    posters.append(poster.a.img['src'])
                except:
                    poster.append(None)

            self.top_box_office_df = pd.DataFrame({'Name' : names, 'ID' : ids,
                                                   'Director' : directors, 'Main Cast' : main_cast,
                                                   'Weekend' : weekend, 'Gross' : gross, 'Total Weeks' : week,
                                                   'Poster' : posters})
        except:
            self.top_box_office_df = None

        """
        :returns: top_box_office_us_movies weekend
        """
        try:
            self.top_box_office_weekend = box_office_soup.select_one('#boxoffice').h4.text
        except:
            self.top_box_office_weekend = None

        """
        :returns: most_popular_movies DataFrame
        """
        try:
            top_250 = most_popular_movies_soup.select_one('.lister-list').select('tr')
            ranks, names, ids, directors, main_cast, years, ratings, rating_stats, posters = [], [], [], [], [], [], [], [], []

            for i in range(len(top_250)):
                title = top_250[i].select_one('.titleColumn')
                poster = top_250[i].select_one('.posterColumn')
                rating = top_250[i].select_one('.ratingColumn')

                try:
                    ranks.append(title.select_one('.velocity').text.split()[0])
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

            self.most_popular_movies_df = pd.DataFrame({'Rank' : ranks, 'Name' : names, 'ID' : ids,
                                                        'Director' : directors, 'Main Cast' : main_cast,
                                                        'Year' : years, 'Rating' : ratings, 'Rating_Stats' : rating_stats,
                                                        'Poster' : posters})
        except:
            self.most_popular_movies_df = None

        """
        :returns: lowest_rated_movies DataFrame
        """
        try:
            top_250 = bottom_soup.select_one('.lister-list').select('tr')
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

            self.lowest_rated_movies_df = pd.DataFrame({'Rank' : ranks, 'Name' : names, 'ID' : ids,
                                                        'Director' : directors, 'Main Cast' : main_cast,
                                                        'Year' : years, 'Rating' : ratings, 'Rating_Stats' : rating_stats,
                                                        'Poster' : posters})
        except:
            self.lowest_rated_movies_df = None

        """
        :returns: top_rated_tv_shows DataFrame
        """
        try:
            top_250 = toptv_soup.select_one('.lister-list').select('tr')
            ranks, names, ids, main_cast, years, ratings, rating_stats, posters = [], [], [], [], [], [], [], []

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

            self.top_rated_tv_shows_df = pd.DataFrame({'Rank' : ranks, 'Name' : names, 'ID' : ids, 'Main Cast' : main_cast,
                                                       'Year' : years, 'Rating' : ratings, 'Rating_Stats' : rating_stats,
                                                       'Poster' : posters})
        except:
            self.top_rated_tv_shows_df = None

        """
        :returns: most_popular_tv_shows DataFrame
        """
        try:
            top_250 = most_popular_tv_shows_soup.select_one('.lister-list').select('tr')
            ranks, names, ids, main_cast, years, ratings, rating_stats, posters = [], [], [], [], [], [], [], []

            for i in range(len(top_250)):
                title = top_250[i].select_one('.titleColumn')
                poster = top_250[i].select_one('.posterColumn')
                rating = top_250[i].select_one('.ratingColumn')

                try:
                    ranks.append(title.select_one('.velocity').text.split()[0])
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

            self.most_popular_tv_shows_df = pd.DataFrame({'Rank' : ranks, 'Name' : names, 'ID' : ids, 'Main Cast' : main_cast,
                                                          'Year' : years, 'Rating' : ratings, 'Rating_Stats' : rating_stats,
                                                          'Poster' : posters})
        except:
            self.most_popular_tv_shows_df = None

        """
        :returns: top_rated_english_movies DataFrame
        """
        try:
            top_250 = top_english_soup.select_one('.lister-list').select('tr')
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

            self.top_rated_english_movies_df = pd.DataFrame({'Rank' : ranks, 'Name' : names, 'ID' : ids,
                                                             'Director' : directors, 'Main Cast' : main_cast,
                                                             'Year' : years, 'Rating' : ratings, 'Rating_Stats' : rating_stats,
                                                             'Poster' : posters})
        except:
            self.top_rated_english_movies_df = None

        print("\rIMDb Charts Extraction Completed\r", end="\r", flush=True)

# main class which passes the titleid to indiviual class
class imdb:
    def __init__(self):
        start_time = datetime.now()
        imdb_charts.__init__(self)

        time_delta = datetime.now() - start_time
        print("\r Calculating time taken for IMDb Charts extraction : %s  seconds\r" % (time_delta.seconds), end="\r", flush=True)
