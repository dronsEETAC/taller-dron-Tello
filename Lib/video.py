from djitellopy import Tello
import cv2 as cv

tello = Tello()
tello.connect()
print(tello.get_battery())
tello.streamon()
cap = cv.VideoCapture(0)

while True:
    telloFrame = tello.get_frame_read().frame
    _, computerFrame = cap.read()
    telloFrame = cv.resize(telloFrame, (360, 240))
    frame_rgb = cv.cvtColor(telloFrame, cv.COLOR_BGR2RGB)
    cv.imshow("tello",  frame_rgb)
    cv.waitKey(1)
    computerFrame = cv.resize(computerFrame, (360, 240))
    cv.imshow("computer", computerFrame)
    cv.waitKey(1)