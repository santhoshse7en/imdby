from imdby.utils.config import base_uri, imdb_uris, tag_search
from imdby.utils.helpers import (catch, catch_dict, catch_list,
                                     cast_non_credit, full_cast, unicode, cast_credit)
from imdby.utils.utils import BeautifulSoup, get, pd, re


# Retrieves IMDb Full Cast & Crew Details
class full_cast_and_crew:

    """
    Collects full cast & crew details of the multi-media content in IMDb when title_id is given.
    :param title_id: Unique identification for every multimedia in IMdb.
    :returns:   1. Directed by
                2. Writtern by
                3. Cast and Crew Details
                4. Cinematography
                5. Producer
                6. Production Designer
                7. Flim Editing
                8. Music
                9. Casting
    """

    def __init__(self, title_id: str) -> bool:
        self.title_id = title_id
        self.full_cast_and_crew_uri = imdb_uris["fullcredits"] % self.title_id

        soup = BeautifulSoup(get(self.full_cast_and_crew_uri).text, 'lxml')

        """
        :returns: table tag index
        """
        table_tag = soup.select('h4')

        """
        :returns: Movie Title
        """
        movie_tag = soup.select_one('h3[itemprop="name"]')
        self.title = catch_list(lambda: unicode(movie_tag.a.get_text()))
        self.title_url = catch_list(lambda: unicode(
            '%s%s' % (base_uri, movie_tag.a['href'][1:])))
        self.year = catch(lambda: int(re.findall(
            r"\d+", unicode(movie_tag.select_one('.nobr').get_text()))[0]))

        """
        :returns: Writtern Credits DataFrame
        """
        self.writers_df = catch(
            lambda: cast_credit(tag_search['writer'], table_tag))
        self.writers_name = catch_list(lambda: self.writers_df.Name.tolist())
        self.writers_id = catch_list(lambda: self.writers_df.ID.tolist())
        self.writers_uri = catch_list(lambda: self.writers_df.URI.tolist())
        self.writers_credit = catch_list(
            lambda: self.writers_df.Credit.tolist())

        """
        :returns: Directed_by DataFrame
        """
        self.directors_df = catch(
            lambda: cast_non_credit(tag_search['director'], table_tag))
        self.directors_name = catch_list(
            lambda: self.directors_df.Name.tolist())
        self.directors_id = catch_list(lambda: self.directors_df.ID.tolist())
        self.directors_uri = catch_list(lambda: self.directors_df.URI.tolist())

        """
        :returns: Produced_by DataFrame
        """
        self.producers_df = catch(
            lambda: cast_non_credit(tag_search['producer'], table_tag))
        self.producers_name = catch_list(
            lambda: self.producers_df.Name.tolist())
        self.producers_id = catch_list(lambda: self.producers_df.ID.tolist())
        self.producers_credit = catch_list(
            lambda: self.producers_df.Credit.tolist())
        self.producers_uri = catch_list(lambda: self.producers_df.URI.tolist())

        """
        :returns: Cast DataFrame
        """
        self.cast_df = catch(lambda: full_cast(tag_search['cast'], table_tag))
        self.cast_name = catch_list(lambda: self.cast_df.Name.tolist())
        self.cast_id = catch_list(lambda: self.cast_df.Name_ID.tolist())
        self.cast_uri = catch_list(lambda: self.cast_df.Name_URI.tolist())
        self.cast_image_uri = catch_list(lambda: self.cast_df.Image.tolist())
        self.cast_character = catch_list(
            lambda: self.cast_df.Character_Name.tolist())
        self.cast_character_id = catch_list(
            lambda: self.cast_df.Character_ID.tolist())
        self.cast_character_uri = catch_list(
            lambda: self.cast_df.Character_URI.tolist())

        """
        :returns: Music by DataFrame
        """
        self.music_df = catch(lambda: cast_non_credit(
            tag_search['music'], table_tag))
        self.music_name = catch_list(lambda: self.music_df.Name.tolist())
        self.music_id = catch_list(lambda: self.music_df.ID.tolist())
        self.music_uri = catch_list(lambda: self.music_df.URI.tolist())

        """
        :returns: Cinematography by DataFrame
        """
        self.cinematography_df = catch(lambda: cast_non_credit(
            tag_search['cinematography'], table_tag))
        self.cinematography_name = catch_list(
            lambda: self.cinematography_df.Name.tolist())
        self.cinematography_id = catch_list(
            lambda: self.cinematography_df.ID.tolist())
        self.cinematography_uri = catch_list(
            lambda: self.cinematography_df.URI.tolist())

        """
        :returns: Production Design by DataFrame
        """
        self.production_designer_df = catch(lambda: cast_non_credit(
            tag_search['production design'], table_tag))
        self.production_designer_name = catch_list(
            lambda: self.production_designer_df.Name.tolist())
        self.production_designer_id = catch_list(
            lambda: self.production_designer_df.ID.tolist())
        self.production_designer_uri = catch_list(
            lambda: self.production_designer_df.URI.tolist())

        """
        :returns: Film Editing by  DataFrame
        """
        self.film_editing_df = catch(lambda: cast_credit(
            tag_search['film editing'], table_tag))
        self.film_editing_name = catch_list(
            lambda: self.film_editing_df.Name.tolist())
        self.film_editing_id = catch_list(
            lambda: self.film_editing_df.ID.tolist())
        self.film_editing_credit = catch_list(
            lambda: self.film_editing_df.Credit.tolist())
        self.film_editing_uri = catch_list(
            lambda: self.film_editing_df.URI.tolist())

        """
        :returns: Casting by  DataFrame
        """
        self.casting_df = catch_list(
            lambda: cast_credit(tag_search['casting'], table_tag))
        self.casting_name = catch_list(lambda: self.casting_df.Name.tolist())
        self.casting_id = catch_list(lambda: self.casting_df.ID.tolist())
        self.casting_credit = catch_list(
            lambda: self.casting_df.Credit.tolist())
        self.casting_uri = catch_list(lambda: self.casting_df.URI.tolist())

        """
        :returns: Creates Dict from the above info. if available.
        """
        self.imdb_full_cast_and_crew_metadata = catch_dict(lambda: {"Movie Name": self.title,
                                                                    "Movie URL": self.title_url,
                                                                    "Title ID": self.title_id,
                                                                    "Year": self.year,
                                                                    "Movie Full Cast and Crew URI": self.full_cast_and_crew_uri,
                                                                    "Director": {"Name": self.directors_name,
                                                                                 "ID": self.directors_id,
                                                                                 "URI": self.directors_uri},
                                                                    "Writer": {"Name": self.writers_name,
                                                                               "Credit": self.writers_credit,
                                                                               "ID": self.writers_id,
                                                                               "URI": self.writers_uri},
                                                                    "Cast": {"Name": self.cast_name,
                                                                             "Name ID": self.cast_id,
                                                                             "Name URI": self.cast_uri,
                                                                             "Image": self.cast_image_uri,
                                                                             "Character Name": self.cast_character,
                                                                             "Characte ID": self.cast_character_id,
                                                                             "Characte URI": self.cast_character_uri},
                                                                    "Producer": {"Name": self.producers_name,
                                                                                 "Credit": self.producers_credit,
                                                                                 "ID": self.producers_id,
                                                                                 "URI": self.producers_uri},
                                                                    "Music": {"Name": self.music_name,
                                                                              "ID": self.music_id,
                                                                              "URI": self.music_uri},
                                                                    "Cinematography": {"Name": self.cinematography_name,
                                                                                       "ID": self.cinematography_id,
                                                                                       "URI": self.cinematography_uri},
                                                                    "Production Desing": {"Name": self.production_designer_name,
                                                                                          "ID": self.production_designer_id,
                                                                                          "URI": self.production_designer_uri},
                                                                    "Flim Editing": {"Name": self.film_editing_name,
                                                                                     "Credit": self.film_editing_credit,
                                                                                     "ID": self.film_editing_id,
                                                                                     "URI": self.film_editing_uri},
                                                                    "Casting": {"Name": self.casting_name,
                                                                                "Credit": self.casting_credit,
                                                                                "ID": self.casting_id,
                                                                                "URI": self.casting_uri}})
