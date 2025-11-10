import cv2
import numpy as np

flag = False
ix = -1
iy = -1


def draw(event, x, y, flags, params):
    # print("Event Triggered")
    # print(event)

    global flag, ix, iy

    if event == 1:

        flag = True
        ix = x
        iy = y

    elif event == 0:
        if flag == True:
            cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y),
                          color=(0, 255, 255), thickness=-1)

    elif event == 4:
        flag = False
        cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y),
                      color=(0, 255, 255), thickness=-1)


cv2.namedWindow(winname="live Drawing")
cv2.setMouseCallback("live Drawing", draw)

img = np.ones((512, 512, 3))


while True:

    cv2.imshow("live Drawing", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
