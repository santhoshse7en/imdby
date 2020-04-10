from imdby.utils import *


# Retrieves IMDb Technical Spec Details
class technical_spec:

    """
    Collects IMDb Technical Spec Details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, titleid):
        self.titleid = titleid
        self.technical_spec_url = "https://www.imdb.com/title/%s/technical" % str(self.titleid)
        soup = BeautifulSoup(get(self.technical_spec_url).text, 'lxml')
        technical_spec = soup.select('td[class="label"]')

        """
        :returns: movie title if available.
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        """
        :returns: movie runtime if available.
        """
        try:
            runtime_index = [i for i in range(len(soup.select('td[class="label"]'))) if 'runtime' in  ' '.join(soup.select('td[class="label"]')[i].text.split()).lower()][0]
            self.runtime = ' '.join(technical_spec[runtime_index].findNext('td').text.split())
        except:
            self.runtime = None

        """
        :returns: movie sound mix if available.
        """
        try:
            sound_mix_index = [i for i in range(len(technical_spec)) if 'sound mix' in  ' '.join(technical_spec[i].text.split()).lower()][0]
            self.sound_mix = ' '.join(technical_spec[sound_mix_index].findNext('td').text.split()).split('|')
        except:
            self.sound_mix = None

        """
        :returns: movie color if available.
        """
        try:
            color_index = [i for i in range(len(technical_spec)) if 'color' in  ' '.join(technical_spec[i].text.split()).lower()][0]
            self.color = ' '.join(technical_spec[color_index].findNext('td').text.split()).split('|')
        except:
            self.color = None

        """
        :returns: movie aspect ratio if available.
        """
        try:
            aspect_ratio_index = [i for i in range(len(technical_spec)) if 'aspect ratio' in  ' '.join(technical_spec[i].text.split()).lower()][0]
            aspect_ratio = list(technical_spec[aspect_ratio_index].findNext('td').stripped_strings)
            self.aspect_ratio = [' '.join(aspect_ratio[i].split()) for i in range(len(aspect_ratio))]
        except:
            self.aspect_ratio = None

        """
        :returns: movie camera if available.
        """
        try:
            camera_index = [i for i in range(len(technical_spec)) if 'camera' in  ' '.join(technical_spec[i].text.split()).lower()][0]
            camera = list(technical_spec[camera_index].findNext('td').stripped_strings)
            self.camera = [' '.join(camera[i].split()) for i in range(len(camera))]
        except:
            self.camera = None

        """
        :returns: movie laboratory if available.
        """
        try:
            laboratory_index = [i for i in range(len(technical_spec)) if 'laboratory' in  ' '.join(technical_spec[i].text.split()).lower()][0]
            laboratory = list(technical_spec[laboratory_index].findNext('td').stripped_strings)
            self.laboratory = [' '.join(laboratory[i].split()) for i in range(len(laboratory))]
        except:
            self.laboratory = None

        """
        :returns: negative format if available.
        """
        try:
            negative_format_index = [i for i in range(len(technical_spec)) if 'negative format' in  ' '.join(technical_spec[i].text.split()).lower()][0]
            self.negative_format = technical_spec[negative_format_index].findNext('td').text.strip()
        except:
            self.negative_format = None

        """
        :returns: cinematography process if available.
        """
        try:
            cinematographic_process_index = [i for i in range(len(technical_spec)) if 'cinematographic process' in  ' '.join(technical_spec[i].text.split()).lower()][0]
            cinematographic_process = list(technical_spec[cinematographic_process_index].findNext('td').stripped_strings)
            self.cinematographic_process = [' '.join(cinematographic_process[i].split()) for i in range(len(cinematographic_process))]
        except:
            self.cinematographic_process = None

        """
        :returns: printed film format if available.
        """
        try:
            printed_film_format_index = [i for i in range(len(technical_spec)) if 'printed film format' in  ' '.join(technical_spec[i].text.split()).lower()][0]
            printed_film_format = list(technical_spec[printed_film_format_index].findNext('td').stripped_strings)
            self.printed_film_format = [' '.join(printed_film_format[i].split()) for i in range(len(printed_film_format))]
        except:
            self.printed_film_format = None

        """
        :returns: film length if available.
        """
        try:
            film_length_index = [i for i in range(len(technical_spec)) if 'film length' in  ' '.join(technical_spec[i].text.split()).lower()][0]
            film_length = list(technical_spec[film_length_index].findNext('td').stripped_strings)
            self.film_length = [' '.join(film_length[i].split()) for i in range(len(film_length))]
        except:
            self.film_length = None

        """
        :returns: Creates Dict from the above info. if available.
        """
        try:
            self.imdb_technical_spec_metadata = {"Movie Name" : self.title,
                                                 "Title ID" : self.titleid,
                                                 "Movie Technical Spec URL" : self.technical_spec_url,
                                                 "Runtime" : self.runtime,
                                                 "Sound Mix" : self.sound_mix,
                                                 "Color" : self.color,
                                                 "Aspect Ratio" : self.aspect_ratio,
                                                 "Camera" : self.camera,
                                                 "Laboratory" : self.laboratory,
                                                 "Negative Film Format" : self.negative_format,
                                                 "Cinematography Process" : self.cinematographic_process,
                                                 "Printed Film Format" : self.printed_film_format,
                                                 "Film Length" : self.film_length}
        except:
            self.imdb_technical_spec_metadata = None

        print("\rTechincal Spec Extraction Completed\r", end="\r", flush=True)
