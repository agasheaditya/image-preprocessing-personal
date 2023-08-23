import cv2
import numpy as np

img = cv2.imread("../data/img3.jpg")

## Changing pixel values
# px = img[55, 55]
# print("Before", px)
#
# img[55, 55] = [255, 255, 255]
# px = img[55, 55]
# print("After", px)

## ROI
roi = img[300:500, 300:500]
# print(roi)
## changing colour of ROI
# img[300:500, 300:500] = [0,0,255]
cv2.imshow("ROI image", img)

img1 = cv2.imread("../data/img4.jpg")
img1[300:500, 300:500] = roi
cv2.imshow("pasted image", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()