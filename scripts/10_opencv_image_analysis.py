import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([10,0,0])
    upper_red = np.array([100,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("real video", frame)
    cv2.imshow("hsv video", hsv)
    cv2.imshow("mask video", mask)
    cv2.imshow("res video", res)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()