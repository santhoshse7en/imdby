from imdby.utils import *


# Retrieves IMDb Company Credits Details
class company:

    """
    Collects Company Credits details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """
    def __init__(self, titleid):
        self.titleid = titleid
        self.company_url = "https://www.imdb.com/title/%s/companycredits" % self.titleid 
        soup = BeautifulSoup(get(self.company_url).text, 'lxml')

        """
        :returns: Movie Title
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        """
        :returns: Production Company Credits DataFrame
        """
        try:
            production_company = soup.select_one('#production').findNext('ul').select('li')
            self.production_company_df = pd.DataFrame(columns=['Name', 'ID'])

            for i in range(len(production_company)):
                try:
                    self.production_company_df.loc[len(self.production_company_df)] = [production_company[i].a.text.strip(),
                                                                                       production_company[i].a['href'][9:].strip()]
                except:
                    pass
        except:
            self.production_company_df = None

        """
        :returns: Production Company Credits Name if available.
        """
        try:
            self.production_company_name = self.production_company_df.Name.tolist()
        except:
            self.production_company_name = None

        """
        :returns: Production Company Credits ID if available.
        """
        try:
            self.production_company_id = self.production_company_df.ID.tolist()
        except:
            self.production_company_id = None
        """
        :returns: Distributors DataFrame
        """
        try:
            distributors = soup.select_one('#distributors').findNext('ul').select('li')
            self.distributors_df = pd.DataFrame(columns=['Name', 'ID'])

            for i in range(len(distributors)):
                try:
                    self.distributors_df.loc[len(self.distributors_df)] = [distributors[i].a.text.strip(),
                                                                           distributors[i].a['href'][9:].strip()]
                except:
                    pass
        except:
            self.distributors_df = None

        """
        :returns: Distributors Name if available.
        """
        try:
            self.distributors_name = self.distributors_df.Name.tolist()
        except:
            self.distributors_name = None

        """
        :returns: Distributors ID if available.
        """
        try:
            self.distributors_id = self.distributors_df.ID.tolist()
        except:
            self.distributors_id = None

        """
        :returns: Special Effects DataFrame
        """
        try:
            special_effects = soup.select_one('#specialEffects').findNext('ul').select('li')
            self.specials_effects_df = pd.DataFrame(columns=['Name', 'ID'])

            for i in range(len(special_effects)):
                try:
                    self.specials_effects_df.loc[len(self.specials_effects_df)] = [special_effects[i].a.text.strip(),
                                                                                   special_effects[i].a['href'][9:].strip()]
                except:
                    pass
        except:
            self.specials_effects_df = None

        """
        :returns: Special Effects Name if available.
        """
        try:
            self.specials_effects_name = self.specials_effects_df.Name.tolist()
        except:
            self.specials_effects_name = None

        """
        :returns: Special Effects ID if available.
        """
        try:
            self.specials_effects_id = self.specials_effects_df.ID.tolist()
        except:
            self.specials_effects_id = None

        """
        :returns: Other Companies DataFrame
        """
        try:
            other_companies = soup.select_one('#other').findNext('ul').select('li')
            self.other_companies_df = pd.DataFrame(columns=['Name', 'ID'])

            for i in range(len(other_companies)):
                try:
                    self.other_companies_df.loc[len(self.other_companies_df)] = [other_companies[i].a.text.strip(),
                                                                                  other_companies[i].a['href'][9:].strip()]
                except:
                    pass
        except:
            self.other_companies_df = None

        """
        :returns: Other Companies Name if available.
        """
        try:
            self.other_companies_name = self.other_companies_df.Name.tolist()
        except:
            self.other_companies_name = None

        """
        :returns: Other Companies ID if available.
        """
        try:
            self.other_companies_id = self.other_companies_df.ID.tolist()
        except:
            self.other_companies_id = None

        """
        returns: Creates Dict from the above info. if available.
        """
        try:
            self.imdb_company_metadata = {"Movie Name" : self.title,
                                                 "Title ID" : self.titleid,
                                                 "Movie Company URL" : self.company_url,
                                                 "Production Company" : {"Name" : self.production_company_name,
                                                                         "ID" : self.production_company_id},
                                                 "Special Effects" : {"Name" : self.specials_effects_name,
                                                                      "ID" : self.specials_effects_id},
                                                 "Distributors" : {"Name" : self.distributors_name,
                                                                   "ID" : self.distributors_id},
                                                 "Other Companies" : {"Name" : self.other_companies_name,
                                                                      "ID" : self.other_companies_id}}
        except:
            self.imdb_company_metadata = None

        print("\rCompany Credits Extraction Completed\r", end="\r", flush=True)
