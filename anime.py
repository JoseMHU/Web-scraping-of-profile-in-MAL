# This module contains the anime class
class Anime:
    def __init__(self, id_list):
        self.id = id_list
        self.mal_base = {"Status": "",
                         "Aired": "",
                         "Premiered": "",
                         "Studios": "",
                         "Genres": ""}