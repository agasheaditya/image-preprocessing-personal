import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread("../data/img4.jpg", 1)
#
# cv2.imshow("input image", img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture("../data/vid1.mp4")
while cap:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("real video", frame)
    cv2.imshow("gray video", gray)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
