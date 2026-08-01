from imdb.parser.search_id_base import BaseSearchID


class search_character_id(BaseSearchID):
    """
    'IMDbID' method takes a character name, searches for the similar character names available in IMDb.
    and suggests the character name to the user. Based upon user's selection it returns a list of character ids.

    Input serial numbers separated with spaces.
    -------------------- -------------------- -------------------- -------------------- --------------------
    :param text: character name.
    :returns: A list of character ids.
    :raises ValueError: Raises an exception when entered a charater other than a number for selection.
    :raises IndexError: Raises an BeautifulSoup exception when index is out of range.
    """

    def __init__(self, text: str):
        super().__init__('character', text)
        self.character_name, self.character_id = self.name, self.id
