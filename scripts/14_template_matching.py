import cv2
import numpy as np

image = cv2.imread("../data/pattern.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread("../data/template.png", 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

thresh = 0.8

loc = np.where( res >= thresh)


for pt in zip(*loc[::-1]):
    image = cv2.rectangle(image, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

cv2.imshow("detected patterns", image)
cv2.imshow("original input", image)
cv2.imshow("pattern", template)

cv2.waitKey(0)
cv2.destroyAllWindows()