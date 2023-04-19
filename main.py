# MAIN FILE
from main_files.main import start

if __name__ == "__main__":
    # If the optional "update" parameter is set to "False", the pkl_manager module will not perform a new HTML query
    # to update the data for animes whose status is not equal to "finished" and which already exist in the local pkl
    # file. This option does not affect operation if the program is run for the first time or if the pkl file is deleted
    start(update=False)
