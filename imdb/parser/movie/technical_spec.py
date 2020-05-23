from imdb.utils.config import base_uri, imdb_uris, tag_search
from imdb.utils.helpers import (catch, catch_dict, catch_list,
                                     dataframe_data, index_finder,
                                     technical_specs, unicode)
from imdb.utils.utils import BeautifulSoup, get, pd, re


# Retrieves IMDb Technical Spec Details
class technical_spec:

    """
    Collects IMDb Technical Spec Details of the multi-media content in IMDb when title_id is given.
    :param title_id: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, title_id):
        self.title_id = title_id
        self.technical_spec_url = imdb_uris["technical"] % self.title_id
        soup = BeautifulSoup(get(self.technical_spec_url).text, 'lxml')
        technical_spec_tag = soup.select('td[class="label"]')

        """
        :returns: Movie Title
        """
        movie_tag = soup.select_one('h3[itemprop="name"]')
        self.title = catch(lambda: unicode(movie_tag.a.get_text()))
        self.title_uri = catch(lambda: unicode(
            '%s%s' % (base_uri, movie_tag.a['href'][1:])))
        self.year = catch(lambda: int(re.findall(
            r"\d+", unicode(movie_tag.select_one('.nobr').get_text()))[0]))

        """
        :returns: movie runtime if available.
        """
        self.runtime = catch(lambda: unicode(technical_spec_tag[index_finder(
            technical_spec_tag, tag_search['runtime'])].findNext('td').text))

        """
        :returns: movie sound mix if available.
        """
        sound_mix = catch(lambda: technical_spec_tag[index_finder(
            technical_spec_tag, tag_search['sound mix'])].findNext('td').select('a'))
        self.sound_mix_df = catch(lambda: technical_specs(sound_mix))
        self.sound_mix_name = catch_list(lambda: self.sound_mix_df.Name.tolist())
        self.sound_mix_uri = catch_list(lambda: self.sound_mix_df.URI.tolist())

        """
        :returns: movie color if available.
        """
        color = catch(lambda: technical_spec_tag[index_finder(
            technical_spec_tag, tag_search['color'])].findNext('td').select('a'))
        self.color_df = catch(lambda: technical_specs(color))
        self.color_name = catch_list(lambda: self.color_df.Name.tolist())
        self.color_uri = catch_list(lambda: self.color_df.URI.tolist())

        """
        :returns: movie aspect ratio if available.
        """
        aspect_ratio = catch_list(lambda: list(technical_spec_tag[index_finder(
            technical_spec_tag, 'aspect ratio')].findNext('td').stripped_strings))
        self.aspect_ratio = catch_list(
            lambda: [unicode(' '.join(item.split())) for item in aspect_ratio])

        """
        :returns: movie camera if available.
        """
        camera = catch_list(lambda: list(technical_spec_tag[index_finder(
            technical_spec_tag, 'camera')].findNext('td').stripped_strings))
        self.camera = catch_list(
            lambda: [unicode(' '.join(item.split())) for item in camera])

        """
        :returns: movie laboratory if available.
        """
        laboratory = catch_list(lambda: list(technical_spec_tag[index_finder(
            technical_spec_tag, 'laboratory')].findNext('td').stripped_strings))
        self.laboratory = catch_list(
            lambda: [unicode(' '.join(item.split())) for item in laboratory])

        """
        :returns: negative format if available.
        """
        self.negative_format = catch_list(lambda: unicode(' '.join(technical_spec_tag[index_finder(
            technical_spec_tag, 'negative format')].findNext('td').get_text().split())))

        """
        :returns: cinematography process if available.
        """
        cinematographic_process = catch_list(lambda: list(technical_spec_tag[index_finder(
            technical_spec_tag, 'cinematographic process')].findNext('td').stripped_strings))
        self.cinematographic_process = catch_list(
            lambda: [unicode(' '.join(item.split())) for item in cinematographic_process])

        """
        :returns: printed film format if available.
        """
        printed_film_format = catch_list(lambda: list(technical_spec_tag[index_finder(
            technical_spec_tag, 'printed film format')].findNext('td').stripped_strings))
        self.printed_film_format = catch_list(
            lambda: [unicode(' '.join(item.split())) for item in printed_film_format])

        """
        :returns: film length if available.
        """
        film_length = catch_list(lambda: list(technical_spec_tag[index_finder(
            technical_spec_tag, 'film length')].findNext('td').stripped_strings))
        self.film_length = catch_list(
            lambda: [unicode(' '.join(item.split())) for item in film_length])

        """
        :returns: Creates Dict from the above info. if available.
        """

        self.imdb_technical_spec_metadata = catch_dict(lambda: {"Movie Name": self.title,
                                                                "Movie URI": self.title_uri,
                                                                "Title ID": self.title_id,
                                                                "Year": self.year,
                                                                "Movie Technical Spec URL": self.technical_spec_url,
                                                                "Runtime": self.runtime,
                                                                "Sound Mix": {"Name": self.sound_mix_name,
                                                                              "URI": self.sound_mix_uri},
                                                                "Color": {"Name": self.color_name,
                                                                          "URI": self.color_uri},
                                                                "Aspect Ratio": self.aspect_ratio,
                                                                "Camera": self.camera,
                                                                "Laboratory": self.laboratory,
                                                                "Negative Film Format": self.negative_format,
                                                                "Cinematography Process": self.cinematographic_process,
                                                                "Printed Film Format": self.printed_film_format,
                                                                "Film Length": self.film_length})
