# MAIN FILE

from gui import Gui
from xml_reader import xml_reader
from pkl_manager import pkl_manager


def main():
    """
    Main function of the project
    :return: Nothing
    """
    # We start the GUI and create the "star" object that contains the path of the XML file that we export from MAL
    star_gui = Gui()
    star_gui.run()

    # We send the path obtained to the xml_reader module and get the dataframe
    df = xml_reader(star_gui.path)

    print(pkl_manager(df))


if __name__ == "__main__":
    main()
