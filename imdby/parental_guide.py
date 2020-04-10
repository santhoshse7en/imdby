from imdby.utils import *


# Retrieves IMDb Parental Guide Details
class parental_guide:

    """
    Collects IMDb Parental Guide Details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, titleid):
        self.titleid = titleid
        self.parental_guide_url = "https://www.imdb.com/title/%s/parentalguide" % self.titleid
        soup = BeautifulSoup(get(self.parental_guide_url).text, 'lxml')

        """
        :returns: Movie Title
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        """
        :returns: Certificate DataFrame if available.
        """
        try:
            certificate = soup.select_one('#certificates').select('tr')
            self.certificates_df = pd.DataFrame(columns=['Name', 'Type'])

            for i in range(len(certificate)):
                try:
                    self.certificates_df.loc[len(self.certificates_df)] = [certificate[i].select_one('td.ipl-zebra-list__label').text.strip(),
                                                               ' '.join(certificate[i].select_one('td').findNext('td').text.split())]
                except:
                    pass
        except:
            self.certificates_df = None

        """
        :returns: Certificate Name if available.
        """
        try:
            self.certificates_name = self.certificates_df.Name.tolist()
        except:
            self.certificates_name = None

        """
        :returns: Certificate Type if available.
        """
        try:
            self.certificates_type = self.certificates_df.Type.tolist()
        except:
            self.certificates_type = None

        """
        :returns: Adivsory Nudity status if available.
        """
        try:
            advisory_nudity = soup.select_one('#advisory-nudity').select('li.ipl-zebra-list__item')
            self.adivsory_nudity_status = str(soup.select_one('#advisory-nudity').select_one('.ipl-status-pill').text.strip()) + " : " + str(soup.select_one('#advisory-nudity').select_one('.advisory-severity-vote__message').text.strip())
        except:
            self.adivsory_nudity_status = None

        """
        :returns: Advisory Nudity Severity Vote if available.
        """
        try:
            advisory_nudity = soup.select_one('#advisory-nudity').select('li.ipl-zebra-list__item')
            self.advisory_nudity_severity_vote = [' '.join(advisory_nudity[i].text.split()).replace("\'", "") for i in range(len(advisory_nudity))]
        except:
            self.advisory_nudity_severity_vote = None

        """
        :returns: Adivsory Violence status if available.
        """
        try:
            advisory_violence = soup.select_one('#advisory-violence').select('li.ipl-zebra-list__item')
            self.advisory_violence_status = str(soup.select_one('#advisory-violence').select_one('.ipl-status-pill').text.strip()) + " : " + str(soup.select_one('#advisory-violence').select_one('.advisory-severity-vote__message').text.strip())
        except:
            self.advisory_violence_status = None

        """
        :returns: Advisory Violence Severity Vote if available.
        """
        try:
            advisory_violence = soup.select_one('#advisory-violence').select('li.ipl-zebra-list__item')
            self.advisory_violence_severity_vote = [' '.join(advisory_violence[i].text.split()).replace("\'", "") for i in range(len(advisory_violence))]
        except:
            self.advisory_violence_severity_vote = None

        """
        :returns: Adivsory Profanity status if available.
        """
        try:
            advisory_profanity = soup.select_one('#advisory-profanity').select('li.ipl-zebra-list__item')
            self.advisory_profanity_status = str(soup.select_one('#advisory-profanity').select_one('.ipl-status-pill').text.strip()) + " : " + str(soup.select_one('#advisory-profanity').select_one('.advisory-severity-vote__message').text.strip())
        except:
            self.advisory_profanity_status = None

        """
        :returns: Advisory Profanity Severity Vote if available.
        """
        try:
            advisory_profanity = soup.select_one('#advisory-profanity').select('li.ipl-zebra-list__item')
            self.advisory_profanity_severity_vote = [' '.join(advisory_profanity[i].text.split()).replace("\'", "") for i in range(len(advisory_profanity))]
        except:
            self.advisory_profanity_severity_vote = None

        """
        :returns: Adivsory Alcohol status if available.
        """
        try:
            advisory_alcohol = soup.select_one('#advisory-alcohol').select('li.ipl-zebra-list__item')
            self.advisory_alcohol_status = str(soup.select_one('#advisory-alcohol').select_one('.ipl-status-pill').text.strip()) + " : " + str(soup.select_one('#advisory-alcohol').select_one('.advisory-severity-vote__message').text.strip())
        except:
            self.advisory_alcohol_status = None

        """
        :returns: Advisory Alcohol Severity Vote if available.
        """
        try:
            advisory_alcohol = soup.select_one('#advisory-alcohol').select('li.ipl-zebra-list__item')
            self.advisory_alcohol_severity_vote = [' '.join(advisory_alcohol[i].text.split()).replace("\'", "") for i in range(len(advisory_alcohol))]
        except:
            self.advisory_alcohol_severity_vote = None

        """
        :returns: Adivsory Frightening status if available.
        """
        try:
            advisory_frightening = soup.select_one('#advisory-frightening').select('li.ipl-zebra-list__item')
            self.advisory_frightening_status = str(soup.select_one('#advisory-frightening').select_one('.ipl-status-pill').text.strip()) + " : " + str(soup.select_one('#advisory-frightening').select_one('.advisory-severity-vote__message').text.strip())
        except:
            self.advisory_frightening_status = None

        """
        :returns: Advisory Frightening Severity Vote if available.
        """
        try:
            advisory_frightening = soup.select_one('#advisory-frightening').select('li.ipl-zebra-list__item')
            self.advisory_frightening_severity_vote = [' '.join(advisory_frightening[i].text.split()).replace("\'", "") for i in range(len(advisory_frightening))]
        except:
            self.advisory_frightening_severity_vote = None

        """
        :returns: Spoilers Violence & Gore if available.
        """
        try:
            spoiler_violence = soup.select_one('#advisory-spoilers').select_one('#advisory-spoiler-violence').select('li.ipl-zebra-list__item')
            self.spoiler_violence = [' '.join(spoiler_violence[i].contents[0].split()) for i in range(len(spoiler_violence))]
        except:
            self.spoiler_violence = None

        """
        :returns: Spoilers Alcohol, Drugs & Smoking if available.
        """
        try:
            spoiler_alcohol = soup.select_one('#advisory-spoilers').select_one('#advisory-spoiler-alcohol').select('li.ipl-zebra-list__item')
            self.spoiler_alcohol = [' '.join(spoiler_alcohol[i].contents[0].split()) for i in range(len(spoiler_alcohol))]
        except:
            self.spoiler_alcohol = None

        """
        :returns: Spoilers Frightening & Intense Scenes if available.
        """
        try:
            spoiler_frightening = soup.select_one('#advisory-spoilers').select_one('#advisory-spoiler-frightening').select('li.ipl-zebra-list__item')
            self.spoiler_frightening = [' '.join(spoiler_frightening[i].contents[0].split()) for i in range(len(spoiler_frightening))]
        except:
            self.spoiler_frightening = None

        """
        :returns: Creates Dict from the above info. if available.
        """
        try:
            self.imdb_parental_guide_metadata = {"Movie Name" : self.title,
                                                 "Title ID" : self.titleid,
                                                 "Movie Parental Guide URL" : self.parental_guide_url,
                                                 "Certificate Name" : self.certificates_name,
                                                 "Certificate Type" : self.certificates_type,
                                                 "Sex & Nudity" : {"Nudity Status" : self.adivsory_nudity_status,
                                                                   "Nudity Severity" : self.advisory_nudity_severity_vote},
                                                 "Alcohol & Smoking" : {"Alcohol Status" : self.advisory_alcohol_status,
                                                                        "Alcohol Severity" : self.advisory_alcohol_severity_vote},
                                                 "Violence" : {"Violence" : self.advisory_violence_status,
                                                               "Violence Severity" : self.advisory_violence_severity_vote},
                                                 "Frighten" : {"Frighten Status" : self.advisory_frightening_status,
                                                               "Frighten Severity" : self.advisory_frightening_severity_vote},
                                                 "Profanity" : {"Profanity Status" : self.advisory_profanity_status,
                                                                "Profanity Severity" : self.advisory_profanity_severity_vote},
                                                 "Spoiler Violence" : self.spoiler_violence,
                                                 "Spoiler Alcohol" : self.spoiler_alcohol,
                                                 "Spoiler Frighten" : self.spoiler_frightening}
        except:
            self.imdb_parental_guide_metadata = None

        print("\rParental Guide Extraction Completed\r", end="\r", flush=True)
