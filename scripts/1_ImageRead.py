## image pre-processinng using Pillow
## pip install Pillow

# from PIL import Image
# import numpy as np
# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
# from skimage import io, img_as_float, img_as_ubyte
import cv2
import glob

## reading an image using Pillow
# img = Image.open(fp="../data/img1.jpg")
# print("type of an image is: ", type(img))

## to show an image
# img.show()
## to check the type of an image
# print(img.format)

## convert imported image into numpy array
# img1 = np.asarray(img)
# print(type(img1))

## reading an image using matplotlib
# img = mpimg.imread(fname="../data/img1.jpg")
# print(type(img))
# print(img.shape)
# plt.imshow(img)

## reading image using sk-image
# img = io.imread(fname="../data/img1.jpg")
# print(type(img))
# plt.imshow(img)


## reading an image using opencv
# img = cv2.imread(filename="../data/img2.jpg")
# cv2.imshow("sample input", img)
#
# ## convert image to grayscale
# gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray input", gray)
#
# ## convert image from bgr to rgb
# rgb = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)
# cv2.imshow("RGB input", rgb)
#
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

## reading multiple files from folder

local_path ="../data/*"
for file in glob.glob(local_path):
    print(file)
    ip = cv2.imread(filename=file)
    gray = cv2.cvtColor(ip, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray from folder", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()