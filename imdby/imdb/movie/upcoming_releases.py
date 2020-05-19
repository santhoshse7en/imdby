from imdby.utils.config import base_uri, imdb_uris
from imdby.utils.helper_function import (catch, dataframe_data, trending_now,
                                     trending_now_df, unicode)
from imdby.utils.utils import BeautifulSoup, get, pd, re, sys


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
        soup = BeautifulSoup(get(imdb_uris['calendar']).text, 'lxml')

        countries, country_code,  = [], []
        country = soup.select_one('#sidebar').select('a')

        try:
            for item in country:
                print('%s : %s' % (country.index(item) + 1, item.text.strip()))
                countries.append(item.text)
                country_code.append(item['href'][17:19].lower())

            input_name = re.findall(r"[\w']+", input('Enter serial number\t'))
            countries = [
                countries[int(load) - 1] if int(load) != 0 else '' for load in input_name]
            country_code = [
                country_code[int(load) - 1] if int(load) != 0 else '' for load in input_name]

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
        self.region_url = imdb_uris['region'] % self.country_code
        region_soup = BeautifulSoup(get(self.region_url).text, 'lxml')

        try:
            release_dates = region_soup.select_one('#pagecontent').select('h4')
            self.upcoming_releases_df = pd.DataFrame(
                columns=['Release Date', 'Movie Title', 'ID', 'URI', 'Year'])

            for item in release_dates:

                movies = item.findNext('ul').select('a')
                years = item.findNext('ul').select('li')

                for i in zip(movies, years):
                    self.upcoming_releases_df.loc[len(self.upcoming_releases_df)] = [catch(lambda: unicode(item.get_text())),
                                                                                     catch(lambda: unicode(i[0].get_text())),
                                                                                     catch(lambda: unicode(i[0]['href'][7:16])),
                                                                                     catch(lambda: "%s%s" % (base_uri, unicode(i[0]['href'][1:]))),
                                                                                     catch(lambda: int(re.findall(r"\d+", unicode(i[1].contents[2]))[-1]))]

            self.upcoming_releases_df = dataframe_data(
                self.upcoming_releases_df)
        except:
            self.upcoming_releases_df = None
