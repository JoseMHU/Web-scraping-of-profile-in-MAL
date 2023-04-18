# This module performs an HTML query to enrich the XML data.
# The reading, being immutable data, is stored in a .pkl so as not to make HTML calls of animes that have already
# been read before.
from requests_html import HTMLSession
import re


def add_data_anime(id_anime=35180):
    mal_html_data = {"Status": "",
                     "Aired": "",
                     "Premiered": "",
                     "Studios": "",
                     "Genre": ""}
    regular_expression = ["Status: ([A-Za-z ]+)", "Aired: ([A-Za-z 0-9, \\?]+)", "Premiered: ([A-Za-z0-9 ]+)",
                          "Studios: ([A-Za-z 0-9-.°]+)", "Genres*: ([A-Za-z ,]+)"]
    mal_page = HTMLSession().get(f"https://myanimelist.net/anime/{id_anime}")
    for element in mal_page.html.find(".leftside", first=True).find(".spaceit_pad"):
        count = 0
        for keys in mal_html_data:
            if re.findall(regular_expression[count], element.text) and keys != "Genre":
                mal_html_data[keys] = re.findall(regular_expression[count], element.text)[0]
            elif re.findall(regular_expression[count], element.text) and keys == "Genre":
                list_items = []
                for raw_text in re.findall(regular_expression[count], element.text):
                    raw_text = raw_text.split(",")
                    for i in raw_text:
                        if i[0] == " ":
                            i = i[1:]
                        i = i[0:int(len(i) / 2)]
                        list_items.append(i)
                mal_html_data[keys] = list_items
            count += 1
    return mal_html_data

if __name__ == "__main__":
    # Functionality test
    print(add_data_anime())
