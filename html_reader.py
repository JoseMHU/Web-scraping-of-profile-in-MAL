# This module performs an HTML query to enrich the XML data.
# The reading, being immutable data, is stored in a .pkl so as not to make HTML calls of animes that have already
# been read before.

import pickle
from requests_html import HTMLSession
from anime import Anime


# animes = Anime()
