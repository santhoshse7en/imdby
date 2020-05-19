from imdby.utils.config import base_uri, search_imdb_id
from imdby.utils.helpers import unicode
from imdby.utils.utils import BeautifulSoup, get, re, sys, unidecode


class search_event_id:
    """
    'IMDbID' method takes a title name, searches for the similar title names available in IMDb.
    and suggests the title name to the user. Based upon user's selection it returns a list of title ids.

    Input serial numbers separated with spaces.
    -------------------- -------------------- -------------------- -------------------- --------------------
    :param movie: title name.
    :returns: A list of title ids.
    :raises ValueError: Raises an exception when entered a charater other than a number for selection.
    :raises IndexError: Raises an BeautifulSoup exception when index is out of range.
    """

    def __init__(self, text: str) -> bool:

        self.entered_text = text
        self.url = '%sfind?q=%s%s' % (base_uri, ''.join(
            self.entered_text.split()), search_imdb_id["event"])
        soup = BeautifulSoup(get(self.url).text, 'lxml')

        suggestions, names, imdbids = [], [], []

        name = soup.select('.result_text')

        try:
            if len(name) > 20:
                for item in name[:20]:
                    print('%s: %s' %
                          ((name.index(item) + 1), unicode(item.get_text())))
                    suggestions.append(item.a['href'][7:16])
                    names.append(item.a.text.strip())
            else:
                for item in name:
                    print('%s: %s' %
                          ((name.index(item) + 1), unicode(item.get_text())))
                    suggestions.append(item.a['href'][7:16])
                    names.append(item.a.text.strip())

            input_name = re.findall(r"[\w']+", input('Enter serial number\t'))
            imdbids = [
                suggestions[int(load) - 1] if int(load) != 0 else '' for load in input_name]
            names = [names[int(load) - 1] if int(load) !=
                     0 else '' for load in input_name]

            if len(imdbids) == 1:
                self.title_name = names[0]
                self.title_id = imdbids[0]
            else:
                self.title_name = names
                self.title_id = imdbids

        except Exception as es:
            print("{0} :".format(type(es)), es)
            sys.exit(0)
