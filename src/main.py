import cv2 as cv
from tkinter import *
from PIL import Image, ImageTk
import os

cap = cv.VideoCapture(0)

root = Tk()
#root.bind('<Key>', lambda e: root.quit())
lmain = Label(root)
lmain.pack()

def process_frame():
    ret, frame = cap.read()
    if ret:
        img = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img) 
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(1, process_frame)


def labelPhoto():
    pass



process_frame()
root.mainloop()


