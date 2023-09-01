import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,0,0])
    upper_red = np.array([255,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15,15), dtype=np.float32) / 225 ## divide the np.ones by the 15*15 = 225
    smoothed = cv2.filter2D(res, -1, kernel=kernel)
    blurred = cv2.GaussianBlur(res, (15, 15), 0)
    median_blur = cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    cv2.imshow("real video", frame)
    # cv2.imshow("hsv video", hsv)
    # cv2.imshow("mask video", mask)
    cv2.imshow("res video", res)
    cv2.imshow("smooth video", smoothed)
    cv2.imshow("Gaussian blur video", blurred)
    cv2.imshow("median blur video", median_blur)
    cv2.imshow("bilateral blur video", bilateral)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()