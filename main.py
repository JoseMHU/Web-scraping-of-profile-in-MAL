# MAIN FILE

from gui import Gui
from xml_reader import xml_reader

if __name__ == "__main__":
    # We start the GUI and create the "star" object that contains the path of the XML file that we export from MAL
    star = Gui()

    # We send the path obtained to the xml_reader module and get the dataframe
    df = xml_reader(star.path)
    # print(df)
