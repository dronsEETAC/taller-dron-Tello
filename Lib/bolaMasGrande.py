import cv2
import numpy as np

amarillo = 30
marron = 12
azul = 104
verde = 74

img = cv2.imread ('imagenes/bolasDiferentesMedidas.png')
img = cv2.resize(img, (720,480))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lower = np.array ([amarillo -2,100,100])
upper = np.array ([amarillo + 2,255,255])
mask = cv2.inRange (hsv,lower,upper)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode (mask, kernel, iterations = 2)
erosion_dilate = cv2.dilate (erosion, kernel, iterations = 3)
contours, hierarchy = cv2.findContours (erosion_dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
if len(contours) > 0:
    mayor = max(contours, key=cv2.contourArea)


res = cv2.drawContours (img, [mayor], -1, (0,255,0),3)



cv2.imshow ("res", res)

cv2.waitKey(0)