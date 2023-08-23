import cv2
import numpy as np

img = cv2.imread("../data/img4.jpg")

## All shape Drawing functions
cv2.line(img, (50, 50), (250, 100), (255, 0, 255), 5, 2)

cv2.rectangle(img, (300, 100), (500, 300), (0, 255, 255), 2)

cv2.circle(img, (400, 200), 120, (0, 0, 255), 3)

## drawing poly lines
pts = np.array([[10, 10], [120, 120], [500, 500], [300, 200], [50, 10]])
cv2.polylines(img, [pts], True, (255, 0, 0), 4)

## Writing text on an image
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img, "Chandrayan - 3", (300,550), font, 1, (255,0,0), 2, cv2.LINE_AA)

cv2.imshow("input image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
