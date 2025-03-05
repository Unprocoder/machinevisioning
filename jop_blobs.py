# joy of programming machine vision
#* https://www.youtube.com/watch?v=3D7O_kZi8-o&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=18

import cv2
import numpy as np

def nothing():
    pass

cv2.namedWindow("Tracking")

while True:
    frame = cv2.imread('blobs.png')

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()