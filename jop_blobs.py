# joy of programming machine vision
#* https://www.youtube.com/watch?v=3D7O_kZi8-o&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=18

import cv2
import numpy as np

def nothing(x):
    pass

# Vihreän värin säätöpalikat
cv2.namedWindow("Tracking_green")
cv2.createTrackbar("low_hue_green", "Tracking_green", 0, 255, nothing)
cv2.createTrackbar("low_satu_green", "Tracking_green", 0, 255, nothing)
cv2.createTrackbar("low_value_green", "Tracking_green", 0, 255, nothing)
cv2.createTrackbar("high_hue_green", "Tracking_green", 255, 255, nothing)
cv2.createTrackbar("high_satu_green", "Tracking_green", 255, 255, nothing)
cv2.createTrackbar("high_value_green", "Tracking_green", 255, 255, nothing)

while True:
    frame = cv2.imread('blobs.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbaarit
    l_h = cv2.getTrackbarPos("low_hue_green", "Tracking_green")
    l_s = cv2.getTrackbarPos("low_satu_green", "Tracking_green")
    l_v = cv2.getTrackbarPos("low_value_green", "Tracking_green")
    u_h = cv2.getTrackbarPos("high_hue_green", "Tracking_green")
    u_s = cv2.getTrackbarPos("high_satu_green", "Tracking_green")
    u_v = cv2.getTrackbarPos("high_value_green", "Tracking_green")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()