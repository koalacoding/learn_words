from tkinter import Tk

class Window(Tk):
  #-------------------------------#
  #----------CONSTRUCTOR----------#
  #-------------------------------#

  def __init__(self, window_title):
    Tk.__init__(self)

    self.resizable(width=False, height=False)
    self.wm_title(window_title) # Title of the window.

    # Used to center the widgets in the middle of the window
    self.rowconfigure(0, weight=1)
    self.rowconfigure(3, weight=1)
    self.columnconfigure(0, weight=1)

    self.center_on_screen()

  #-----------------------------------------------#
  #----------CENTER WINDOW ON THE SCREEN----------#
  #-----------------------------------------------#

  def center_on_screen(self):
    self.update_idletasks()
    width = self.winfo_width()
    height = self.winfo_height()
    x = (self.winfo_screenwidth() // 2) - (width // 2)
    y = (self.winfo_screenheight() // 2) - (height // 2)
    self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
