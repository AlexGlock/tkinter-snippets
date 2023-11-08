"""
.. module:: layout
   :noindex:

.. header:: The basic design of the GUI window

.. moduleauthor:: Alex Glock
"""
import tkinter as tk
import settings
import logging
import time
import os
from PIL import ImageTk, Image, ImageOps
from start_frame import StartFrame


class TitleBar(tk.Frame):
    """TitleBar This class generates a title bar at the top of the App

    The titlebar will contain the png-graphic which is defined as
    ``LOGO_IMAGE_PATH`` in the settings.py. Other than that it contains the
    title of the App and a red close button + a home button.

    :param tk: tkinter package
    :type tk: default tkinter classes
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # title bar container
        # self.parent.overrideredirect(True)
        self.title_bar = tk.Frame(
            self.parent, bg=settings.TITLE_BG, relief="raised", bd=0
        )
        self.title_bar.pack(side=tk.TOP, fill=tk.X)

        # title logo
        self.logo_image = ImageTk.PhotoImage(
            Image.open(settings.LOGO_IMAGE_PATH).resize((140, 35))
        )
        title_logo = tk.Label(
            self.title_bar, image=self.logo_image, bg=settings.TITLE_BG
        )
        title_logo.pack(side=tk.LEFT, pady=6, padx=6)

        # titlebar text
        title_label = tk.Label(
            self.title_bar,
            text=settings.APP_TITLE,
            font=settings.TITLE_FONT + " bold",
            bg=settings.TITLE_BG,
            fg=settings.TITLE_FG,
        )
        title_label.pack(side=tk.LEFT, pady=2, padx=6)

        def quitter(e):
            logging.warning(" [ ABORT ] User closed the App ")
            # disconnect scpi
            self.parent.disconnect_scpi()
            # quit and remove App
            self.parent.destroy()

        # titlebar close button
        self.close_image = ImageTk.PhotoImage(
            Image.open(settings.CLOSE_IMAGE_PATH).resize((40, 40))
        )
        close_label = tk.Label(
            self.title_bar,
            image=self.close_image,
            font=settings.TITLE_FONT + " bold",
            bg="darkred",
            fg=settings.TITLE_FG,
            relief="sunken",
            bd=1,
        )
        close_label.pack(side=tk.RIGHT, pady=4, padx=10)
        close_label.bind("<Button-1>", quitter)

    def create_homebutton(self):
        def startframe(e):
            logging.warning(" [ ABORT ] User pressed the Home Button ")
            self.home_label.destroy()
            # disconnect scpi
            self.parent.disconnect_scpi()
            # load start
            self.parent.content_section.switch_frame(
                StartFrame, None, None, None, None
            )

        # titlebar home button
        self.home_image = ImageTk.PhotoImage(
            Image.open(settings.HOME_IMAGE_PATH).resize((40, 40))
        )
        self.home_label = tk.Label(
            self.title_bar,
            image=self.home_image,
            font=settings.TITLE_FONT + " bold",
            bg="white",
            fg=settings.TITLE_FG,
            relief="sunken",
            bd=1,
        )
        self.home_label.pack(side=tk.RIGHT, pady=4, padx=10)
        self.home_label.bind("<Button-1>", startframe)


class FooterBar(tk.Frame):
    """FooterBar This function creates a Footer (bottombar) for the application

    The bar contains the author information.

    :param tk: tkinter package
    :type tk: default tkinter classes
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.create_widgets()

    def create_widgets(self):
        # footer
        footer_bar = tk.Frame(
            self.parent, bg=settings.FOOTER_BG, relief="raised", bd=0
        )
        footer_bar.pack(side=tk.BOTTOM, fill=tk.X)

        footer_label1 = tk.Label(
            footer_bar,
            text="Entwicklung: ",
            font=settings.FOOTER_FONT,
            bg=settings.FOOTER_BG,
            fg=settings.FOOTER_FG,
        )
        footer_label1.pack(side=tk.LEFT, pady=4, padx=4)

        footer_label2 = tk.Label(
            footer_bar,
            text=" AlexGlock@2023 ",
            font=settings.FOOTER_FONT + " bold",
            bg=settings.FOOTER_BG,
            fg=settings.FOOTER_FG,
        )
        footer_label2.pack(side=tk.LEFT, pady=4, padx=4)


class ContentSection(tk.Frame):
    """ContentSection This function creates the content section within the app.

    The area between titlebar and the footer region will be populated with
    Frame classes from starting with ``StartFrame`` from ``start_frame.py``.

    :param tk: tkinter package
    :type tk: default tkinter classes
    """

    def __init__(self, parent, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.current_frame = StartFrame(self)
        self.current_frame.set_initial_focus()

    def switch_frame(self, frame_class, p1, p2, p3, p4):
        """Destroys current frame content and replaces it with a new one."""
        if self.current_frame is not None:
            self.current_frame.content_container.pack_forget()
            self.current_frame.content_container.destroy()
        # load new frame with kwargs
        self.current_frame = frame_class(
            self, p1, p2, p3, p4
        )
        self.current_frame.set_initial_focus()
        self.current_frame.tkraise()
