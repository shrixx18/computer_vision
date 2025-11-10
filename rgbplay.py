import cv2
import numpy as np

img1 = cv2.imread("images\\img1.png")
print(type(img1))
print(img1.shape)  # type: ignore

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # type: ignore

img2 = cv2.imread("images\\img2.png")
print(img2.shape)  # type: ignore

# cv2.imshow("window", img1_gray)  # type: ignore

# cv2.waitKey(0)

print(img1_gray.shape)

# playing with rgb image
# here iin images RGB is treated as BGR , making the blue component 0

# img1[:, :, 0] = 0  # type: ignore

# cv2.imshow("without blue channel", img1)  # type: ignore
# cv2.waitKey(0)

# making green 0
# img1[:, :, 1] = 0  # type: ignore

# cv2.imshow("without green channel", img1)  # type: ignore
# cv2.waitKey(0)

# making red green
# img1[:, :, 2] = 0  # type: ignore

# cv2.imshow("without green channel", img1)  # type: ignore
# cv2.waitKey(0)

imgBlue = img1[:, :, 0]  # type: ignore
imgGreen = img1[:, :, 1]  # type: ignore
imgRed = img1[:, :, 2]  # type: ignore

new_img = np.hstack((imgBlue, imgGreen, imgRed))
cv2.imshow("window", new_img)
cv2.waitKey(0)
