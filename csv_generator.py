# This module is responsible for generating CSV files from the data
# 3 CSV files are generated:
# 1. The main file with most of the data
# 2. A file that uniquely lists each of the possible genres for an anime.
# 3. A relational file that links the id of the animes with the id of the available genres.
import pandas as pd


def data_combination(dataframe, pkl_data):
    status = []
    aired = []
    premiered = []
    studios = []
    genre = []
    for id_anime in pkl_data:
        status.append(pkl_data[id_anime]["Status"])
        aired.append(pkl_data[id_anime]["Aired"])
        premiered.append(pkl_data[id_anime]["Premiered"])
        studios.append(pkl_data[id_anime]["Studios"])
        genre.append(pkl_data[id_anime]["Genre"])
    serie_genre = genre_table_builder(genre)


def genre_table_builder(raw_genre_list):
    genre_list = []
    unique_genre_list = []
    for items in raw_genre_list:
        for item in items:
            genre_list.append(item)
    [unique_genre_list.append(genre) for genre in genre_list if genre not in unique_genre_list]
    s = pd.Series(unique_genre_list, dtype="string", name="Genres")
    s.to_csv("Genres_table.csv", index=True)
    return s


if __name__ == "__main__":
    # Functionality test
    from xml_reader import xml_reader
    from pkl_manager import pkl_manager
    df = xml_reader("C:\\Users\\josep\\Desktop\\animelist_1681744650_-_8148940.xml")
    mal_data = pkl_manager(df, False)
    data_combination(df, mal_data)
