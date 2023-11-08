"""
.. module:: start_frame
   :noindex:

.. header:: The first app page after the invocation

.. moduleauthor:: Alex Glock
"""
import tkinter as tk
import settings
from functions import configure_grid, configure_container
from models import load_board_measurements, save_board_measurements
from PIL import ImageTk, Image, ImageOps


class StartFrame(tk.Frame):
    """StartFrame This frame is loaded on startup of the App

    :param tk: content space in the GUI
    :type tk: TK Frame objekt
    """

    def __init__(self, parent, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        tk.Frame.__init__(self, parent)
        self.parent = parent
        # init attributes ...
        # init grid
        self.content_container = configure_container(self)
        configure_grid(self.content_container, 4, 12)
        # init gui
        self.create_widgets()

    def create_widgets(self):
        """build the page content"""

    def set_initial_focus(self):
        """set initial focus for a widget"""

