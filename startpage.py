from tkinter import *
from functools import partial
from NewWordPage import NewWordPage

class Startpage:
  #-------------------------------#
  #----------CONSTRUCTOR----------#
  #-------------------------------#

  def __init__(self, window):
    Button(window, text="Add a new word",
           command=lambda: self.show_new_word_page(window)).grid(row=1)

  #--------------------------------------#
  #----------SHOW NEW WORD PAGE----------#
  #--------------------------------------#

  def show_new_word_page(self, window):
    for element in window.grid_slaves(): # Removing all the window's content.
      element.grid_forget()

    newWordPage = NewWordPage(window) # Showing the NewWordPage.
