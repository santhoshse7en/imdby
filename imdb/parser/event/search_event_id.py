from imdb.parser.search_id_base import BaseSearchID


class search_event_id(BaseSearchID):
    """
    'IMDbID' method takes an event name, searches for the similar event names available in IMDb.
    and suggests the event name to the user. Based upon user's selection it returns a list of event ids.

    Input serial numbers separated with spaces.
    -------------------- -------------------- -------------------- -------------------- --------------------
    :param text: event name.
    :returns: A list of event ids.
    :raises ValueError: Raises an exception when entered a charater other than a number for selection.
    :raises IndexError: Raises an BeautifulSoup exception when index is out of range.
    """

    def __init__(self, text: str):
        super().__init__('event', text)
        self.event_name, self.event_id = self.name, self.id
