from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()
print(tello.get_battery())
tello.streamon()
cap = cv2.VideoCapture(0)

while True:
    telloFrame = tello.get_frame_read().frame
    _, computerFrame = cap.read()
    telloFrame = cv2.resize(telloFrame, (360, 240))
    cv2.imshow("tello", telloFrame)
    cv2.waitKey(1)
    computerFrame = cv2.resize(computerFrame, (360, 240))
    cv2.imshow("computer", computerFrame)
    cv2.waitKey(1)