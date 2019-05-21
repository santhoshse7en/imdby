from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import time, sys

# Retrieves IMDb MovieDetails
class movie:

    """
    Collects basic movie details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, titleid):
        start = time.time()
        self.titleid = titleid
        self.movie_url = "https://www.imdb.com/title/" + self.titleid
        soup = BeautifulSoup(get(self.movie_url).text, 'lxml')

        """
        :returns: Movie Name if available.
        """
        try:
            self.title = soup.select_one('h1[class=""]').contents[0].strip()
        except:
            self.title = None

        """
        :returns: Genre types for the movie if available.
        """
        try:
            self.genre = [soup.find('h4', string='Genres:').findNextSiblings('a')[i].text.strip() for i in range(len(soup.find('h4', string='Genres:').findNextSiblings('a')))]
        except:
            self.genre = None

        """
        :returns: IMDb rating for the movie if available.
        """
        try:
            self.rating = soup.select_one('span[itemprop="ratingValue"]').text.strip()
        except:
            self.rating = None

        """
        :returns: IMDb votes obtained for the movie if available.
        """
        try:
            self.imdb_votes = soup.select_one('span[itemprop="ratingCount"]').text.strip()
        except:
            self.imdb_votes = None

        """
        :returns: Metascore of the movie if available.
        """
        try:
            self.metascore = soup.select_one('.metacriticScore').text.replace(u'\xa0', u' ').strip()
        except:
            self.metascore = None

        """
        :returns: Storyline of the movie if available.
        """
        try:
            self.storyline = soup.select_one('.inline.canwrap').text.replace(u'\xa0', u' ').strip()
        except:
            self.storyline = None

        """
        :returns: Summary/Synopsis of the story if available.
        """
        try:
            self.summary = soup.select_one('.summary_text').text.strip()
        except:
            self.summary = None

        """
        :returns: Budget of the movie if available.
        """
        try:
            self.budget = soup.find('h4', string='Budget:').nextSibling.replace(u'\xa0', u' ').strip()
        except:
            self.budget = None

        """
        :returns: Opening Weekend USA of the movie if available.
        """
        try:
            self.opening_weekend_usa = soup.find('h4', string='Opening Weekend USA:').nextSibling.replace(u'\xa0', u' ').strip()
        except:
            self.opening_weekend_usa = None

        """
        :returns: Gross USA of the movie if available.
        """
        try:
            self.gross_usa = soup.find('h4', string='Gross USA:').nextSibling.replace(u'\xa0', u' ').strip()
        except:
            self.gross_usa = None

        """
        :returns: Cumulative Worldwide Gross of the movie if available.
        """
        try:
            self.cumulative_worldwide_gross = soup.find('h4', string='Cumulative Worldwide Gross:').nextSibling.replace(u'\xa0', u' ').strip()
        except:
            self.cumulative_worldwide_gross = None

        """
        :returns: Movie Poster URL if available.
        """
        try:
            self.movie_poster_url = 'https://www.imdb.com'+ soup.select_one('.poster').a['href']
        except:
            self.movie_poster_url = None

        """
        :returns: Movie Released Year if available.
        """
        try:
            self.movie_release_year = soup.select_one('span[id="titleYear"]').a.text.strip()
        except:
            self.movie_release_year = None

        """
        :returns: Creates Meta Data from the above info. if available.
        """
        try:
            self.imdb_movie_metadata = {"Movie Name" : self.title,
                                  "Title ID" : self.titleid,
                                  "Rating" : self.rating,
                                  "IMDb Votes" : self.imdb_votes,
                                  "Genre" : self.genre,
                                  "Year" : self.movie_release_year,
                                  "Metascore" : self.metascore,
                                  "Movie Poster URL" : self.movie_poster_url,
                                  "Budget" : self.budget,
                                  "Opening Weekend USA" : self.opening_weekend_usa,
                                  "Cumulative Worldwide Gross" : self.cumulative_worldwide_gross,
                                  "Gross USA" : self.gross_usa,
                                  "Storyline" : self.storyline,
                                  "Summary" : self.summary,
                                  "Movie URL" : self.movie_url}
        except:
            self.imdb_movie_metadata = None

        end = time.time()
        sys.stdout.write('\r' + str("Time taken for extracting basic movie info") + " : " + str(round(end - start)) + " " + str("seconds") + '\r')
        sys.stdout.flush()

# Retrieves IMDb Full Cast & Crew Details
class cast_and_crew:

    """
    Collects full cast & crew details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """
    def __init__(self, titleid):
        start = time.time()
        self.titleid = titleid
        self.cast_and_crew_url = "https://www.imdb.com/title/" + self.titleid + "/fullcredits"
        soup = BeautifulSoup(get(self.cast_and_crew_url).text, 'lxml')

        """
        returns: Movie Title
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None


        """
        returns: Writtern Credits DataFrame
        """
        try:
            w_index = [i for i in range(len(soup.select('h4'))) if 'writing' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            writer = soup.select('h4')[w_index].findNext('table').select('tr')
            self.writers_df = pd.DataFrame(columns=['Name', 'Credit', 'ID'])

            for index, i in enumerate(range(len(writer))):
                try:
                    self.writers_df.loc[len(self.writers_df)] = [writer[i].select_one('td.name').a.text.strip(),
                                                                 writer[i].select_one('td.credit').text.strip(),
                                                                 writer[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
                sys.stdout.write('\r' + "Writers for " + str(self.title) + " : " + str(index) + '\r')
                sys.stdout.flush()
        except:
            self.writers_df = None

        """
        returns: Writers list
        """
        try:
            self.writers = self.writers_df.Name.tolist()
        except:
            self.writers = None

        """
        returns: Writers ID list
        """
        try:
            self.writers_id = self.writers_df.ID.tolist()
        except:
            self.writers_id = None

        """
        returns: Writers Credit list
        """
        try:
            self.writers_credit = self.writers_df.Credit.tolist()
        except:
            self.writers_credit = None

        """
        returns: Directed_by DataFrame
        """
        try:
            d_index = [i for i in range(len(soup.select('h4'))) if 'directed' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            director = soup.select('h4')[d_index].findNext('table').select('tr')
            self.directors_df = pd.DataFrame(columns=['Name', 'ID'])

            for index, i in enumerate(range(len(director))):
                try:
                    self.directors_df.loc[len(self.directors_df)] = [director[i].select_one('td.name').a.text.strip(),
                                                                     director[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
                sys.stdout.write('\r' + "Directors for " + str(self.title) + " : " + str(index) + '\r')
                sys.stdout.flush()
        except:
            self.directors_df = None

        """
        returns: Directors list
        """
        try:
            self.directors = self.directors_df.Name.tolist()
        except:
            self.directors = None

        """
        returns: Directors ID list
        """
        try:
            self.directors_id = self.directors_df.ID.tolist()
        except:
            self.directors_id = None

        """
        returns: Produced_by DataFrame
        """
        try:
            p_index = [i for i in range(len(soup.select('h4'))) if 'produced' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            producer = soup.select('h4')[p_index].findNext('table').select('tr')
            self.producers_df = pd.DataFrame(columns=['Name', 'Credit', 'ID'])

            for index, i in enumerate(range(len(producer))):
                try:
                    self.producers_df.loc[len(self.producers_df)] = [producer[i].select_one('td.name').a.text.strip(),
                                                                     producer[i].select_one('td.credit').text.strip(),
                                                                     producer[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
                sys.stdout.write('\r' + "Producers for " + str(self.title) + " : " + str(index) + '\r')
                sys.stdout.flush()
        except:
            self.producers_df = None

        """
        returns: Producers list
        """
        try:
            self.producers = self.producers_df.Name.tolist()
        except:
            self.producers = None

        """
        returns: Producers ID list
        """
        try:
            self.producers_id = self.producers_df.ID.tolist()
        except:
            self.producers_id = None

        """
        returns: Producers Credit list
        """
        try:
            self.producers_credit = self.producers_df.Credit.tolist()
        except:
            self.producers_credit = None

        """
        returns: Cast DataFrame
        """
        try:
            c_index = [i for i in range(len(soup.select('h4'))) if 'cast' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            casting = soup.select('h4')[c_index].findNext('table').select('tr')
            self.cast_df = pd.DataFrame(columns=['Name', 'Image', 'Character', 'ID'])

            for index, i in enumerate(range(len(casting))):
                try:
                    self.cast_df.loc[len(self.cast_df)] = [casting[i].select_one('td.primary_photo').a.img['title'].strip(),
                                                           casting[i].select_one('td.primary_photo').a.img['src'].strip(),
                                                           ' '.join(casting[i].select_one('td.character').text.split()).strip(),
                                                           casting[i].select_one('td.primary_photo').a['href'][6:15].strip()]
                except:
                    pass
                sys.stdout.write('\r' + "Casting for " + str(self.title) + " : " + str(index) + '\r')
                sys.stdout.flush()
        except:
            self.cast_df = None

        """
        returns: Cast list
        """
        try:
            self.cast = self.cast_df.Name.tolist()
        except:
            self.cast = None

        """
        returns: Cast ID list
        """
        try:
            self.cast_id = self.cast_df.ID.tolist()
        except:
            self.cast_id = None

        """
        returns: Cast Character/Role list
        """
        try:
            self.cast_character = self.cast_df.Character.tolist()
        except:
            self.cast_character = None

        """
        returns: Cast Image URL list
        """
        try:
            self.cast_character_img_url = self.cast_df.Image.tolist()
        except:
            self.cast_character_img_url = None

        """
        returns: Music by DataFrame
        """
        try:
            m_index = [i for i in range(len(soup.select('h4'))) if 'music' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            music = soup.select('h4')[m_index].findNext('table').select('tr')
            self.music_df = pd.DataFrame(columns=['Name', 'ID'])

            for index, i in enumerate(range(len(music))):
                try:
                    self.music_df.loc[len(self.music_df)] = [music[i].select_one('td.name').a.text.strip(),
                                                             music[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
                sys.stdout.write('\r' + "Music for " + str(self.title) + " : " + str(index) + '\r')
                sys.stdout.flush()
        except:
            self.music_df = None

        """
        returns: Music by list
        """
        try:
            self.music = self.music_df.Name.tolist()
        except:
            self.music = None

        """
        returns: Music by ID list
        """
        try:
            self.music_id = self.music_df.ID.tolist()
        except:
            self.music_id = None

        """
        returns: Cinematography by DataFrame
        """
        try:
            ct_index = [i for i in range(len(soup.select('h4'))) if 'cinematography' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            cinematography = soup.select('h4')[ct_index].findNext('table').select('tr')
            self.cinematography_df = pd.DataFrame(columns=['Name', 'ID'])

            for index, i in enumerate(range(len(cinematography))):
                try:
                    self.cinematography_df.loc[len(self.cinematography_df)] = [cinematography[i].select_one('td.name').a.text.strip(),
                                                                               cinematography[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
                sys.stdout.write('\r' + "Cinematography for " + str(self.title) + " : " + str(index) + '\r')
                sys.stdout.flush()
        except:
            self.cinematography_df = None

        """
        returns: Cinematography by list
        """
        try:
            self.cinematography = self.cinematography_df.Name.tolist()
        except:
            self.cinematography = None

        """
        returns: Cinematography by ID list
        """
        try:
            self.cinematography_id = self.cinematography_df.ID.tolist()
        except:
            self.cinematography_id = None

        """
        returns: Production Design by DataFrame
        """
        try:
            pd_index = [i for i in range(len(soup.select('h4'))) if 'production design' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            production_designer = soup.select('h4')[pd_index].findNext('table').select('tr')
            self.production_designer_df = pd.DataFrame(columns=['Name', 'ID'])

            for index, i in enumerate(range(len(production_designer))):
                try:
                    self.production_designer_df.loc[len(self.production_designer_df)] = [production_designer[i].select_one('td.name').a.text.strip(),
                                                                                         production_designer[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
                sys.stdout.write('\r' + "Production Designer for " + str(self.title) + " : " + str(index) + '\r')
                sys.stdout.flush()
        except:
            self.cinematography_df = None

        """
        returns: Production Design by list
        """
        try:
            self.production_designer = self.production_designer_df.Name.tolist()
        except:
            self.production_designer = None

        """
        returns: Production Design by ID list
        """
        try:
            self.production_designer_id = self.production_designer_df.ID.tolist()
        except:
            self.production_designer_id = None

        """
        returns: Film Editing by  DataFrame
        """
        try:
            fe_index = [i for i in range(len(soup.select('h4'))) if 'film editing' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            film_editing = soup.select('h4')[fe_index].findNext('table').select('tr')
            self.film_editing_df = pd.DataFrame(columns=['Name', 'Credit', 'ID'])

            for index, i in enumerate(range(len(film_editing))):
                try:
                    self.film_editing_df.loc[len(self.film_editing_df)] = [film_editing[i].select_one('td.name').a.text.strip(),
                                                                     film_editing[i].select_one('td.credit').text.strip(),
                                                                     film_editing[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
                sys.stdout.write('\r' + "Film Editing for " + str(self.title) + " : " + str(index) + '\r')
                sys.stdout.flush()
        except:
            self.film_editing_df = None

        """
        returns: Film Editing list
        """
        try:
            self.film_editing = self.film_editing_df.Name.tolist()
        except:
            self.film_editing = None

        """
        returns: Film Editing ID list
        """
        try:
            self.film_editing_id = self.film_editing_df.ID.tolist()
        except:
            self.film_editing_id = None

        """
        returns: Film Editing Credit list
        """
        try:
            self.film_editing_credit = self.film_editing_df.Credit.tolist()
        except:
            self.film_editing_credit = None

        """
        returns: Casting by  DataFrame
        """
        try:
            cg_index = [i for i in range(len(soup.select('h4'))) if 'casting' in  ' '.join(soup.select('h4')[i].text.split()).lower()][0]
            casting_d = soup.select('h4')[cg_index].findNext('table').select('tr')
            self.casting_df = pd.DataFrame(columns=['Name', 'Credit', 'ID'])

            for index, i in enumerate(range(len(casting_d))):
                try:
                    self.casting_df.loc[len(self.casting_df)] = [casting_d[i].select_one('td.name').a.text.strip(),
                                                                     casting_d[i].select_one('td.credit').text.strip(),
                                                                     casting_d[i].select_one('td.name').a['href'][6:15].strip()]
                except:
                    pass
                sys.stdout.write('\r' + "Film Editing for " + str(self.title) + " : " + str(index) + '\r')
                sys.stdout.flush()
        except:
            self.casting_df = None

        """
        returns: Casting list
        """
        try:
            self.casting = self.casting_df.Name.tolist()
        except:
            self.casting = None

        """
        returns: Casting ID list
        """
        try:
            self.casting_id = self.casting_df.ID.tolist()
        except:
            self.casting_id = None

        """
        returns: Casting Credit list
        """
        try:
            self.casting_credit = self.casting_df.Credit.tolist()
        except:
            self.casting_credit = None


        """
        returns: Creates Dict from the above info. if available.
        """
        try:
            self.imdb_cast_metadata = {"Movie Name" : self.title,
                                       "Title ID" : self.titleid,
                                       "Movie URL" : self.cast_and_crew_url,
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

        end = time.time()
        sys.stdout.write('\r' + str("Time taken for extracting cast & crew info") + " : " + str(round(end - start)) + " " + str("seconds") + '\r')
        sys.stdout.flush()

class plot:

    """
    Collects IMDb Plot Details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, titleid):
        start = time.time()
        self.titleid = titleid
        self.plot_url = "https://www.imdb.com/title/" + self.titleid + "/plotsummary"
        soup = BeautifulSoup(get(self.plot_url).text, 'lxml')

        """
        returns: Movie Title
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        """
        returns: Movie Plot
        """
        try:
            self.plot = ' '.join(soup.select_one('#synopsis').findNext('ul').text.split()).replace("\'", " ")
        except:
            self.plot = None

        """
        returns: Movies Summaries
        """
        try:
            block = soup.select_one('#summaries').findNext('ul').select('li')
            self.summaries = [' '.join(block[i].text.split()) for i in range(len(block))]
        except:
            self.summaries = None

        """
        returns: Creates Dict from the above info. if available.
        """
        try:
            self.imdb_plot_metadata = {"Movie Name" : self.title,
                                       "Title ID" : self.titleid,
                                       "Movie URL" : self.plot_url,
                                       "Plot" : self.plot,
                                       "Summaries" : self.summaries}
        except:
            self.imdb_plot_metadata = None

        end = time.time()
        sys.stdout.write('\r' + str("Time taken for extracting plot info") + " : " + str(round(end - start)) + " " + str("seconds") + '\r')
        sys.stdout.flush()

# Retrieves IMDb Plot Keywords Details
class plot_keywords:

    """
    Collects IMDb Plot Keywords Details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, titleid):
        start = time.time()
        self.titleid = titleid
        self.plot_keywords_url = "https://www.imdb.com/title/" + self.titleid + "/keywords"
        soup = BeautifulSoup(get(self.plot_keywords_url).text, 'lxml')

        """
        returns: Movie Title
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        """
        returns: Movie Plot Keywords
        """
        try:
            block = soup.select('td.soda')
            self.plot_keywords = [block[i]['data-item-keyword'] for i in range(len(block))]
        except:
            self.plot_keywords = None

        """
        returns: Creates Dict from the above info. if available.
        """
        try:
            self.imdb_plot_Keywords_metadata = {"Movie Name" : self.title,
                                       "Title ID" : self.titleid,
                                       "Movie URL" : self.plot_keywords_url,
                                       "Plot Keywords" : self.plot_keywords}
        except:
            self.imdb_plot_Keywords_metadata = None

        end = time.time()
        sys.stdout.write('\r' + str("Time taken for extracting plot Keywords info") + " : " + str(round(end - start)) + " " + str("seconds") + '\r')
        sys.stdout.flush()

# Retrieves IMDb Company Credits Details
class company:

    """
    Collects Company Credits details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """
    def __init__(self, titleid):
        start = time.time()
        self.titleid = titleid
        self.company_url = "https://www.imdb.com/title/" + self.titleid + "/companycredits"
        soup = BeautifulSoup(get(self.company_url).text, 'lxml')

        """
        returns: Movie Title
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None


        """
        returns: Production Company Credits DataFrame
        """
        try:
            production_company = soup.select_one('#production').findNext('ul').select('li')
            self.production_company_df = pd.DataFrame(columns=['Name', 'ID'])

            for index, i in enumerate(range(len(production_company))):
                try:
                    self.production_company_df.loc[len(self.production_company_df)] = [production_company[i].a.text.strip(),
                                                                                       production_company[i].a['href'][9:].strip()]
                except:
                    pass
                sys.stdout.write('\r' + "Production Company for " + str(self.title) + " : " + str(index) + '\r')
                sys.stdout.flush()
        except:
            self.production_company_df = None

        """
        returns: Distributors DataFrame
        """
        try:
            distributors = soup.select_one('#distributors').findNext('ul').select('li')
            self.distributors_df = pd.DataFrame(columns=['Name', 'ID'])

            for index, i in enumerate(range(len(distributors))):
                try:
                    self.distributors_df.loc[len(self.distributors_df)] = [distributors[i].a.text.strip(),
                                                                           distributors[i].a['href'][9:].strip()]
                except:
                    pass
                sys.stdout.write('\r' + "Distributors for " + str(self.title) + " : " + str(index) + '\r')
                sys.stdout.flush()
        except:
            self.distributors_df = None

        """
        returns: Special Effects DataFrame
        """
        try:
            special_effects = soup.select_one('#specialEffects').findNext('ul').select('li')
            self.specials_effects_df = pd.DataFrame(columns=['Name', 'ID'])

            for index, i in enumerate(range(len(special_effects))):
                try:
                    self.specials_effects_df.loc[len(self.specials_effects_df)] = [special_effects[i].a.text.strip(),
                                                                                   special_effects[i].a['href'][9:].strip()]
                except:
                    pass
                sys.stdout.write('\r' + "Specials Effects for " + str(self.title) + " : " + str(index) + '\r')
                sys.stdout.flush()
        except:
            self.specials_effects_df = None

        """
        returns: Other Companies DataFrame
        """
        try:
            other_companies = soup.select_one('#other').findNext('ul').select('li')
            self.other_companies_df = pd.DataFrame(columns=['Name', 'ID'])

            for index, i in enumerate(range(len(other_companies))):
                try:
                    self.other_companies_df.loc[len(self.other_companies_df)] = [other_companies[i].a.text.strip(),
                                                                                  other_companies[i].a['href'][9:].strip()]
                except:
                    pass
                sys.stdout.write('\r' + "Other Companies for " + str(self.title) + " : " + str(index) + '\r')
                sys.stdout.flush()
        except:
            self.other_companies_df = None

        end = time.time()
        sys.stdout.write('\r' + str("Time taken for extracting company credits info") + " : " + str(round(end - start)) + " " + str("seconds") + '\r')
        sys.stdout.flush()

# Retrieves IMDb Parental Guide Details
class parental_guide:

    """
    Collects IMDb Parental Guide Details of the multi-media content in IMDb when titleid is given.
    :param titleid: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, titleid):
        start = time.time()
        self.titleid = titleid
        self.parental_guide_url = "https://www.imdb.com/title/" + self.titleid + "/parentalguide"
        soup = BeautifulSoup(get(self.parental_guide_url).text, 'lxml')

        """
        returns: Movie Title
        """
        try:
            self.title = soup.select_one('h3[itemprop="name"]').a.text.strip()
        except:
            self.title = None

        """
        returns: Certificate DataFrame if available.
        """
        try:
            certificate = soup.select_one('#certificates').select('tr')
            self.certificates_df = pd.DataFrame(columns=['Name', 'Type'])

            for index, i in enumerate(range(len(certificate))):
                try:
                    self.certificates_df.loc[len(self.certificates_df)] = [certificate[i].select_one('td.ipl-zebra-list__label').text.strip(),
                                                               ' '.join(certificate[i].select_one('td').findNext('td').text.split())]
                except:
                    pass
                sys.stdout.write('\r' + "Writers for " + str(self.title) + " : " + str(index) + '\r')
        except:
            self.certificates_df = None

        """
        returns: Certificate Name if available.
        """
        try:
            self.certificates_name = self.certificates_df.Name.tolist()
        except:
            self.certificates_name = None

        """
        returns: Certificate Type if available.
        """
        try:
            self.certificates_type = self.certificates_df.Type.tolist()
        except:
            self.certificates_type = None

        """
        returns: Adivsory Nudity status if available.
        """
        try:
            advisory_nudity = soup.select_one('#advisory-nudity').select('li.ipl-zebra-list__item')
            self.adivsory_nudity_status = str(soup.select_one('#advisory-nudity').select_one('.ipl-status-pill').text.strip()) + " : " + str(soup.select_one('#advisory-nudity').select_one('.advisory-severity-vote__message').text.strip())
        except:
            self.adivsory_nudity_status = None

        """
        returns: Advisory Nudity Severity Vote if available.
        """
        try:
            advisory_nudity = soup.select_one('#advisory-nudity').select('li.ipl-zebra-list__item')
            self.advisory_nudity_severity_vote = [' '.join(advisory_nudity[i].text.split()).replace("\'", "") for i in range(len(advisory_nudity))]
        except:
            self.advisory_nudity_severity_vote = None

        """
        returns: Adivsory Violence status if available.
        """
        try:
            advisory_violence = soup.select_one('#advisory-violence').select('li.ipl-zebra-list__item')
            self.advisory_violence_status = str(soup.select_one('#advisory-violence').select_one('.ipl-status-pill').text.strip()) + " : " + str(soup.select_one('#advisory-violence').select_one('.advisory-severity-vote__message').text.strip())
        except:
            self.advisory_violence_status = None

        """
        returns: Advisory Violence Severity Vote if available.
        """
        try:
            advisory_violence = soup.select_one('#advisory-violence').select('li.ipl-zebra-list__item')
            self.advisory_violence_severity_vote = [' '.join(advisory_violence[i].text.split()).replace("\'", "") for i in range(len(advisory_violence))]
        except:
            self.advisory_violence_severity_vote = None

        """
        returns: Adivsory Profanity status if available.
        """
        try:
            advisory_profanity = soup.select_one('#advisory-profanity').select('li.ipl-zebra-list__item')
            self.advisory_profanity_status = str(soup.select_one('#advisory-profanity').select_one('.ipl-status-pill').text.strip()) + " : " + str(soup.select_one('#advisory-profanity').select_one('.advisory-severity-vote__message').text.strip())
        except:
            self.advisory_profanity_status = None

        """
        returns: Advisory Profanity Severity Vote if available.
        """
        try:
            advisory_profanity = soup.select_one('#advisory-profanity').select('li.ipl-zebra-list__item')
            self.advisory_profanity_severity_vote = [' '.join(advisory_profanity[i].text.split()).replace("\'", "") for i in range(len(advisory_profanity))]
        except:
            self.advisory_profanity_severity_vote = None

        """
        returns: Adivsory Alcohol status if available.
        """
        try:
            advisory_alcohol = soup.select_one('#advisory-alcohol').select('li.ipl-zebra-list__item')
            self.advisory_alcohol_status = str(soup.select_one('#advisory-alcohol').select_one('.ipl-status-pill').text.strip()) + " : " + str(soup.select_one('#advisory-alcohol').select_one('.advisory-severity-vote__message').text.strip())
        except:
            self.advisory_alcohol_status = None

        """
        returns: Advisory Alcohol Severity Vote if available.
        """
        try:
            advisory_alcohol = soup.select_one('#advisory-alcohol').select('li.ipl-zebra-list__item')
            self.advisory_alcohol_severity_vote = [' '.join(advisory_alcohol[i].text.split()).replace("\'", "") for i in range(len(advisory_alcohol))]
        except:
            self.advisory_alcohol_severity_vote = None

        """
        returns: Adivsory Frightening status if available.
        """
        try:
            advisory_frightening = soup.select_one('#advisory-frightening').select('li.ipl-zebra-list__item')
            self.advisory_frightening_status = str(soup.select_one('#advisory-frightening').select_one('.ipl-status-pill').text.strip()) + " : " + str(soup.select_one('#advisory-frightening').select_one('.advisory-severity-vote__message').text.strip())
        except:
            self.advisory_frightening_status = None

        """
        returns: Advisory Frightening Severity Vote if available.
        """
        try:
            advisory_frightening = soup.select_one('#advisory-frightening').select('li.ipl-zebra-list__item')
            self.advisory_frightening_severity_vote = [' '.join(advisory_frightening[i].text.split()).replace("\'", "") for i in range(len(advisory_frightening))]
        except:
            self.advisory_frightening_severity_vote = None

        """
        returns: Spoilers Violence & Gore if available.
        """
        try:
            spoiler_violence = soup.select_one('#advisory-spoilers').select_one('#advisory-spoiler-violence').select('li.ipl-zebra-list__item')
            self.spoiler_violence = [' '.join(spoiler_violence[i].contents[0].split()) for i in range(len(spoiler_violence))]
        except:
            self.spoiler_violence = None

        """
        returns: Spoilers Alcohol, Drugs & Smoking if available.
        """
        try:
            spoiler_alcohol = soup.select_one('#advisory-spoilers').select_one('#advisory-spoiler-alcohol').select('li.ipl-zebra-list__item')
            self.spoiler_alcohol = [' '.join(spoiler_alcohol[i].contents[0].split()) for i in range(len(spoiler_alcohol))]
        except:
            self.spoiler_alcohol = None

        """
        returns: Spoilers Frightening & Intense Scenes if available.
        """
        try:
            spoiler_frightening = soup.select_one('#advisory-spoilers').select_one('#advisory-spoiler-frightening').select('li.ipl-zebra-list__item')
            self.spoiler_frightening = [' '.join(spoiler_frightening[i].contents[0].split()) for i in range(len(spoiler_frightening))]
        except:
            self.spoiler_frightening = None

        """
        returns: Creates Dict from the above info. if available.
        """
        try:
            self.imdb_parental_guide_metadata = {"Movie Name" : self.title,
                                                 "Title ID" : self.titleid,
                                                 "Movie URL" : self.parental_guide_url,
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

        end = time.time()
        sys.stdout.write('\r' + str("Time taken for execution parental guide info") + " : " + str(round(end - start)) + " " + str("seconds") + '\r')
        sys.stdout.flush()

class imdb:
      def __init__(self, titleid):
        movie.__init__(self, titleid)
        plot.__init__(self, titleid)
        plot_keywords.__init__(self, titleid)
        parental_guide.__init__(self, titleid)
        company.__init__(self, titleid)
        cast_and_crew.__init__(self, titleid)
