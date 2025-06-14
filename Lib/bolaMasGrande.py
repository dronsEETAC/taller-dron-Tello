import cv2 as cv
import numpy as np

amarillo = 30
marron = 12
azul = 104
verde = 74

img = cv.imread ('imagenes/bolasDiferentesMedidas.png')
img = cv.resize(img, (720,480))

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)


lower = np.array ([amarillo -2,100,100])
upper = np.array ([amarillo + 2,255,255])
mask = cv.inRange (hsv,lower,upper)
kernel = np.ones((5,5), np.uint8)
erosion = cv.erode (mask, kernel, iterations = 2)
erosion_dilate = cv.dilate (erosion, kernel, iterations = 3)
contours, hierarchy = cv.findContours (erosion_dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
if len(contours) > 0:
    mayor = max(contours, key=cv.contourArea)


res = cv.drawContours (img, [mayor], -1, (0,255,0),3)



cv.imshow ("res", res)

cv.waitKey(0)