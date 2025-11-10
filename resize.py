import cv2


img1 = cv2.imread("images\\img1.png")
img1_resize = cv2.resize(img1, (256, 256))  # type: ignore


# half the size of image

img1_new = cv2.resize(
    img1, (img1.shape[1]//2, img1.shape[0]//2))  # type: ignore
cv2.imshow("resized image", img1_new)
cv2.waitKey(0)
