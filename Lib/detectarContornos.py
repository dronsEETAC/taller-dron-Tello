import cv2
import numpy as np


img = cv2.imread ('imagenes/bolasDiferentesMedidas.png')
img = cv2.resize(img, (720,480))
cv2.imshow ("img", img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array ([28,100,100])
upper = np.array ([32,255,255])

mask = cv2.inRange (hsv,lower,upper)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode (mask, kernel, iterations = 2)
erosion_dilate = cv2.dilate (erosion, kernel, iterations = 3)
cv2.imshow ("mask", mask)
cv2.imshow ("erosion", erosion)
cv2.imshow ("erosion_dilate", erosion_dilate)
contours, hierarchy = cv2.findContours (erosion_dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
res = cv2.drawContours (img, contours, -1, (0,255,0),3)
cv2.imshow ("res", res)

cv2.waitKey(0)