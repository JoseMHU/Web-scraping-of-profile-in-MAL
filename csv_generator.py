# This module is responsible for generating CSV files from the data
# 3 CSV files are generated:
# 1. The main file with most of the data
# 2. A file that uniquely lists each of the possible genres for an anime.
# 3. A relational file that links the id of the animes with the id of the available genres.
import pandas as pd
from pathlib import Path


def csv_generator(dataframe, pkl_data):
    """
    Main function of the module that is responsible for processing the data to load the main CSV file and call the
    other functions that create the rest of the CSV files
    :param dataframe: dataframe generated from XML file read
    :param pkl_data: Data extracted from the pkl_manager module
    :return: Nothing
    """
    pkl_data_extraction = {
        "ID": [],
        "Status": [],
        "Aired": [],
        "Premiered": [],
        "Studios": [],
        "Genre": []
    }
    for id_anime in pkl_data:
        pkl_data_extraction["ID"].append(id_anime)
        for column_data in list(pkl_data_extraction.keys())[1:]:
            pkl_data_extraction[column_data].append(pkl_data[id_anime][column_data])

    for column_data in list(pkl_data_extraction.keys())[1:5]:
        dataframe[column_data] = pkl_data_extraction[column_data]

    try:
        # 1. We create the main file with most of the data
        dataframe.to_csv(f"{Path.home()}\\Desktop\\Main_table.csv", index=False)
    except PermissionError:
        print("Write permissions denied. Close the CSV file so the program can modify it, or move it to another path "
              "so the program can generate another.")

    serie_genre = genre_table_builder(pkl_data_extraction["Genre"])

    relational_table_builder(pkl_data_extraction, serie_genre)


def genre_table_builder(raw_genre_list):
    """
    Function that reads the anime genres and creates a series with the unique values of these to store them in CSV
    format.
    :param raw_genre_list: List of lists with the genres of each anime
    :return: The series with unique genres
    """
    genre_list = []
    unique_genre_list = []
    for items in raw_genre_list:
        for item in items:
            genre_list.append(item)
    [unique_genre_list.append(genre) for genre in genre_list if genre not in unique_genre_list]
    s = pd.Series(unique_genre_list, dtype="string", name="Genres")
    try:
        # 2. We create a file that uniquely lists each of the possible genres for an anime.
        s.to_csv(f"{Path.home()}\\Desktop\\Genres_table.csv", index=True)
    except PermissionError:
        print("Write permissions denied. Close the CSV file so the program can modify it, or move it to another path "
              "so the program can generate another.")
    return s


def relational_table_builder(pkl_data_extraction, serie_genre):
    """
    Function that reads the anime genre series and the ID data of each anime to create a real dataframe where each
    anime ID is assigned the genre series index, creating the CSV file with these relationships at the end.
    :param pkl_data_extraction: Data grouped and extracted in lists from the data of the pkl_manager module
    :param serie_genre: The series with unique genres created by the genre_table_builder function
    :return: Nothing
    """
    df_dictionary = dict()
    df_dictionary["ID"] = []
    df_dictionary["Genre"] = []
    count = 0
    for genre_list in pkl_data_extraction["Genre"]:
        for genre in genre_list:
            df_dictionary["ID"].append(pkl_data_extraction["ID"][count])
            df_dictionary["Genre"].append(list(serie_genre).index(genre))
        count += 1
    df_relational = pd.DataFrame(df_dictionary)
    try:
        # 3. We create a relational file that links the id of the animes with the id of the available genres.
        df_relational.to_csv(f"{Path.home()}\\Desktop\\Relational_table.csv", index=True)
    except PermissionError:
        print("Write permissions denied. Close the CSV file so the program can modify it, or move it to another path "
              "so the program can generate another.")


if __name__ == "__main__":
    # Functionality test
    from xml_reader import xml_reader
    from pkl_manager import pkl_manager
    df = xml_reader("C:\\Users\\josep\\Desktop\\animelist_1681744650_-_8148940.xml")
    mal_data = pkl_manager(df, False)
    csv_generator(df, mal_data)
