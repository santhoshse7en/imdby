from imdb.utils.config import base_uri, imdb_uris
from imdb.utils.helpers import (catch, dataframe_data, index_finder,
                                india_index_finder, unicode)
from imdb.utils.utils import BeautifulSoup, get, pd, re


# Retrieves IMDb Release Info
class release_info:

    """
    Collects Release Info details of the multi-media content in IMDb when title_id is given.
    :param title_id: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, title_id):
        self.title_id = title_id
        self.release_info_url = imdb_uris["releaseinfo"] % self.title_id
        soup = BeautifulSoup(get(self.release_info_url).text, 'lxml')

        """
        :returns: table tag index
        """
        table_tag = catch('None', lambda: soup.select('h4'))

        """
        :returns: Movie Title
        """
        movie_tag = catch(
            'None', lambda: soup.select_one('h3[itemprop="name"]'))
        self.title = catch('None', lambda: unicode(movie_tag.a.get_text()))
        self.title_url = catch('None', lambda: unicode(
            '%s%s' % (base_uri, movie_tag.a['href'][1:])))
        self.year = catch('None', lambda: int(re.findall(
            r"\d+", unicode(movie_tag.select_one('.nobr').get_text()))[0]))

        """
        returns: tags
        """
        releases = catch('None', lambda: table_tag[index_finder(
            table_tag, 'release')].findNext('table').select('tr'))

        """
        returns: Release Info DataFrame if available.
        """
        try:
            self.releases_df = pd.DataFrame(
                columns=['Country', 'URI', 'Date', 'Location'])

            for tag in releases:
                self.releases_df.loc[len(self.releases_df)] = [catch('None', lambda: unicode(tag.select_one('td.release-date-item__country-name').a.get_text())),
                                                               catch('None', lambda: "%s%s" % (base_uri, unicode(tag.select_one(
                                                                   'td.release-date-item__country-name').a['href'][1:]))),
                                                               catch('None', lambda: unicode(tag.select_one(
                                                                   'td.release-date-item__date').get_text())),
                                                               catch('None', lambda: unicode(tag.select_one('td.release-date-item__attributes').get_text()))]

            self.releases_df = dataframe_data(self.releases_df)

        except:
            self.releases_df = None

        """
        :returns: Released Countries, Dates, Location list if available.
        """
        self.released_country_names = catch(
            'list', lambda: self.releases_df.Country.tolist())
        self.released_country_uri = catch(
            'list', lambda: self.releases_df.URI.tolist())
        self.released_dates = catch(
            'list', lambda: self.releases_df.Date.tolist())
        self.released_locations = catch(
            'list', lambda: self.releases_df.Location.tolist())

        """
        :returns: Released Date in India if available.
        """
        self.release_date_in_india = catch('None', lambda: unicode(releases[india_index_finder(
            releases, 'india')].select_one('td').findNext('td').get_text()))

        """
        returns: Also Known As DataFrame if available.
        """
        try:
            aka = table_tag[index_finder(table_tag, 'also known as')].findNext(
                'table').select('tr')
            self.also_known_as_df = pd.DataFrame(columns=['Country', 'Title'])

            for tag in aka:
                self.also_known_as_df.loc[len(self.also_known_as_df)] = [catch('None', lambda: unicode(tag.select_one('td.aka-item__name').get_text())),
                                                                         catch('None', lambda: unicode(tag.select_one('td.aka-item__title').get_text()))]

            self.also_known_as_df = dataframe_data(self.also_known_as_df)
        except:
            self.also_known_as_df = None

        """
        :returns: Also Known As Countries, Title list if available.
        """
        self.also_known_as_country_names = catch(
            'list', lambda: self.also_known_as_df.Country.tolist())
        self.also_known_as_titles = catch(
            'list', lambda: self.also_known_as_df.Title.tolist())

        """
        :returns: Creates Meta Data from the above info. if available.
        """
        self.imdb_release_info_metadata = catch('dict', lambda: {"Movie Name": self.title,
                                                                 "Movie URI": self.title_url,
                                                                 "Title ID": self.title_id,
                                                                 "Year": self.year,
                                                                 "Movie Release Info URL": self.release_info_url,
                                                                 "India Release Date": self.release_date_in_india,
                                                                 "Release Dates": {"Country": self.released_country_names,
                                                                                   "URI": self.released_country_uri,
                                                                                   "Date": self.released_dates,
                                                                                   "Location": self.released_locations},
                                                                 "Also Known As (AKA)": {"Country": self.also_known_as_country_names,
                                                                                         "Title": self.also_known_as_titles}})
