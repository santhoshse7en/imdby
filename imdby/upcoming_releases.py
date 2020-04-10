from imdby.utils import *


class upcoming_releases:
    """
    'Upcoming Releases' method shows the available region in IMDb and suggests the regions to the user.
    Based upon user's selection it returns a upcoming_releases DataFrame.

    Input serial numbers separated with spaces.
    -------------------- -------------------- -------------------- -------------------- --------------------
    :returns: Upcoming Releases in selected regions.
    :raises ValueError: Raises an exception when entered a charater other than a number for selection.
    :raises IndexError: Raises an BeautifulSoup exception when index is out of range.
    """

    def __init__(self):

        """
        returns: Country Name & Country Code
        """
        url = 'https://www.imdb.com/calendar/'
        soup = BeautifulSoup(get(url).text, 'lxml')

        countries, country_code,  = [], []
        country = soup.select_one('#sidebar').select('a')

        try:
            for item in country:
                print('%s' %(country.index(item) + 1) + ': ' + item.text.strip())
                countries.append(item.text)
                country_code.append(item['href'][17:19].lower())

            input_name = re.findall(r"[\w']+", input('Enter serial number\t'))
            countries = [countries[int(load) - 1] if int(load) != 0 else '' for load in input_name]
            country_code = [country_code[int(load) - 1] if int(load) != 0 else '' for load in input_name]

            if len(country_code) == 1:
                self.country_name = countries[0]
                self.country_code = country_code[0]
            else:
                self.country_name = countries
                self.country_code = country_code

        except Exception as es:
            print("{0} :".format(type(es)), es)
            sys.exit(0)

        """
        returns: Upcoming Release for selected regions
        """
        self.region_url = 'https://www.imdb.com/calendar/?region=%s' % self.country_code
        region_soup = BeautifulSoup(get(self.region_url).text, 'lxml')

        release_dates = region_soup.select_one('#pagecontent').select('h4')
        movie_name, title_id, release_date, year = [None] * 4
        self.upcoming_releases_df = pd.DataFrame(columns=['Release Date', 'Movie Title' , 'ID' , 'Years' ])

        for item in release_dates:

            try:
                movies = item.findNext('ul').select('a')
                years = item.findNext('ul').select('li')
                
                for i in zip(movies, years):
                    release_date = item.text
                    movie_name = i[0].text.strip()
                    title_id = i[0]['href'][7:16]
                    year = re.findall("\d+", i[1].contents[2].strip())[0]
                    self.upcoming_releases_df.loc[len(self.upcoming_releases_df)] = [release_date, movie_name, title_id, year]

            except Exception as es:
                print("No! release data found on selected region"+"{0} :".format(type(es)), es)
                sys.exit(0)

        print("\rUpcoming Releases Extraction Completed\r", end="\r", flush=True)

# main class which passes the titleid to indiviual class
class imdb:
    def __init__(self):
        start_time = datetime.now()
        upcoming_releases.__init__(self)

        time_delta = datetime.now() - start_time
        print("\rCalculating time taken for upcoming releases extraction : %s  seconds" % (time_delta.seconds), end="\r", flush=True)
