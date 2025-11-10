import cv2
import numpy

img1 = cv2.imread("images\\img1.png")
crop_img = img1[0:100, 0:250]  # type: ignore

cv2.imshow("cropped", crop_img)
cv2.waitKey(0)


# saving the iamge

cv2.imwrite('bird_head.png', crop_img)
