"""
.. module:: main
   :noindex:

.. header:: The launch sequence and app invocation

.. moduleauthor:: Alex Glock
"""
import tkinter as tk
import settings
import pyvisa
import time
import os
from layout import TitleBar, ContentSection, FooterBar


class MainApplication(tk.Tk):
    """MainApplication This function starts the TKinter GUI

    The main funtion initializes the GUI Interface and loads the first Frame.

    :param tk: root window
    :type tk: tkinter Tk class
    """

    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        tk.Tk.__init__(self, *args, **kwargs)
        # init PyVisa interface
        self.scpi_manager = pyvisa.ResourceManager("@py")
        # init scpi devices
        self.scpi_device = None
        # init gui
        self.configure_gui()
        self.create_widgets()

    def connect_scpi(self):
        """connect_scpi This function connects the scpi devices"""
        device_list = self.scpi_manager.list_resources()
        MY_DEVICE_ID = '123456'

        for device_string in device_list:
            if MY_DEVICE_ID in device_string:
                self.scpi_device = self.scpi_manager.open_resource(
                    device_string, read_termination="\n"
                )


    def disconnect_scpi(self):
        """disconnect_scpi this function disconnects the scpi devices safely"""
        if self.scpi_device is not None:
            # turn off supply before disconnecting
            self.scpi_device.close()

    def configure_gui(self):
        self.title("MY TK APP")
        # fullscreen
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))
        self.resizable(True, True)

    def create_widgets(self):
        # titlebar
        self.title_bar = TitleBar(self)
        # contentsection
        self.content_section = ContentSection(self)
        # footerbar
        self.footer_bar = FooterBar(self)

    def minimize_app(self):
        # remove content, shrink to title bar
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx50+0+%d" % (width, height - 50))


if __name__ == "__main__":
    """ launch the tkinter app """
    main_app = MainApplication()
    main_app.lift()
    main_app.attributes("-topmost", True)
    main_app.focus_force()
    main_app.mainloop()
