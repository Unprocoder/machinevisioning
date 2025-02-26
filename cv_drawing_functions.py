import numpy as np
import cv2

img = cv2.imread('lena.jpg', 1)

img = cv2.line(img, (0,0), (255,255), (255,0,0), 5)
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 5)

img = cv2.rectangle(img, (400,0), (500,100), (0,0,255), -1)
img = cv2.circle(img, (256,75), 63, (0,255,0))

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()