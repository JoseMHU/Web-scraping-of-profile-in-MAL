# This module reads the content of the XML file
import xml.etree.ElementTree as Et
import pandas as pd


def xml_reader(path):
    """
    Function that will read the XML file from the path and create a dataframe with Pandas from the parameters:
            [
            series_animedb_id
            series_title
            series_type
            series_episodes
            my_score
            my_status
            ]
    :param path: XML file address
    :return: DataFrame of the processed XML file
    """
    xml_data = open(path, "r").read()
    root = Et.XML(xml_data)

    data = []
    cols = []
    for index, child in enumerate(root[1:]):
        if index == 1:
            cols.append([sub_child.tag for sub_child in child[0:4]])
            cols[0].append(child[9].tag)
            cols[0].append(child[12].tag)
        data.append([sub_child.text for sub_child in child[0:4]])
        data[len(data) - 1].append(child[9].text)
        data[len(data) - 1].append(child[12].text)

    df = pd.DataFrame(data)
    df.columns = cols
    # df.to_csv("Anime_list.csv", index=False)
    return df


if __name__ == "__main__":
    # Functionality test
    xml_reader("C:\\Users\\josep\\Desktop\\animelist_1681744650_-_8148940.xml")
