# This module handles the reading and writing of a pkl binary file where the data queried in My anime list is copied so
# as not to perform repeated HTML queries
import pickle
from html_reader import add_data_anime


def pkl_manager(dataframe):
    try:
        with open("MAL_local_data.pkl", "rb") as MAL_data:
            return pickle.load(MAL_data)
    except FileNotFoundError:
        with open("MAL_local_data.pkl", "wb") as MAL_data:
            data = {}
            for id_anime in dataframe['series_animedb_id'].to_numpy().tolist():
                data[id_anime[0]] = add_data_anime(id_anime[0])
            pickle.dump(data, MAL_data)
            return data
