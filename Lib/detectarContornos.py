import cv2 as cv
import numpy as np


#img = cv.imread ('imagenes/bolasDiferentesMedidas.png')
img = cv.imread ('imagenes/muchasPelotas.jpg')
img = cv.resize(img, (720,480))
cv.imshow ("img", img)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lower = np.array ([25,100,100])
upper = np.array ([35,255,255])

mask = cv.inRange (hsv,lower,upper)
kernel = np.ones((5,5), np.uint8)
erosion = cv.erode (mask, kernel, iterations = 1)
erosion_dilate = cv.dilate (erosion, kernel, iterations = 5)
cv.imshow ("mask", mask)
cv.imshow ("erosion", erosion)
cv.imshow ("erosion_dilate", erosion_dilate)
contours, hierarchy = cv.findContours (erosion_dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
res = cv.drawContours (img, contours, -1, (0,255,0),3)
cv.imshow ("res", res)

cv.waitKey(0)