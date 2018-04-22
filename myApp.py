from Tkinter import *
import tkFileDialog
from PIL import Image, ImageTk
import cv2
import numpy as np

master = Tk()
master.title("GUI")
master.geometry("1280x720+500+500")
master.resizable(0, 0)

canvas = Canvas(width=300, height=200, bg='black')
canvas.pack(expand=YES, fill=BOTH)

path = ''

def callback():

    path = tkFileDialog.askopenfilename(
        initialdir="/home/porteon/Documents/Tez/Images/")
    e.delete(0, END)  # Remove current text in entry
    e.insert(0, path)  # Insert the 'path'

    img = PhotoImage(file=path)
    canvas.create_image(50, 10, image=img, anchor=NW)

if __name__ == "__main__":

    w = Label(master, text="File Path:")
    e = Entry(master, text="")
    b = Button(master, text="Browse", command=callback)


    w.pack(side=TOP)
    e.pack(side=TOP)
    b.pack(side=TOP)
    # lbl.pack()

    master.mainloop()