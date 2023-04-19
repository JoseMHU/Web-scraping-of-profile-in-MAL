# This module handles the reading and writing of a pkl binary file where the data queried in My anime list is copied so
# as not to perform repeated HTML queries
import pickle
from main_files.html_reader import add_data_anime


def pkl_manager(dataframe, update):
    """
    This function is the main handler for reading and writing the pkl file.
    :param dataframe: dataframe generated from XML file read
    :param update: It is used to activate or deactivate the update of the data stored in the function pkl_data_update
    :return: Anime dictionary by ID with data dictionaries inside
    """
    try:
        with open("MAL_local_data.pkl", "rb") as MAL_data:
            old_data = pickle.load(MAL_data)
            if update:
                pkl_data_update()
            new_data = pkl_add_data(dataframe, old_data)
            return new_data
    except (EOFError, FileNotFoundError):
        with open("MAL_local_data.pkl", "wb") as MAL_data:
            data = {}
            print(f"Consulting: {len(dataframe['series_animedb_id'].to_numpy().tolist())} animes")
            for id_anime in dataframe['series_animedb_id'].to_numpy().tolist():
                data[id_anime[0]] = add_data_anime(id_anime[0])
                print(f"{len(data)}", end=",")
            pickle.dump(data, MAL_data)
            return data


def pkl_add_data(dataframe, old_data):
    """
    This function adds new animes to the pkl file if they are not registered by their ID in the pkl
    :param dataframe: dataframe generated from XML file read
    :param old_data: Data loaded from pkl file without modification
    :return: Data updated in dictionary by ID format with dictionaries by field
    """
    if len(dataframe['series_animedb_id'].to_numpy().tolist()) != len(old_data):
        print(f"Consulting: {len(dataframe['series_animedb_id'].to_numpy().tolist()) - len(old_data)} animes")
        count = 1
        for id_anime in dataframe['series_animedb_id'].to_numpy().tolist():
            if [id_anime[0]] not in list(old_data.keys()):
                print(f"{count}", end=",")
                old_data[id_anime[0]] = add_data_anime(id_anime[0])
                count += 1
        with open("MAL_local_data.pkl", "wb") as MAL_data:
            pickle.dump(old_data, MAL_data)
    return old_data


def pkl_data_update():
    """
    This function performs an HTML query of all animes whose registered status in the PKL is not finalized.
    This seeks to complete the fields that could be empty or update these after a new reading of an XML file
    with the data at the time it is on the MAL page.
    :return: Nothing
    """
    print("Updating local data:", end=" ")
    with open("MAL_local_data.pkl", "rb") as MAL_data:
        old_data = pickle.load(MAL_data)
        count = 1
        for keys in old_data:
            if old_data[keys]["Status"] != "Finished Airing":
                print(f"{count}", end=",")
                count += 1
                old_data[keys] = add_data_anime(keys)
    with open("MAL_local_data.pkl", "wb") as MAL_data:
        pickle.dump(old_data, MAL_data)


if __name__ == "__main__":
    # Functionality test
    from main_files.xml_reader import xml_reader
    df = xml_reader("C:\\Users\\josep\\Desktop\\animelist_1681744650_-_8148940.xml")
    pkl_manager(df, False)
