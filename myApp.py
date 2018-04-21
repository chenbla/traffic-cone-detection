from Tkinter import *
import tkFileDialog
import cv2
import numpy as np

master = Tk()
master.geometry("1280x720+500+500")
master.resizable(0, 0)

c = Canvas(master, bg="blue", height=720, width=720)
c.pack()

img = ImageTk.PhotoImage(Image.open(path))
panel = Label(master, image = img)
panel.pack(side="bottom", fill="both", expand="yes")

def callback():
    path = tkFileDialog.askopenfilename()
    e.delete(0, END)  # Remove current text in entry
    e.insert(0, path)  # Insert the 'path'


w = Label(master, text="File Path:")
e = Entry(master, text="")
b = Button(master, text="Browse", command=callback)

w.pack(side=TOP)
e.pack(side=TOP)
b.pack(side=TOP)

master.mainloop()