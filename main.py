# MAIN FILE

from gui import Gui
from xml_reader import xml_reader
from pkl_manager import pkl_manager
from csv_generator import data_combination


def main(update=True):
    """
    Main function of the project
    :param update: It is used to activate or deactivate the update of the data stored in the module pkl_manager
    :return: Nothing
    """
    # We start the GUI and create the "star" object that contains the path of the XML file that we export from MAL
    star_gui = Gui()
    star_gui.run()

    # We send the path obtained to the xml_reader module and get the dataframe
    df = xml_reader(star_gui.path)

    # We send the dataframe to the pkl_manager module to upload the MAL data to the system.
    mal_data = pkl_manager(df, update)

    # We pass the dataframe extracted from the XML and the MAL data to the module that combines them.
    data_combination(df, mal_data)


if __name__ == "__main__":
    main(update=False)
