from imdby.utils.config import base_uri, imdb_uris, tag_search
from imdby.utils.helper_function import (adivsory_satus, advisory_reviews, catch,
                                     catch_dict, catch_list, dataframe_data,
                                     unicode)
from imdby.utils.utils import BeautifulSoup, get, pd, re


# Retrieves IMDb Parental Guide Details
class parental_guide:

    """
    Collects IMDb Parental Guide Details of the multi-media content in IMDb when title_id is given.
    :param title_id: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, title_id):
        self.title_id = title_id
        self.parental_guide_url = imdb_uris["parentalguide"] % self.title_id
        soup = BeautifulSoup(get(self.parental_guide_url).text, 'lxml')

        """
        :returns: Movie Title
        """
        movie_tag = soup.select_one('h3[itemprop="name"]')
        self.title = catch(lambda: unicode(movie_tag.a.get_text()))
        self.title_url = catch(lambda: unicode(
            '%s%s' % (base_uri, movie_tag.a['href'][1:])))
        self.year = catch(lambda: int(re.findall(
            r"\d+", unicode(movie_tag.select_one('.nobr').get_text()))[0]))

        """
        :returns: MPAA available.
        """
        mpaa = catch(lambda: soup.select_one(
            tag_search['certificates']).select_one(tag_search['mpaa']))
        mpaa_tag = catch(lambda: mpaa.select_one(
            'td[class="ipl-zebra-list__label"]'))
        self.mpaa_name = catch(lambda: unicode(mpaa_tag.get_text()))
        self.mpaa_description = catch(
            lambda: unicode(mpaa_tag.findNext('td').get_text()))

        """
        :returns: Certificate DataFrame if available.
        """
        try:
            certificates = catch(lambda: soup.select_one(tag_search['certificates']).select_one(tag_search['certifications']).find(
                'td', string='Certification').findNextSibling('td').select('li.ipl-inline-list__item'))

            self.certificates_df = pd.DataFrame(columns=['Name', 'URI'])

            for tag in certificates:
                self.certificates_df.loc[len(self.certificates_df)] = [catch(lambda: unicode(tag.a.get_text())),
                                                                       catch(lambda: unicode("%s%s" % (base_uri, tag.a['href'][1:])))]

            self.certificates_df = dataframe_data(self.certificates_df)
        except:
            self.certificates_df = None

        self.certificates_name = catch_list(
            lambda: self.certificates_df.Name.tolist())
        self.certificates_uri = catch_list(
            lambda: self.certificates_df.URI.tolist())

        """
        :returns: Adivsory Nudity status if available.
        """
        advisory = catch(lambda: soup.select_one(
            tag_search['advisory-nudity']))
        severity = advisory.select_one(tag_search['nudity'])
        self.adivsory_nudity_severity_status = catch_dict(
            lambda: adivsory_satus(severity))

        self.advisory_nudity_reviews = catch_list(
            lambda: advisory_reviews(advisory))

        """
        :returns: Adivsory Violence status if available.
        """
        advisory = catch(lambda: soup.select_one(
            tag_search['advisory-violence']))
        severity = advisory.select_one(tag_search['violence'])
        self.advisory_violence_severity_status = catch_dict(
            lambda: adivsory_satus(severity))

        self.advisory_violence_reviews = catch_list(
            lambda: advisory_reviews(advisory))

        """
        :returns: Adivsory Profanity status if available.
        """
        advisory = catch(lambda: soup.select_one(
            tag_search['advisory-profanity']))
        severity = advisory.select_one(tag_search['profanity'])
        self.advisory_profanity_severity_status = catch_dict(
            lambda: adivsory_satus(severity))

        self.advisory_profanity_reviews = catch_list(
            lambda: advisory_reviews(advisory))

        """
        :returns: Adivsory Alcohol status if available.
        """
        advisory = catch(lambda: soup.select_one(
            tag_search['advisory-alcohol']))
        severity = advisory.select_one(tag_search['alcohol'])

        self.advisory_alcohol_severity_status = catch_dict(
            lambda: adivsory_satus(severity))

        self.advisory_alcohol_reviews = catch_list(
            lambda: advisory_reviews(advisory))

        """
        :returns: Adivsory Frightening status if available.
        """
        advisory = catch(lambda: soup.select_one(
            tag_search['advisory-frightening']))
        severity = advisory.select_one(tag_search['frightening'])
        self.advisory_frightening_severity_status = catch_dict(
            lambda: adivsory_satus(severity))

        self.advisory_frightening_reviews = catch_list(
            lambda: advisory_reviews(advisory))

        """
        :returns: Spoilers Violence & Gore if available.
        """
        advisory = catch(lambda: soup.select_one(
            tag_search['advisory-spoilers']).select_one('section[id="advisory-spoiler-violence"]'))
        self.spoiler_violence_reviews = catch_list(
            lambda: advisory_reviews(advisory))

        """
        :returns: Spoilers Alcohol, Drugs & Smoking if available.
        """
        advisory = catch(lambda: soup.select_one(
            tag_search['advisory-spoilers']).select_one('section[id="advisory-spoiler-profanity"]'))
        self.spoiler_alcohol_reviews = catch_list(
            lambda: advisory_reviews(advisory))

        """
        :returns: Spoilers Frightening & Intense Scenes if available.
        """
        advisory = catch(lambda: soup.select_one(
            tag_search['advisory-spoilers']).select_one('section[id="advisory-spoiler-frightening"]'))
        self.spoiler_frightening_reviews = catch_list(
            lambda: advisory_reviews(advisory))

        """
        :returns: Creates Dict from the above info. if available.
        """
        self.imdb_parental_guide_metadata = catch_dict(lambda: {"Movie Name": self.title,
                                                                "Movie URI": self.title_url,
                                                                "Title ID": self.title_id,
                                                                "Year": self.year,
                                                                "Movie Parental Guide URL": self.parental_guide_url,
                                                                "MPAA Name": self.mpaa_name,
                                                                "MPAA Description": self.mpaa_description,
                                                                "Certificate": self.certificates_name,
                                                                "Certificate URI": self.certificates_uri,
                                                                "Sex & Nudity": {"Nudity Severity": self.adivsory_nudity_severity_status,
                                                                                 "Nudity Review": self.advisory_nudity_reviews},
                                                                "Alcohol & Smoking": {"Alcohol Severity": self.advisory_alcohol_severity_status,
                                                                                      "Alcohol Review": self.advisory_alcohol_reviews},
                                                                "Violence": {"Violence Severity": self.advisory_violence_severity_status,
                                                                             "Violence Review": self.advisory_violence_reviews},
                                                                "Frighten": {"Frighten Severity": self.advisory_frightening_severity_status,
                                                                             "Frighten Review": self.advisory_frightening_reviews},
                                                                "Profanity": {"Profanity Severity": self.advisory_profanity_severity_status,
                                                                              "Profanity Review": self.advisory_profanity_reviews},
                                                                "Spoiler Violence": self.spoiler_violence_reviews,
                                                                "Spoiler Alcohol": self.spoiler_alcohol_reviews,
                                                                "Spoiler Frighten": self.spoiler_frightening_reviews})
