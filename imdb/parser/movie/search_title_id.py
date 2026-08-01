from imdb.parser.search_id_base import BaseSearchID


class search_title_id(BaseSearchID):
    """
    'IMDbID' method takes a title name, searches for the similar title names available in IMDb.
    and suggests the title name to the user. Based upon user's selection it returns a list of title ids.

    Input serial numbers separated with spaces.
    -------------------- -------------------- -------------------- -------------------- --------------------
    :param text: title name.
    :returns: A list of title ids.
    :raises ValueError: Raises an exception when entered a charater other than a number for selection.
    :raises IndexError: Raises an BeautifulSoup exception when index is out of range.
    """

    def __init__(self, text: str):
        super().__init__('title', text)
        self.title_name, self.title_id = self.name, self.id
