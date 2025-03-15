# joy of programming machine vision
#* -- Trackbaarit --
#* https://www.youtube.com/watch?v=3D7O_kZi8-o&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=18
#* -- Ympyrät --
#* https://www.geeksforgeeks.org/circle-detection-using-opencv-python/

import cv2
import numpy as np
import time

def nothing(x):
    pass

# Vihreän värin säätöpalikat
#! käytetty ohjelman säätöön
# cv2.namedWindow("Tracking_green")
# cv2.createTrackbar("low_hue_green", "Tracking_green", 0, 255, nothing)
# cv2.createTrackbar("low_satu_green", "Tracking_green", 0, 255, nothing)
# cv2.createTrackbar("low_value_green", "Tracking_green", 0, 255, nothing)
# cv2.createTrackbar("high_hue_green", "Tracking_green", 255, 255, nothing)
# cv2.createTrackbar("high_satu_green", "Tracking_green", 255, 255, nothing)
# cv2.createTrackbar("high_value_green", "Tracking_green", 255, 255, nothing)

while True:
    frame = cv2.imread('blobs.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbaarit
    #! käytetty ohjelman säätöön
    # l_h = cv2.getTrackbarPos("low_hue_green", "Tracking_green")
    # l_s = cv2.getTrackbarPos("low_satu_green", "Tracking_green")
    # l_v = cv2.getTrackbarPos("low_value_green", "Tracking_green")
    # u_h = cv2.getTrackbarPos("high_hue_green", "Tracking_green")
    # u_s = cv2.getTrackbarPos("high_satu_green", "Tracking_green")
    # u_v = cv2.getTrackbarPos("high_value_green", "Tracking_green")

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


    # ylärektankeli
    #frame = cv2.rectangle(frame, (0,0), (255,100), (0, 0, 0), -1)
    # alarektankeli
    #frame = cv2.rectangle(frame, (0, 120), (255, 255), (0, 0, 0), -1) 

    # kuvien näyttäminen
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask green", mask_green)
    cv2.imshow("Mask red", mask_red)
    cv2.imshow("Result", res)

    # --- Koordinaattien nuuhkinta ---

    # suurimpien arvojen määrittäminen yhdeksi vaakasuoraksi viivaksi
    middle_green = mask_green.max(axis = 0)
    middle_red = mask_red.max(axis = 0)

    midline_green = cv2.findNonZero(middle_green)
    midline_red = cv2. findNonZero(middle_red)

    def printteri():
        print(f"Vihreät arvot {midline_green} Punaiset arvot {midline_red}")
        time.sleep(30)
    printteri()

    # --------------------------------

    #ympyrän havaitseminen
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.blur(gray, (4, 4))

    detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 60, param2 = 25, minRadius = 1, maxRadius = 40)

    # sirkkeleiden tunnistaminen
    if detected_circles is not None:
        detected_circles = np.uint16(np.around(detected_circles))
        
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]

            cv2.circle(frame, (a, b), r, (255, 255, 0), 2)

            cv2.circle(frame, (a, b), 1, (255, 255, 0), 2)

    cv2.imshow("Harmaa", gray_blurred)
    cv2.imshow("Detected Circle", frame)

    # escape
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()