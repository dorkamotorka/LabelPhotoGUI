import cv2 as cv
from tkinter import *
from PIL import Image, ImageTk
import os


def ObstacleLabel():
    print('obstacle!')

def FreepathLabel():
    print('freepath!')

cap = cv.VideoCapture(0)

root = Tk()
btn = Button(root, text='Obstacle', bd='5', bg='blue', fg='white', command=ObstacleLabel) 
btn.pack(side='bottom')
btn = Button(root, text='Free-path', bd='5', bg='red', fg='white', command=FreepathLabel)
btn.pack(side='bottom', padx='5', pady='5')
#root.bind('<Key>', lambda e: root.destroy())
lmain = Label(root)
lmain.pack()

def process_frame():
    ret, frame = cap.read()
    if ret:
        img = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img) 
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk, background='black')
        lmain.after(1, process_frame)


process_frame()
root.mainloop()


