import cv2
import numpy as np

img = cv2.imread("images\\img1.png")

flag = False
ix = -1
iy = -1


def crop(event, x, y, flags, params):
    global flag, ix, iy
    if event == 1:
        flag = True
        ix = x
        iy = y

    # elif event == 0:
    #     if flag == True:
    #         cv2.rectangle(img, pt1=(ix, iy), thickness=1, color=(255,0,255))   # type: ignore

    elif event == 4:

        fx = x
        fy = y
        flag = False
        # type: ignore
        cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y),  # type: ignore
                      thickness=1, color=(255, 0, 255))  # type: ignore
        cropped_imgNew = img[iy:fy, ix:fx]  # type: ignore
        cv2.imwrite("cropped.png", cropped_imgNew)


cv2.namedWindow(winname="window")
cv2.setMouseCallback("window", crop)

while True:

    cv2.imshow("window", img)  # type: ignore

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
