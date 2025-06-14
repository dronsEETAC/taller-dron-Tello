from tkinter import *
from djitellopy import Tello
import cv2 as cv

from PIL import Image
from PIL import ImageTk




def takePictureComputerButtonClick ():
    global cap

    _, frame = cap.read()
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    image = Image.fromarray(frame_rgb)
    max_size = (400, 300)
    image.thumbnail(max_size)
    computerPicturePanel.image = ImageTk.PhotoImage(image)
    computerPicturePanel.create_image(0, 0, anchor=NW, image=computerPicturePanel.image)

def takePictureDroneButtonClick ():
    global tello
    frame = tello.get_frame_read().frame
    image = Image.fromarray(frame)
    max_size = (400, 300)
    image.thumbnail(max_size)
    dronePicturePanel.image = ImageTk.PhotoImage(image)
    dronePicturePanel.create_image(0, 0, anchor=NW, image=dronePicturePanel.image)


def connectButtonClick ():
    global tello
    global cap
    tello = Tello()
    tello.connect()
    batteryLabel['text'] = str (tello.get_battery())
    tello.streamon()

    cap = cv.VideoCapture(0)


window = Tk()
window.geometry("800x400")
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=5)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


connectButton = Button(window, text="Conecta", bg='red', fg="white",command=connectButtonClick)
connectButton.grid(row=0, column=0, padx=5, pady=5, sticky=N + S + E + W)
batteryLabel = Label(window, text = "", font=("Courier", 20, "italic"))
batteryLabel.grid(row=0, column=1, columnspan=5, padx=5, pady=5, sticky=N + S + E + W)

takePictureDroneButton = Button(window, text="Toma foto con dron", bg='red', fg="white",command=takePictureDroneButtonClick)
takePictureDroneButton.grid(row=1, column=0, padx=5, pady=5, sticky=N + S + E + W)
dronePicturePanel = Canvas(window)
dronePicturePanel.grid(row=2, column =0, sticky=N + S + E + W)

takePictureComputerButton = Button(window, text="Toma foto con ordenador", bg='red', fg="white",command=takePictureComputerButtonClick)
takePictureComputerButton.grid(row=1, column=1, padx=5, pady=5, sticky=N + S + E + W)
computerPicturePanel = Canvas(window)
computerPicturePanel.grid(row=2, column =1, sticky=N + S + E + W)


window.mainloop()


