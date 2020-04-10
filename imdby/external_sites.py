from imdby.utils import *


# Retrieves External Sites Details
class external_sites:

    """
    Collects External Sites details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, titleid):
        self.titleid = titleid
        self.external_sites_url = "https://www.imdb.com/title/%s/externalsites" % self.titleid 
        soup = BeautifulSoup(get(self.external_sites_url).text, 'lxml')

        """
        returns: Movie Title
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        """
        returns: Official Sites DataFrame if available.
        """
        try:
            titles, urls = [], []
            official_sites = soup.select_one('#official').findNext('ul').select('li')
            for item in official_sites:
                try:
                    titles.append(item.text.strip())
                    urls.append(get('https://www.imdb.com%s' % item.a['href']).url)
                except:
                    titles.append(None)
                    urls.append(None)
            self.official_sites_df = pd.DataFrame({'Name' : titles, 'URL' : urls})
        except:
            self.official_sites_df = None

        """
        :returns: Official Site Name list if available.
        """
        try:
            self.official_sites_names = self.official_sites_df.Name.tolist()
        except:
            self.official_sites_names = None

        """
        :returns: Official Site URLs list if available.
        """
        try:
            self.official_sites_urls = self.official_sites_df.URL.tolist()
        except:
            self.official_sites_urls = None

        """
        returns: Miscellaneous Sites DataFrame if available.
        """
        try:
            titles, urls = [], []
            miscellaneous_sites = soup.select_one('#misc').findNext('ul').select('li')
            for item in miscellaneous_sites:
                try:
                    titles.append(item.text.strip())
                    urls.append(get('https://www.imdb.com%s' % item.a['href']).url)
                except:
                    titles.append(None)
                    urls.append(None)
            self.miscellaneous_sites_df = pd.DataFrame({'Name' : titles, 'URL' : urls})
        except:
            self.miscellaneous_sites_df = None

        """
        :returns: Miscellaneous Sites Names list if available.
        """
        try:
            self.miscellaneous_sites_names = self.miscellaneous_sites_df.Name.tolist()
        except:
            self.miscellaneous_sites_names = None

        """
        :returns: Miscellaneous Sites URLs list if available.
        """
        try:
            self.miscellaneous_sites_urls = self.miscellaneous_sites_df.URL.tolist()
        except:
            self.miscellaneous_sites_urls = None

        """
        returns: Photographs Sites DataFrame if available.
        """
        try:
            titles, urls = [], []
            photographs_sites = soup.select_one('#photos').findNext('ul').select('li')
            for item in photographs_sites:
                try:
                    titles.append(item.text.strip())
                    urls.append(get('https://www.imdb.com%s' % item.a['href']).url)
                except:
                    titles.append(None)
                    urls.append(None)
            self.photographs_sites_df = pd.DataFrame({'Title' : titles, 'URL' : urls})
        except:
            self.photographs_sites_df = None

        """
        :returns: Photographs Sites Names list if available.
        """
        try:
            self.photographs_sites_names = self.photographs_sites_df.Name.tolist()
        except:
            self.photographs_sites_names = None

        """
        :returns: Photographs Sites URLs list if available.
        """
        try:
            self.photographs_sites_urls = self.photographs_sites_df.URL.tolist()
        except:
            self.photographs_sites_urls = None

        """
        returns: Videos Clips and Trailers Sites DataFrame if available.
        """
        try:
            titles, urls = [], []
            videos_clips_and_trailers_sites = soup.select_one('#videos').findNext('ul').select('li')
            for item in videos_clips_and_trailers_sites:
                try:
                    titles.append(item.text.strip())
                    urls.append(get('https://www.imdb.com%s' % item.a['href']).url)
                except:
                    titles.append(None)
                    urls.append(None)
            self.videos_clips_and_trailers_sites_df = pd.DataFrame({'Title' : titles, 'URL' : urls})
        except:
            self.videos_clips_and_trailers_sites_df = None

        """
        :returns: Videos Clips and Trailers Sites Names list if available.
        """
        try:
            self.videos_clips_and_trailers_sites_names = self.videos_clips_and_trailers_sites_df.Name.tolist()
        except:
            self.videos_clips_and_trailers_sites_names = None

        """
        :returns: Videos Clips and Trailers Sites URLs list if available.
        """
        try:
            self.videos_clips_and_trailers_sites_urls = self.videos_clips_and_trailers_sites_df.URL.tolist()
        except:
            self.videos_clips_and_trailers_sites_urls = None

        """
        :returns: Creates Meta Data from the above info. if available.
        """
        try:
            self.imdb_external_sites_metadata = {"Movie Title" : self.title,
                                               "Title ID" : self.titleid,
                                               "Movie URL" : self.external_sites_url,
                                               "Official Sites" : {"Name" : self.official_sites_names,
                                                                  "URL" : self.official_sites_urls},
                                               "Miscellaneous Sites" : {"Name" : self.miscellaneous_sites_names,
                                                                        "URL" : self.miscellaneous_sites_urls},
                                               "Photographs" : {"Name" : self.photographs_sites_names,
                                                                "URL" : self.photographs_sites_urls},
                                               "Video Clips and Trailers" : {"Name" : self.videos_clips_and_trailers_sites_names,
                                                                             "URL" : self.videos_clips_and_trailers_sites_urls}}
        except:
            self.imdb_external_sites_metadata = None

        sys.stdout.write('\r' + str("External Sites Extraction Completed") +  '\r')
        sys.stdout.flush()

# main class which passes the titleid to indiviual class
class imdb:
    def __init__(self, titleid):
        start_time = datetime.now()
        external_sites.__init__(self, titleid)

        time_delta = datetime.now() - start_time
        print("\rCalculating time taken for external sites extraction : %s  seconds\r" % (time_delta.seconds), end="\r", flush=True)
