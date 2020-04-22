from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class Application:
    def __init__(self, arg1):
        #           --- DEFINE THE FRAME WIDGETS ---
        self.container1 = Frame(arg1)
        self.container1.pack(side=TOP)
        self.container2 = Frame(arg1)
        self.container2.pack(side=BOTTOM)

        #           --- IMPORT CHESSBOARD IMAGE ---
        self.img = ImageTk.PhotoImage(Image.open("Chessboard.png"))
        self.panel = ttk.Label(self.container1, image = self.img)
        self.panel.pack()

        #           --- EXIT BUTTON WIDGET ---
        self.button = Button(self.container2)
        self.button["text"] = "Exit"
        self.button["command"] = root.destroy
        self.button["background"] = "red"
        self.button.pack()

root = Tk()
root.geometry('650x650')
root.title('Chess')
root.iconbitmap('icon.ico')

app = Application(root)
root.mainloop()
