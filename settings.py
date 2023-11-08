"""
.. module:: settings
   :noindex:

.. header:: Global parameters for the entire application

.. moduleauthor:: Alex Glock
"""
import pathlib
import os

BASE_DIR = pathlib.Path(__file__).parent.resolve()

APP_TITLE = "TK TEMPLATE"
SCPI_DEVICE_ID = "12345"

# font styles
TITLE_FONT = "Helvetica 14"
H1_FONT = "Helvetica 18 bold"
H2_FONT = "Helvetica 14"
CONTENT_FONT = "Helvetica 10"
FOOTER_FONT = "Helvetica 8"
# background styles
TITLE_BG = "darkgreen"
CONTENT_BG = "#E0E0E0"
FOOTER_BG = "grey"
HIGHLIGHT_BG = "#A5D6A7"
# forground styles (font color)
TITLE_FG = "white"
CONTENT_FG = "black"
FOOTER_FG = "black"

# static files
LOGO_IMAGE_PATH = os.path.join(BASE_DIR, "statics/icons/close.png")
HOME_IMAGE_PATH = os.path.join(BASE_DIR, "statics/icons/home.png")
CLOSE_IMAGE_PATH = os.path.join(BASE_DIR, "statics/icons/close.png")


