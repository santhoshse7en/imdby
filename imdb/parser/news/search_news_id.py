from imdb.parser.search_id_base import BaseSearchID


class search_news_id(BaseSearchID):
    """
    'IMDbID' method takes a news title, searches for the similar news titles available in IMDb.
    and suggests the news title to the user. Based upon user's selection it returns a list of news ids.

    Input serial numbers separated with spaces.
    -------------------- -------------------- -------------------- -------------------- --------------------
    :param text: news title.
    :returns: A list of news ids.
    :raises ValueError: Raises an exception when entered a charater other than a number for selection.
    :raises IndexError: Raises an BeautifulSoup exception when index is out of range.
    """

    def __init__(self, text: str):
        super().__init__('news', text)
        self.news_title, self.news_id = self.name, self.id
