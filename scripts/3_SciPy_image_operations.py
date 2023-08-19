from skimage import io
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

img = io.imread("../data/img2.jpg")
print(img.shape, img.dtype, type(img))

# print(img[100:105, 110:115])

# mean_gray = img.mean()
# max_val = img.max()
# min_val = img.min()

# print(f"Mean {mean_gray}, Maximum {max_val}, Minimum {min_val}")

# flippedLR = np.fliplr(img)
# flippedUD = np.flipud(img)
#
# plt.subplot(2,1,1)
# plt.imshow(img, cmap="Grays")
# plt.subplot(2,2,3)
# plt.imshow(flippedLR, cmap="Blues")
# plt.subplot(2,2,4)
# plt.imshow(flippedUD, cmap="hsv")

## rotating image
# rotated = ndimage.rotate(img, 45, reshape=True)
# plt.imshow(rotated)

## image filtering
uniform_filtered = ndimage.uniform_filter(img, size=9)
plt.imshow(uniform_filtered)

gaussian_filtered = ndimage.gaussian_filter(img, sigma=5)
plt.imshow(gaussian_filtered)

median_filtered = ndimage.median_filter(img, size=3)
plt.imshow(median_filtered)

sobel_filtered = ndimage.sobel(img, axis=0)
plt.imshow(sobel_filtered)