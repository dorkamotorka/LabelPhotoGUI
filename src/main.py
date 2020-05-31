import cv2 as cv
import torch
import tkinter as tk
import os

print(torch.cuda.is_available())

cam = cv.VideoCapture(0)
disp = tk.Tk()
butt = tk.Button(disp, text="Obstacle") 

