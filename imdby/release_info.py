from imdby.utils import *


# Retrieves IMDb Release Info
class release_info:

    """
    Collects Release Info details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, titleid):
        self.titleid = titleid
        self.release_info_url = "https://www.imdb.com/title/%s/releaseinfo" % self.titleid 
        soup = BeautifulSoup(get(self.release_info_url).text, 'lxml')

        """
        returns: Movie Title
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        """
        returns: Release Info DataFrame if available.
        """
        releases_index = [i for i in range(len(soup.select('h4'))) if 'release' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
        releases = soup.select('h4')[releases_index].findNext('table').select('tr')
        country, date, location = [], [], []
        try:
            for i in range(len(releases)):
                try:
                    country.append(releases[i].select_one('td.release-date-item__country-name').a.text.strip())
                except:
                    country.append(None)

                try:
                    date.append(releases[i].select_one('td.release-date-item__date').text.strip())
                except:
                    date.append(None)

                try:
                    location.append(releases[i].select_one('td.release-date-item__attributes').text.strip())
                except:
                    location.append(None)

                self.releases_df = pd.DataFrame({'Country' : country, 'Date' : date, 'Location' : location})
        except:
            self.releases_df = None

        """
        :returns: Released Countries list if available.
        """
        try:
            self.released_country_names = self.releases_df.Country.tolist()
        except:
            self.released_country_names = None

        """
        :returns: Released Dates list if available.
        """
        try:
            self.released_dates = self.releases_df.Date.tolist()
        except:
            self.released_dates = None

        """
        :returns: Released Location list if available.
        """
        try:
            self.released_locations = self.releases_df.Location.tolist()
        except:
            self.released_locations = None

        """
        :returns: Released Date in India if available.
        """
        try:
            releases_index = [i for i in range(len(soup.select('h4'))) if 'release' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            releases = soup.select('h4')[releases_index].findNext('table').select('tr')
            india_index = [i for i in range(len(releases)) if 'india' in  releases[i].select_one('td').a.text.strip().lower()][0]
            self.release_date_in_india = releases[india_index].select_one('td').findNext('td').text.strip()
        except:
            self.release_date_in_india = None

        """
        returns: Also Known As DataFrame if available.
        """
        aka_index = [i for i in range(len(soup.select('h4'))) if 'also known as' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
        aka = soup.select('h4')[aka_index].findNext('table').select('tr')
        self.also_known_as_df = pd.DataFrame(columns=['Country', 'Title'])
        try:
            for i in range(len(aka)):
                try:
                    self.also_known_as_df.loc[len(self.also_known_as_df)] = [aka[i].select_one('td.aka-item__name').text.strip(),
                                                                             aka[i].select_one('td.aka-item__title').text.strip()]
                except:
                    pass
        except:
            self.also_known_as_df = None

        """
        :returns: Also Known As Countries list if available.
        """
        try:
            self.also_known_as_country_names = self.also_known_as_df.Country.tolist()
        except:
            self.also_known_as_country_names = None

        """
        :returns: Also Known As Title list if available.
        """
        try:
            self.also_known_as_titles = self.also_known_as_df.Title.tolist()
        except:
            self.also_known_as_titles = None

        """
        :returns: Creates Meta Data from the above info. if available.
        """
        try:
            self.imdb_release_info_metadata = {"Movie Title" : self.title,
                                               "Title ID" : self.titleid,
                                               "Movie Release Info URL" : self.release_info_url,
                                               "India Release Date" : self.release_date_in_india,
                                               "Release Dates" : {"Country" : self.released_country_names,
                                                                  "Date" : self.released_dates,
                                                                  "Location" : self.released_locations},
                                               "Also Known As (AKA)" : {"Country" : self.also_known_as_country_names,
                                                                        "Title" : self.also_known_as_titles}}
        except:
            self.imdb_release_info_metadata = None

        print("\rRelease Info Extraction Completed\r", end="\r", flush=True)
