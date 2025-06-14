import cv2 as cv
def onMouseAction (event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        print ("(BGR)", img [y,x])
        hsv = cv.cvtColor (img, cv.COLOR_BGR2HSV)
        print ("(HSV)", hsv[y,x])

img = cv.imread ('imagenes/bolasDiferentesMedidas.png')
img = cv.resize(img, (720,480))
cv.imshow ("imagen", img)
cv.setMouseCallback ('imagen', onMouseAction)
cv.waitKey(0)