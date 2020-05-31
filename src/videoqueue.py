import cv2 as cv
from queue import Queue
from threading import Thread


class BoostedFPS:
    def __init__(self, src=0, queueSize=100000):
        '''Video stream thread setup'''
        self.src = src	
        self.stop_thread = False
        self.Q = Queue(maxsize=queueSize)
        Thread(target=self.VideoStream, daemon=True).start()

    def VideoStream(self):
        stream =  cv.VideoCapture(self.src)
        while not self.stop_thread:
            _, frame = stream.read()
            self.Q.put(frame)

    def stopStream(self):
        self.stop_thread = True

    def getFrame(self):
        return self.Q.get();

    def checkBuffer(self):
        return not self.Q.full() 
