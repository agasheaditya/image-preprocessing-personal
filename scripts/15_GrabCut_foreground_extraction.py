import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("../data/test.jpg")
img_mask = cv2.imread("../data/test.jpg", 0)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# rect = (180, 570, 400, 400) # (start_x, start_y, width, height) adjust this as per the input image
# cropped = img[180:180+400, 570:570+400]
# cv2.imshow("cropped", cropped)

cv2.imshow("img_mask", img_mask)
cv2.imshow("img", img)

mask = np.zeros(img.shape[:2],np.uint8)
mask[img_mask == 255] = 1
mask[img_mask == 0] = 2 #Guess everything else is background

mask, bgdModel, fgdModel = cv2.grabCut(img, mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)

mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
mask[mask == 1] = 255

img = img * mask[:, :, np.newaxis]

cv2.imshow("img", img)
cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()