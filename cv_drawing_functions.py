import numpy as np
import cv2
#* https://www.youtube.com/watch?v=V1aMDD5583k&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=6


img = cv2.imread('lena.jpg', 1)

img = np.zeros([512,512,3], np.uint8)

img = cv2.line(img, (0,0), (255,255), (255,0,0), 5)
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 5)

img = cv2.rectangle(img, (400,0), (500,100), (0,0,255), -1)
img = cv2.circle(img, (256,75), 63, (0,255,0))
font = cv2.FONT_HERSHEY_PLAIN
img = cv2.putText(img, "OpenCV", (10,500), font, 6, (255,255,255), cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()