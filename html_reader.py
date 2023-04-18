# This module performs an HTML query to enrich the XML data.
# The reading, being immutable data, is stored in a .pkl so as not to make HTML calls of animes that have already
# been read before.
from requests_html import HTMLSession
import re


def add_data_anime(id_anime):
    """
    This is the function in charge of making the HTML queries to the "My anime list" page.
    :param id_anime: Enter the anime ID extracted from the XML
    :return: A dictionary with the fields of the anime associated with the ID
    """
    mal_html_data = {"Status": "",
                     "Aired": "",
                     "Premiered": "",
                     "Studios": "",
                     "Genre": ""}
    regular_expression = ("Status: ([A-Za-z ]+)", "Aired: ([A-Za-z 0-9, \\?]+)", "Premiered: ([A-Za-z0-9 ]+)",
                          "Studios: ([A-Za-z 0-9-.°]+)", "Genres*: ([A-Za-z ,-]+)")
    mal_page = HTMLSession().get(f"https://myanimelist.net/anime/{id_anime}")
    try:
        for element in mal_page.html.find(".leftside", first=True).find(".spaceit_pad"):
            count = 0
            for keys in mal_html_data:
                if re.findall(regular_expression[count], element.text) and keys != "Genre":
                    mal_html_data[keys] = re.findall(regular_expression[count], element.text)[0]

                # Due to the nature of the html query, the text chosen for the "Genre" field must be operated.
                # In MAL the "Genre" field has twice the text, so it is necessary to eliminate this duplication
                # after the query.
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
    except AttributeError:
        print("Problems with the HTML connection. Manually check that the My Anime List page is up and running.")
    return mal_html_data


if __name__ == "__main__":
    # Functionality test
    print(add_data_anime(41457))
