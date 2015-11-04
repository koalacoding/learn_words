from tkinter import Frame, Button, Label

class Startpage:
  def __init__(self, window):
    Button(window, text="Start working").grid()
    Button(window, text="Statistics").grid()
    Label(window, text="").grid() # To make a line space between Statistics and Login.
    Button(window, text="Login").grid()
    Button(window, text="Register").grid()
