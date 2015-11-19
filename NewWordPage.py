from tkinter import Entry, Label

class NewWordPage:
  #-------------------------------#
  #----------CONSTRUCTOR----------#
  #-------------------------------#

  def __init__(self, window):
    Label(window, text="Add a new word").grid(row=1)
    Entry(window).grid(row=2)
