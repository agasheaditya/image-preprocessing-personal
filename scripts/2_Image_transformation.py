from PIL import Image


img = Image.open("../data/img2.jpg")
print(f"Size of an image is {img.size}")
# img.show("input image")

## Resizing image
# resized_img = img.resize((200,300))
# print(f"Size of an resized image is {resized_img.size}")
# resized_img.show("resized image")

## using thumbnail method
# img.thumbnail((300,300))
# print(f"Size of an thumbnail image is {img.size}")
# img.show("resized image")

## cropping an image
# cropped = img.crop([0,0,200,300])
# cropped.show("cropped image")

## copy pasting images
## pasting img2 on img
# img2 = Image.open("../data/img3.jpg")
# img2.thumbnail((500,500))
# copy_img1 = img.copy()
# copy_img1.paste(img2, (250,250))
# copy_img1.show("copy paste overlay")

## rotating an image
# rotated = img.rotate(angle=135, expand=True)
# rotated.show("rotated img")

## flipping an image

# flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
# flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
# flipped.show("flipped image")

## changing image colour scale
gray = img.convert("L")
gray.show("gray image")