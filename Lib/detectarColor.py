from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()
print(tello.get_battery())
tello.streamon()


while True:
    telloFrame = tello.get_frame_read().frame

    telloFrame = cv2.resize(telloFrame, (640, 480))
    hsv = cv2.cvtColor(telloFrame, cv2.COLOR_BGR2HSV)
    value = hsv[240, 320][0]
    cv2.circle(telloFrame, (320, 240), 7, (0, 0, 255), -1)
    if value != 0:
        print (hsv[240, 320])

        cv2.putText(img=telloFrame, text=str(value), org=(320, 300), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=2,
               color=(255, 255, 255), thickness=1)

    cv2.imshow("tello", telloFrame)
    cv2.waitKey(1)