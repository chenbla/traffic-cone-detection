from Tkinter import *
import tkFileDialog
from PIL import Image, ImageTk

master = Tk()
master.title("GUI")
master.geometry("1280x720+500+500")
master.resizable(0, 0)

def callback():
    path = tkFileDialog.askopenfilename(
        initialdir="/home/porteon/Documents/Tez/Images/")
    e.delete(0, END)  # Remove current text in entry
    e.insert(0, path)  # Insert the 'path'

w = Label(master, text="File Path:")
e = Entry(master, text="")
b = Button(master, text="Browse", command=callback)

im = Image.open("/home/porteon/Documents/Tez/Images/test1.jpeg")
photo = ImageTk.PhotoImage(im)
cv = Canvas()
cv.pack(side="top", fill="both", expand="yes")
cv.create_image(10, 10, image=photo, anchor="nw")

w.pack(side=TOP)
e.pack(side=TOP)
b.pack(side=TOP)

master.mainloop()