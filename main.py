
import tkinter
from tkinter.constants import TOP 
import cv2 
import os
from PIL import Image,ImageTk
import math
import numpy as np
from functools import partial
import threading
import time
import imutils 

stream = cv2.VideoCapture("temp2.mp4")
# cv2.imshow("st",stream)
flag = True
def play(speed):
    global flag
    print(f"The stream speed is : {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    
    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    
    # cv2.imshow("stream",stream)
    frame = imutils.resize(frame, width=1100, height=200)
    new_frame=frame
    frame=cv2.cvtColor(new_frame,cv2.COLOR_RGB2BGR)
    # new_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # cv2.imshow("main",new_hsv)
    
    
    # low_red=np.array([0,0,0])
    # high_red=np.array([,255,255])
    # nw_mask=cv2.inRange(new_frame,low_red,high_red)

    # ball=cv2.bitwise_and(frame,frame,mask=)
    frame = ImageTk.PhotoImage(image = Image.fromarray(frame))
    
    

    
    canvas.image = frame
 
    
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="orange", font="Times 26 bold", text="Umpire Check")
    flag = not flag
    

def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("pendu.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
    time.sleep(1.5)

    
    time.sleep(2.5)
    # 5. Display out/notout image
    if decision == 'out':
        decisionImg = "OUT.jpg"
    else:
        decisionImg = "NOT.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")

# Width and height of our main screen
SET_WIDTH = 1000
SET_HEIGHT = 800

# Tkinter gui starts here
window = tkinter.Tk()
window.geometry("1800x1000")
window.title("Third Umpire Decision Review ")
cv_img = cv2.cvtColor(cv2.imread("welcu.jpeg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=600)
photo = ImageTk.PhotoImage(image=Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()


# Buttons to control playback
btn = tkinter.Button(window, text = "Previous(Fast)", command = partial(play,-10), activeforeground = 'red',
			activebackground = "yellow", bg = "red", fg = "yellow",
			width = 70, font = 'summer', bd = 5,height=2)
btn.pack(side=TOP)

btn = tkinter.Button(window, text = "Previous(Slow)", command = partial(play,-2), activeforeground = 'red',
			activebackground = "yellow", bg = "red", fg = "yellow",
			width = 70, font = 'summer', bd = 5,height=2)
btn.pack()

btn = tkinter.Button(window, text = "Next(Slow)", command = partial(play,1), activeforeground = 'red',
			activebackground = "yellow", bg = "red", fg = "yellow",
			width = 70, font = 'summer', bd = 5,height=2)
btn.pack()

btn = tkinter.Button(window, text = "Next(Fast)", command = partial(play,10), activeforeground = 'red',
			activebackground = "yellow", bg = "red", fg = "yellow",
			width = 70, font = 'summer', bd = 5,height=2)
btn.pack()

btn = tkinter.Button(window, text = "Give OUT", command = out, activeforeground = 'red',
			activebackground = "yellow", bg = "red", fg = "yellow",
			width = 70, font = 'summer', bd = 5,height=2)
btn.pack()

btn = tkinter.Button(window, text = "Give NOT OUT", command = not_out, activeforeground = 'red',
			activebackground = "yellow", bg = "red", fg = "yellow",
			width = 70, font = 'summer', bd = 5,height=2,)
btn.pack()
window.mainloop()