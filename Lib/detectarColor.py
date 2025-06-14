from djitellopy import Tello
import cv2 as cv

tello = Tello()
tello.connect()
print(tello.get_battery())
tello.streamon()


while True:
    telloFrame = tello.get_frame_read().frame

    telloFrame = cv.resize(telloFrame, (640, 480))
    frame_rgb = cv.cvtColor(telloFrame, cv.COLOR_BGR2RGB)

    hsv = cv.cvtColor( telloFrame, cv.COLOR_BGR2HSV)
    value = hsv[240, 320][0]
    cv.circle(telloFrame, (320, 240), 7, (0, 0, 255), -1)
    if value != 0:
        print (hsv[240, 320])

        cv.putText(img=frame_rgb, text=str(value), org=(320, 300), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=2,
               color=(255, 255, 255), thickness=1)

    cv.imshow("tello", frame_rgb)
    cv.waitKey(1)