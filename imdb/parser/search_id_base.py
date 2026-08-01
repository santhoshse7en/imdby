from imdb.utils.config import search_imdb_id
from imdb.utils.helpers import unicode
from imdb.utils.utils import BeautifulSoup, get, re, sys


class BaseSearchID:
    """
    Searches IMDb for a piece of text under the given category, prints up to
    20 matching suggestions, and resolves the user's selection to name(s)/id(s).

    Input serial numbers separated with spaces.
    -------------------- -------------------- -------------------- -------------------- --------------------
    :param category: IMDb search category key (see `imdb.utils.config.search_imdb_id`).
    :param text: search text.
    :returns: A name (or list of names) and an id (or list of ids).
    :raises ValueError: Raises an exception when entered a character other than a number for selection.
    :raises IndexError: Raises an BeautifulSoup exception when index is out of range.
    """

    def __init__(self, category: str, text: str):
        self.entered_text = text
        self.url = search_imdb_id[category] % ''.join(text.split())
        soup = BeautifulSoup(get(self.url).text, 'lxml')

        results = soup.select('.result_text')
        suggestions, names = [], []

        for index, item in enumerate(results[:20]):
            print('%s: %s' % (index + 1, unicode(item.get_text())))
            suggestions.append(item.a['href'][7:16])
            names.append(item.a.text.strip())

        try:
            selected = re.findall(r"[\w']+", input('Enter serial number\t'))
            ids = [suggestions[int(i) - 1] if int(i) != 0 else '' for i in selected]
            names = [names[int(i) - 1] if int(i) != 0 else '' for i in selected]
        except Exception as es:
            print("{0} :".format(type(es)), es)
            sys.exit(0)

        if len(ids) == 1:
            self.name, self.id = names[0], ids[0]
        else:
            self.name, self.id = names, ids
