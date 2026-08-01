from imdb.parser.search_id_base import BaseSearchID


class search_company_id(BaseSearchID):
    """
    'IMDbID' method takes a company name, searches for the similar company names available in IMDb.
    and suggests the company name to the user. Based upon user's selection it returns a list of company ids.

    Input serial numbers separated with spaces.
    -------------------- -------------------- -------------------- -------------------- --------------------
    :param text: company name.
    :returns: A list of company ids.
    :raises ValueError: Raises an exception when entered a charater other than a number for selection.
    :raises IndexError: Raises an BeautifulSoup exception when index is out of range.
    """

    def __init__(self, text: str):
        super().__init__('company', text)
        self.company_name, self.company_id = self.name, self.id
