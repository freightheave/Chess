from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title('Chess')
root.iconbitmap('icon.ico')

myImg = ImageTk.PhotoImage(Image.open('Chessboard.png'))
panel= ttk.Label(root, image = myImg)
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()
