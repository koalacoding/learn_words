from tkinter import Frame, Button, Label

class Startpage:
  def __init__(self, window):
    Label(window, text="").grid() # To make a vertical space.
    Button(window, text="Add a new word").grid(padx=50)
    Label(window, text="").grid()
