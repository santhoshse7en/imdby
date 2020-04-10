from imdby.utils import *


# Retrieves IMDb Full Cast & Crew Details
class cast_and_crew:

    """
    Collects full cast & crew details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """
    def __init__(self, titleid):
        self.titleid = titleid
        self.cast_and_crew_url = "https://www.imdb.com/title/%s/fullcredits" % self.titleid
        soup = BeautifulSoup(get(self.cast_and_crew_url).text, 'lxml')

        """
        :returns: Movie Title
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        """
        :returns: Writtern Credits DataFrame
        """
        try:
            w_index = [i for i in range(len(soup.select('h4'))) if 'writing' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            writer = soup.select('h4')[w_index].findNext('table').select('tr')
            self.writers_df = pd.DataFrame(columns=['Name', 'Credit', 'ID'])

            for i in range(len(writer)):
                try:
                    self.writers_df.loc[len(self.writers_df)] = [writer[i].select_one('td.name').a.text.strip(),
                                                                 writer[i].select_one('td.credit').text.strip(),
                                                                 writer[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
        except:
            self.writers_df = None

        """
        :returns: Writers list
        """
        try:
            self.writers = self.writers_df.Name.tolist()
        except:
            self.writers = None

        """
        :returns: Writers ID list
        """
        try:
            self.writers_id = self.writers_df.ID.tolist()
        except:
            self.writers_id = None

        """
        :returns: Writers Credit list
        """
        try:
            self.writers_credit = self.writers_df.Credit.tolist()
        except:
            self.writers_credit = None

        """
        :returns: Directed_by DataFrame
        """
        try:
            d_index = [i for i in range(len(soup.select('h4'))) if 'directed' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            director = soup.select('h4')[d_index].findNext('table').select('tr')
            self.directors_df = pd.DataFrame(columns=['Name', 'ID'])

            for i in range(len(director)):
                try:
                    self.directors_df.loc[len(self.directors_df)] = [director[i].select_one('td.name').a.text.strip(),
                                                                     director[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
        except:
            self.directors_df = None

        """
        :returns: Directors list
        """
        try:
            self.directors = self.directors_df.Name.tolist()
        except:
            self.directors = None

        """
        :returns: Directors ID list
        """
        try:
            self.directors_id = self.directors_df.ID.tolist()
        except:
            self.directors_id = None

        """
        :returns: Produced_by DataFrame
        """
        try:
            p_index = [i for i in range(len(soup.select('h4'))) if 'produced' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            producer = soup.select('h4')[p_index].findNext('table').select('tr')
            self.producers_df = pd.DataFrame(columns=['Name', 'Credit', 'ID'])

            for i in range(len(producer)):
                try:
                    self.producers_df.loc[len(self.producers_df)] = [producer[i].select_one('td.name').a.text.strip(),
                                                                     producer[i].select_one('td.credit').text.strip(),
                                                                     producer[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
        except:
            self.producers_df = None

        """
        :returns: Producers list
        """
        try:
            self.producers = self.producers_df.Name.tolist()
        except:
            self.producers = None

        """
        :returns: Producers ID list
        """
        try:
            self.producers_id = self.producers_df.ID.tolist()
        except:
            self.producers_id = None

        """
        :returns: Producers Credit list
        """
        try:
            self.producers_credit = self.producers_df.Credit.tolist()
        except:
            self.producers_credit = None

        """
        :returns: Cast DataFrame
        """
        try:
            c_index = [i for i in range(len(soup.select('h4'))) if 'cast' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            casting = soup.select('h4')[c_index].findNext('table').select('tr')
            self.cast_df = pd.DataFrame(columns=['Name', 'Image', 'Character', 'ID'])

            for i in range(len(casting)):
                try:
                    self.cast_df.loc[len(self.cast_df)] = [casting[i].select_one('td.primary_photo').a.img['title'].strip(),
                                                           casting[i].select_one('td.primary_photo').a.img['src'].strip(),
                                                           ' '.join(casting[i].select_one('td.character').text.split()).strip(),
                                                           casting[i].select_one('td.primary_photo').a['href'][6:15].strip()]
                except:
                    pass
        except:
            self.cast_df = None

        """
        :returns: Cast list
        """
        try:
            self.cast = self.cast_df.Name.tolist()
        except:
            self.cast = None

        """
        :returns: Cast ID list
        """
        try:
            self.cast_id = self.cast_df.ID.tolist()
        except:
            self.cast_id = None

        """
        :returns: Cast Character/Role list
        """
        try:
            self.cast_character = self.cast_df.Character.tolist()
        except:
            self.cast_character = None

        """
        :returns: Cast Image URL list
        """
        try:
            self.cast_character_img_url = self.cast_df.Image.tolist()
        except:
            self.cast_character_img_url = None

        """
        :returns: Music by DataFrame
        """
        try:
            m_index = [i for i in range(len(soup.select('h4'))) if 'music' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            music = soup.select('h4')[m_index].findNext('table').select('tr')
            self.music_df = pd.DataFrame(columns=['Name', 'ID'])

            for i in range(len(music)):
                try:
                    self.music_df.loc[len(self.music_df)] = [music[i].select_one('td.name').a.text.strip(),
                                                             music[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
        except:
            self.music_df = None

        """
        :returns: Music by list
        """
        try:
            self.music = self.music_df.Name.tolist()
        except:
            self.music = None

        """
        :returns: Music by ID list
        """
        try:
            self.music_id = self.music_df.ID.tolist()
        except:
            self.music_id = None

        """
        :returns: Cinematography by DataFrame
        """
        try:
            ct_index = [i for i in range(len(soup.select('h4'))) if 'cinematography' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            cinematography = soup.select('h4')[ct_index].findNext('table').select('tr')
            self.cinematography_df = pd.DataFrame(columns=['Name', 'ID'])

            for i in range(len(cinematography)):
                try:
                    self.cinematography_df.loc[len(self.cinematography_df)] = [cinematography[i].select_one('td.name').a.text.strip(),
                                                                               cinematography[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
        except:
            self.cinematography_df = None

        """
        :returns: Cinematography by list
        """
        try:
            self.cinematography = self.cinematography_df.Name.tolist()
        except:
            self.cinematography = None

        """
        :returns: Cinematography by ID list
        """
        try:
            self.cinematography_id = self.cinematography_df.ID.tolist()
        except:
            self.cinematography_id = None

        """
        :returns: Production Design by DataFrame
        """
        try:
            pd_index = [i for i in range(len(soup.select('h4'))) if 'production design' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            production_designer = soup.select('h4')[pd_index].findNext('table').select('tr')
            self.production_designer_df = pd.DataFrame(columns=['Name', 'ID'])

            for i in range(len(production_designer)):
                try:
                    self.production_designer_df.loc[len(self.production_designer_df)] =[production_designer[i].select_one('td.name').a.text.strip(),
                                                                                       production_designer[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
        except:
            self.cinematography_df = None

        """
        :returns: Production Design by list
        """
        try:
            self.production_designer = self.production_designer_df.Name.tolist()
        except:
            self.production_designer = None

        """
        :returns: Production Design by ID list
        """
        try:
            self.production_designer_id = self.production_designer_df.ID.tolist()
        except:
            self.production_designer_id = None

        """
        :returns: Film Editing by  DataFrame
        """
        try:
            fe_index = [i for i in range(len(soup.select('h4'))) if 'film editing' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            film_editing = soup.select('h4')[fe_index].findNext('table').select('tr')
            self.film_editing_df = pd.DataFrame(columns=['Name', 'Credit', 'ID'])

            for i in range(len(film_editing)):
                try:
                    self.film_editing_df.loc[len(self.film_editing_df)] = [film_editing[i].select_one('td.name').a.text.strip(),
                                                                           film_editing[i].select_one('td.credit').text.strip(),
                                                                           film_editing[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
        except:
            self.film_editing_df = None

        """
        :returns: Film Editing list
        """
        try:
            self.film_editing = self.film_editing_df.Name.tolist()
        except:
            self.film_editing = None

        """
        :returns: Film Editing ID list
        """
        try:
            self.film_editing_id = self.film_editing_df.ID.tolist()
        except:
            self.film_editing_id = None

        """
        :returns: Film Editing Credit list
        """
        try:
            self.film_editing_credit = self.film_editing_df.Credit.tolist()
        except:
            self.film_editing_credit = None

        """
        :returns: Casting by  DataFrame
        """
        try:
            cg_index = [i for i in range(len(soup.select('h4'))) if 'casting' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            casting_d = soup.select('h4')[cg_index].findNext('table').select('tr')
            self.casting_df = pd.DataFrame(columns=['Name', 'Credit', 'ID'])

            for i in range(len(casting_d)):
                try:
                    self.casting_df.loc[len(self.casting_df)] = [casting_d[i].select_one('td.name').a.text.strip(),
                                                                 casting_d[i].select_one('td.credit').text.strip(),
                                                                 casting_d[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
        except:
            self.casting_df = None

        """
        :returns: Casting list
        """
        try:
            self.casting = self.casting_df.Name.tolist()
        except:
            self.casting = None

        """
        :returns: Casting ID list
        """
        try:
            self.casting_id = self.casting_df.ID.tolist()
        except:
            self.casting_id = None

        """
        :returns: Casting Credit list
        """
        try:
            self.casting_credit = self.casting_df.Credit.tolist()
        except:
            self.casting_credit = None

        """
        :returns: Creates Dict from the above info. if available.
        """
        try:
            self.imdb_cast_metadata = {"Movie Name" : self.title,
                                       "Title ID" : self.titleid,
                                       "Movie Full Cast and Crew URL" : self.cast_and_crew_url,
                                       "Director" : { "Name": self.directors,
                                                     "ID" : self.directors_id},
                                       "Writer" : {"Name" : self.writers,
                                                   "Credit" : self.writers_credit,
                                                   "ID" : self.writers_id},
                                       "Cast" : {"Name" : self.cast,
                                                 "Character" : self.cast_character,
                                                 "Image" : self.cast_character_img_url,
                                                 "ID" : self.cast_id},
                                       "Producer" : {"Name" : self.producers,
                                                     "Credit" : self.producers_credit,
                                                     "ID" : self.producers_id},
                                       "Music" : {"Name" : self.music,
                                                  "ID" : self.music_id},
                                       "Cinematography" : {"Name" : self.cinematography,
                                                           "ID" : self.cinematography_id},
                                       "Production Desing" : {"Name" : self.production_designer,
                                                              "ID" : self.production_designer_id},
                                       "Flim Editing" : {"Name" : self.film_editing,
                                                         "Credit" : self.film_editing_credit,
                                                         "ID" : self.film_editing_id},
                                       "Casting" : {"Name" : self.casting,
                                                    "Credit" : self.casting_credit,
                                                    "ID" : self.casting_id}}
        except:
            self.imdb_cast_metadata = None

        print("\rFull Cast & Crew Extraction Completed\r", end="\r", flush=True)
