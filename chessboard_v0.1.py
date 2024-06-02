from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class Application:
    def __init__(self, arg1):
        #           --- DEFINE THE FRAME WIDGETS ---
        self.container1 = Frame(arg1)
        self.container1.pack()

        #           --- IMPORT CHESSBOARD IMAGE ---
        self.img = ImageTk.PhotoImage(Image.open("D:\Repositories\Chess\image_assets\Chessboard.png"))
        self.panel = ttk.Label(self.container1, image = self.img)
        self.panel.pack()

root = Tk()
root.geometry('650x650')
root.title('Chess')
root.iconbitmap('D:\Repositories\Chess\image_assets\icon.ico')

#           --- MENU BAR ---
menubar = Menu(root)
menubar.add_command(label="Exit", command=root.quit)
root.config(menu=menubar)

app = Application(root)
root.mainloop()
