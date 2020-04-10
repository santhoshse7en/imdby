from imdby.utils import *


class company_name:
    """
    'IMDbID' method takes a company name, searches for the similar company names available in IMDb.
    and suggests the company name to the user. Based upon user's selection it returns a list of company ids.

    Input serial numbers separated with spaces.
    -------------------- -------------------- -------------------- -------------------- --------------------
    :param movie: company name.
    :returns: A list of company ids.
    :raises ValueError: Raises an exception when entered a charater other than a number for selection.
    :raises IndexError: Raises an BeautifulSoup exception when index is out of range.
    """

    def __init__(self, text):
        self.entered_text = text
        self.url = 'https://www.imdb.com/find?q=%s&s=co&ref_=fn_al_co_mr' % ''.join(self.entered_text.split())
        soup = BeautifulSoup(get(self.url).text, 'lxml')

        suggestions, names, imdbids = [], [], []

        name = soup.select('.result_text')

        try:
            if len(name) > 20:
                for item in name[:20]:
                    print('%s' %(name.index(item) + 1) + ': ' + item.text.strip())
                    suggestions.append(item.a['href'][9:18])
                    names.append(item.a.text.strip())
            else:
                for item in name:
                    print('%s' %(name.index(item) + 1) + ': ' + item.text.strip())
                    suggestions.append(item.a['href'][9:18])
                    names.append(item.a.text.strip())

            input_name = re.findall(r"[\w']+", input('Enter serial number\t'))
            imdbids = [suggestions[int(load) - 1] if int(load) != 0 else '' for load in input_name]
            names = [names[int(load) - 1] if int(load) != 0 else '' for load in input_name]


            if len(imdbids) == 1:
                self.company_name = names[0]
                self.company_id = imdbids[0]
            else:
                self.company_name = names
                self.company_id = imdbids

        except Exception as es:
            print("{0} :".format(type(es)), es)
            sys.exit(0)

# main class which passes the titleid to indiviual class
class imdb:
    def __init__(self, text):
        start_time = datetime.now()
        company_name.__init__(self, text)

        time_delta = datetime.now() - start_time
        print("\rCalculating time taken for search company extraction : %s  seconds\r" % (time_delta.seconds), end="\r", flush=True)
