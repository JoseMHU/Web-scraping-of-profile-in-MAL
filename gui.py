# Simple graphical user interface.
# To select the MAL XML file with the Windows file explorer.

import tkinter
from tkinter import filedialog
import customtkinter
from pathlib import Path


class Gui:
    def __init__(self):
        self.path = ""

    def run(self):
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        root = customtkinter.CTk()
        root.geometry("400x240")
        root.title("MAL XML file reader")

        def open_file():
            self.path = filedialog.askopenfilename(initialdir=f"{Path.home()}\\Desktop",
                                                   title="Select a XML file", filetypes=(("XML file", "*.xml"),))
            root.destroy()

        button = customtkinter.CTkButton(master=root, text="Documento XML", width=240, height=52, border_color="white",
                                         border_width=1, corner_radius=120, command=open_file)
        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        root.mainloop()


if __name__ == "__main__":
    # Functionality test
    star_gui = Gui()
    star_gui.run()
