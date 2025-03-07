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
    #! käytetty ohjelman säätöön
    l_h = cv2.getTrackbarPos("low_hue_green", "Tracking_green")
    l_s = cv2.getTrackbarPos("low_satu_green", "Tracking_green")
    l_v = cv2.getTrackbarPos("low_value_green", "Tracking_green")
    u_h = cv2.getTrackbarPos("high_hue_green", "Tracking_green")
    u_s = cv2.getTrackbarPos("high_satu_green", "Tracking_green")
    u_v = cv2.getTrackbarPos("high_value_green", "Tracking_green")

    # vihreät säädöt
    l_g = np.array([0, 0, 199])
    u_g = np.array([71, 255, 255])

    # punaiset säädöt
    l_r = np.array([0, 24, 186])
    u_r = np.array([26, 215, 248])

    # maskit
    mask_green = cv2.inRange(hsv, l_g, u_g)
    mask_red = cv2.inRange(hsv, l_r, u_r)
    mask = mask_green | mask_red # joko vihreä tai punainen maski → maskien "yhdistäminen" 
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # kuvien näyttäminen
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask green", mask_green)
    cv2.imshow("Mask red", mask_red)
    cv2.imshow("Result", res)

    # escape
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()