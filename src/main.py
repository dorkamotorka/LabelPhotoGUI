import cv2 as cv
from tkinter import *
from PIL import Image, ImageTk
import os


img = 0
f_num = 0
o_num = 0
path_free = '../data/freeway'
path_obstacle= '../data/obstacle'

cap = cv.VideoCapture(0)
root = Tk()
btn = Button(root, text='Obstacle', bd='5', bg='blue', fg='white', command=lambda :obstacle_path(img)) 
btn.pack(side='bottom')
btn = Button(root, text='Free-path', bd='5', bg='red', fg='white', command=lambda :free_path(img))
btn.pack(side='bottom', padx='5', pady='5')
#root.bind('<Key>', lambda e: root.destroy())
lmain = Label(root)
lmain.pack()

def process_frame():
    global img
    ret, frame = cap.read()
    if ret:
        img = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
        imgtk = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=imgtk) 
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk, background='black')
        lmain.after(1, process_frame)

def free_path(jpg):
    global f_num, path_free
    f_num = len(os.listdir(path_free))
    ext = 'freepath{x}.jpg'.format(x=f_num) 
    path = os.path.join(path_free, ext)
    cv.imwrite(path, jpg) 

def obstacle_path(jpg):
    global o_num, path_obstacle
    o_num = len(os.listdir(path_obstacle))
    ext = 'obstacle{x}.jpg'.format(x=o_num)
    path = os.path.join(path_obstacle, ext)
    cv.imwrite(path, jpg) 

process_frame()
root.mainloop()


