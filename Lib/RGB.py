import cv2
def onMouseAction (event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print ("(BGR)", img [y,x])
        hsv = cv2.cvtColor (img, cv2.COLOR_BGR2HSV)
        print ("(HSV)", hsv[y,x])

img = cv2.imread ('imagenes/bolasDiferentesMedidas.png')
img = cv2.resize(img, (720,480))
cv2.imshow ("imagen", img)
cv2.setMouseCallback ('imagen', onMouseAction)
cv2.waitKey(0)