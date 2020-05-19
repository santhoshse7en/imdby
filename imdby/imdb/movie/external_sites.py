from imdb_py.config import base_uri, imdb_uris, tag_search
from imdb_py.helper_function import catch, catch_list, catch_dict, dataframe_data, unicode, external_site
from imdb_py.utils import BeautifulSoup, get, pd, re


# Retrieves External Sites Details
class external_sites:

    """
    Collects External Sites details of the multi-media content in IMDb when title_id is given.
    :param title_id: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, title_id):
        self.title_id = title_id
        self.external_sites_url = imdb_uris["externalsites"] % self.title_id
        soup = BeautifulSoup(get(self.external_sites_url).text, 'lxml')

        """
        :returns: Movie Title
        """
        movie_tag = soup.select_one('h3[itemprop="name"]')
        self.title = catch(lambda: unicode(movie_tag.a.get_text()))
        self.title_url = catch(lambda: unicode(
            '%s%s' % (base_uri, movie_tag.a['href'][1:])))
        self.year = catch(lambda: int(re.findall(
            r"\d+", unicode(movie_tag.select_one('.nobr').get_text()))[0]))

        """
        returns: Official Sites DataFrame if available.
        """
        self.official_sites_df = catch(
            lambda: external_site(tag_search['official'], soup))
        self.official_sites_names = catch_list(
            lambda: self.official_sites_df.Name.tolist())
        self.official_sites_urls = catch_list(
            lambda: self.official_sites_df.URI.tolist())

        """
        returns: Miscellaneous Sites DataFrame if available.
        """
        self.miscellaneous_sites_df = catch(
            lambda: external_site(tag_search['miscellaneous'], soup))
        self.miscellaneous_sites_names = catch_list(
            lambda: self.miscellaneous_sites_df.Name.tolist())
        self.miscellaneous_sites_urls = catch_list(
            lambda: self.miscellaneous_sites_df.URI.tolist())

        """
        returns: Photographs Sites DataFrame if available.
        """
        self.photographs_sites_df = catch(
            lambda: external_site(tag_search['photo'], soup))
        self.photographs_sites_names = catch_list(
            lambda: self.photographs_sites_df.Name.tolist())
        self.photographs_sites_urls = catch_list(
            lambda: self.photographs_sites_df.URI.tolist())

        """
        returns: Videos Clips and Trailers Sites DataFrame if available.
        """
        self.videos_clips_and_trailers_sites_df = catch(
            lambda: external_site(tag_search['videos'], soup))
        self.videos_clips_and_trailers_sites_names = catch_list(
            lambda: self.videos_clips_and_trailers_sites_df.Name.tolist())
        self.videos_clips_and_trailers_sites_urls = catch_list(
            lambda: self.videos_clips_and_trailers_sites_df.URI.tolist())

        """
        :returns: Creates Meta Data from the above info. if available.
        """
        self.imdb_external_sites_metadata = catch_dict(lambda: {"Movie Title": self.title,
                                                                "Movie URL": self.external_sites_url,
                                                                "Title ID": self.title_id,
                                                                "Year": self.year,
                                                                "Official Sites": {"Name": self.official_sites_names,
                                                                                   "URL": self.official_sites_urls},
                                                                "Miscellaneous Sites": {"Name": self.miscellaneous_sites_names,
                                                                                        "URL": self.miscellaneous_sites_urls},
                                                                "Photographs": {"Name": self.photographs_sites_names,
                                                                                "URL": self.photographs_sites_urls},
                                                                "Video Clips and Trailers": {"Name": self.videos_clips_and_trailers_sites_names,
                                                                                             "URL": self.videos_clips_and_trailers_sites_urls}})
