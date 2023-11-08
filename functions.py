"""
.. module:: functions
   :noindex:

.. header:: Shared functionalities for multiple sourcefiles

.. moduleauthor:: Alex Glock
"""
import tkinter as tk
import settings



def configure_grid(frame, x, y):
    """This function configures a tkinter grid object.

    This utility function configures a simple grid inside of a given **frame**
    with the dimensions **x** = columns and **y** = rows.

    :param frame: container frame for the grid
    :type frame: tk.Frame
    :param x: Grid Dimension columns
    :type x: int
    :param y: Grid Dimension rows
    :type y: int
    """
    for i in range(x):
        frame.columnconfigure(i, weight=1)
    for j in range(y):
        frame.rowconfigure(j, weight=1)


def configure_container(self):
    """This function creates a basic container for all Frames.

    :return: content container filling the middle of the page
    :rtype: tk.Frame
    """
    content_container = tk.Frame(
        self.parent.parent,
        takefocus=1,
        bg=settings.CONTENT_BG,
        relief="raised",
        bd=0,
    )
    content_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    return content_container
