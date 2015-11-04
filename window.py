from tkinter import Tk

class Window(Tk):
  def __init__(self, window_title, width, height):
    Tk.__init__(self)

    self.geometry(str(width) + "x" + str(height))

    self.resizable(width=False, height=False)
    self.wm_title(window_title) # Title of the window.