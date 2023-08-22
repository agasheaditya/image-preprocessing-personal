import numpy as np
from skimage import io
import scipy.stats as st
import matplotlib.pyplot as plt
from skimage.transform import rescale, resize, downscale_local_mean
from skimage.filters import roberts, sobel, scharr, prewitt
from skimage.feature import canny
from skimage import restoration
from skimage.filters.rank import entropy
from skimage.morphology import disk

img = io.imread("../data/img2.jpg", as_gray=True)

# rescaled = rescale(img, 1.0/4.0, anti_aliasing=True)

# resized = resize(img, (200,200), anti_aliasing=True)

# downscaled = downscale_local_mean(img, (4,3))

## Edge filtering
# edge_roberts = roberts(img)
# edge_sobel = sobel(img)
# edge_scharr = scharr(img)
# edge_prewitt = prewitt(img)
#
# fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
#
# ax = axes.ravel()
# ax[0].imshow(img, cmap=plt.cm.gray)
# ax[0].set_title("Original")
#
# ax[1].imshow(edge_roberts, cmap=plt.cm.gray)
# ax[1].set_title("Roberts")
#
# ax[2].imshow(edge_sobel, cmap=plt.cm.gray)
# ax[2].set_title("Sobel")
#
# ax[3].imshow(edge_scharr, cmap=plt.cm.gray)
# ax[3].set_title("Scharr")
#
# # plt.imshow(img, cmap=True)
#
# for a in ax:
#     a.axis("off")
#
# plt.tight_layout()

## Canny edge detection
# edge_canny = canny(img, sigma=5)
# plt.imshow(edge_canny)

## Restoration & de-convolution

# psf = np.ones((3,3)) / 9

## to implement gaussian kernal as psf

# def gkern(kernlen=21, nsig=3):
#     """Returns a 2D Gaussian kernel."""
#
#     x = np.linspace(-nsig, nsig, kernlen+1)
#     kern1d = np.diff(st.norm.cdf(x))
#     kern2d = np.outer(kern1d, kern1d)
#     return kern2d/kern2d.sum()
# psf = gkern(5,3)
# print(psf)
# deconvolved, _ = restoration.unsupervised_wiener(img, psf = psf)  ## psf -> point spread function
# plt.imshow(deconvolved)

### Using entropy function to do microscope scratch analysis

entropy_img = entropy(img, disk(3))
# plt.imshow(entropy_img, cmap="gray")
## applying threshold on entropy filters

from skimage.filters import try_all_threshold, threshold_otsu

otsu_thresh = threshold_otsu(entropy_img)
binary = entropy_img <= otsu_thresh
# fig,ax =try_all_threshold(entropy_img, figsize=(10, 8), verbose=False)
plt.imshow(binary)
plt.show()

