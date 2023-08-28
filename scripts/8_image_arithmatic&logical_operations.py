import cv2
import numpy as np

img1 = cv2.imread("../data/img3.jpg")
img2 = cv2.imread("../data/logo.png")

# add = img1 + img2 ## for this operation the images should have same resolution
# add = cv2.add(img1, img2) ## Also try dividing image pixels like this -> add(img1, img2)
# cv2.imshow("add", add)

# weighted_add = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
# cv2.imshow("Weighted add", weighted_add)

rows, cols, channels = img2.shape

roi = img1[0:rows, 0:cols]
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 210, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("mask", mask)

mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask)
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow("res", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()