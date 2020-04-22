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
        image = Image.open("Chessboard.png")
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(self.container1, image=photo)
        label.image = photo
        label.pack()

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
