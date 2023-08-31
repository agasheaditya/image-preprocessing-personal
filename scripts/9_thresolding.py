import cv2
import numpy as np

img1 = cv2.imread("../data/bookpage.jpg")
ret, thresh = cv2.threshold(img1, 12, 255, cv2.THRESH_BINARY)
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_ret, gray_thresh = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
otsu_ret, otsu_thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# cv2.imshow("original", img1)
# cv2.imshow("Thresholded", thresh)
# cv2.imshow("Gray", gray)
# cv2.imshow("Gray Thresholded", gray_thresh)
# cv2.imshow("Gaussian Thresh", gaus)
cv2.imshow("OTSU Thresh", otsu_thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()
