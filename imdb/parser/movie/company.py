from imdb.utils.config import base_uri, imdb_uris, tag_search
from imdb.utils.helpers import catch, company_data, dataframe_data, unicode
from imdb.utils.utils import BeautifulSoup, get, pd, re


# Retrieves IMDb Company Credits Details
class company:

    """
    Collects Company Credits details of the multi-media content in IMDb when title_id is given.
    :param title_id: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, title_id):
        self.title_id = title_id
        self.company_uri = imdb_uris["companycredits"] % self.title_id
        soup = BeautifulSoup(get(self.company_uri).text, 'lxml')

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
        :returns: Production Company Credits DataFrame
        """
        self.production_company_df = catch(
            'None', lambda: company_data(tag_search['production'], soup))
        self.production_company_name = catch(
            'list', lambda: self.production_company_df.Name.tolist())
        self.production_company_id = catch(
            'list', lambda: self.production_company_df.ID.tolist())
        self.production_company_uri = catch(
            'list', lambda: self.production_company_df.URI.tolist())

        """
        :returns: Distributors DataFrame
        """
        self.distributors_df = catch(
            'None', lambda: company_data(tag_search['distributor'], soup))
        self.distributors_name = catch(
            'list', lambda: self.distributors_df.Name.tolist())
        self.distributors_id = catch(
            'list', lambda: self.distributors_df.ID.tolist())
        self.distributors_uri = catch(
            'list', lambda: self.distributors_df.URI.tolist())

        """
        :returns: Special Effects DataFrame
        """
        self.specials_effects_df = catch(
            'None', lambda: company_data(tag_search['special_effects'], soup))
        self.specials_effects_name = catch(
            'list', lambda: self.specials_effects_df.Name.tolist())
        self.specials_effects_id = catch(
            'list', lambda: self.specials_effects_df.ID.tolist())
        self.specials_effects_uri = catch(
            'list', lambda: self.specials_effects_df.URI.tolist())

        """
        :returns: Other Companies DataFrame
        """
        self.other_companies_df = catch(
            'None', lambda: company_data(tag_search['other'], soup))
        self.other_companies_name = catch(
            'list', lambda: self.other_companies_df.Name.tolist())
        self.other_companies_id = catch(
            'list', lambda: self.other_companies_df.ID.tolist())
        self.other_companies_uri = catch(
            'list', lambda: self.other_companies_df.URI.tolist())

        """
        returns: Creates Dict from the above info. if available.
        """
        self.imdb_company_metadata = catch('dict', lambda: {"Movie Name": self.title,
                                                            "Movie URI": self.title_url,
                                                            "Title ID": self.title_id,
                                                            "Year": self.year,
                                                            "Movie Company URL": self.company_uri,
                                                            "Distributors": {"Name": self.distributors_name,
                                                                             "ID": self.distributors_id,
                                                                             "URI": self.distributors_uri},
                                                            "Other Companies": {"Name": self.other_companies_name,
                                                                                "ID": self.other_companies_id,
                                                                                "URI": self.other_companies_uri},
                                                            "Production Company": {"Name": self.production_company_name,
                                                                                   "ID": self.production_company_id,
                                                                                   "URI": self.production_company_uri},
                                                            "Special Effects": {"Name": self.specials_effects_name,
                                                                                "ID": self.specials_effects_id,
                                                                                "URI": self.specials_effects_uri}})
