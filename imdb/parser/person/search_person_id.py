from imdb.parser.search_id_base import BaseSearchID


class search_person_id(BaseSearchID):
    """
    'IMDbID' method takes a person name, searches for the similar person names available in IMDb.
    and suggests the person name to the user. Based upon user's selection it returns a list of person ids.

    Input serial numbers separated with spaces.
    -------------------- -------------------- -------------------- -------------------- --------------------
    :param text: person name.
    :returns: A list of person ids.
    :raises ValueError: Raises an exception when entered a charater other than a number for selection.
    :raises IndexError: Raises an BeautifulSoup exception when index is out of range.
    """

    def __init__(self, text: str):
        super().__init__('person', text)
        self.person_id = self.id
