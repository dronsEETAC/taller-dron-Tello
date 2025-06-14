from tkinter import *
from djitellopy import Tello
import cv2 as cv

from PIL import Image
from PIL import ImageTk
import threading

def takeVideoStream ():
    global tello
    global takingVideo
    while takingVideo:
        telloFrame = tello.get_frame_read().frame
        telloFrame = cv.resize(telloFrame, (360, 240))
        frame_rgb = cv.cvtColor(telloFrame, cv.COLOR_BGR2RGB)
        cv.imshow("tello", frame_rgb)
        cv.waitKey(1)
    cv.destroyWindow ('tello')


def takeVideoButtonClick ():
    global takingVideo
    takingVideo = True
    x = threading.Thread(target=takeVideoStream)
    x.start()

def stopVideoButtonClick ():
    global takingVideo
    takingVideo = False

def takePictureButtonClick ():
    global tello
    frame = tello.get_frame_read().frame
    image = Image.fromarray(frame)
    max_size = (400, 300)
    image.thumbnail(max_size)
    picturePanel.image = ImageTk.PhotoImage(image)
    picturePanel.create_image(0, 0, anchor=NW, image=picturePanel.image)


def connectButtonClick ():
    global tello
    global cap
    tello = Tello()
    tello.connect()
    batteryLabel['text'] = str (tello.get_battery())
    tello.streamon()
    #cap = cv.VideoCapture(0)


window = Tk()
window.geometry("400x400")
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


connectButton = Button(window, text="Conecta", bg='red', fg="white",command=connectButtonClick)
connectButton.grid(row=0, column=0, padx=5, pady=5, sticky=N + S + E + W)
batteryLabel = Label(window, text = "", font=("Courier", 20, "italic"))
batteryLabel.grid(row=0, column=1, columnspan=5, padx=5, pady=5, sticky=N + S + E + W)

takeVideoButton = Button(window, text="Toma video con dron", bg='red', fg="white",command=takeVideoButtonClick)
takeVideoButton.grid(row=1, column=0, padx=5, pady=5, sticky=N + S + E + W)

stopVideoButton = Button(window, text="Stop video con dron", bg='red', fg="white",command=stopVideoButtonClick)
stopVideoButton.grid(row=1, column=1, padx=5, pady=5, sticky=N + S + E + W)


takePictureButton = Button(window, text="Toma foto con dron", bg='red', fg="white",command=takePictureButtonClick)
takePictureButton.grid(row=2, column=0, columnspan = 2, padx=5, pady=5, sticky=N + S + E + W)
picturePanel = Canvas(window)
picturePanel.grid(row=3, column =0, columnspan = 2, sticky=N + S + E + W)


window.mainloop()


