import cv2

img1 = cv2.imread("images\\img1.png")

# flip vertically
img1_flip = cv2.flip(img1, 0)  # type: ignore


# flip horizontally
img1_new = cv2.flip(img1, 1)  # type: ignore


# total flip
img1_total = cv2.flip(img1, -1)  # type: ignore

cv2.imshow("win", img1_total)
cv2.waitKey(0)
