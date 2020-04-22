from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class App:
        def __init__(self, myParent):
                self.myContainer1 = Frame(myParent)
                self.myContainer1.pack()

                self.img = ImageTk.PhotoImage(Image.open('Chessboard.png'))
                self.Label['image'] = self.img
root = Tk()
app = App(root)
root.mainloop()
