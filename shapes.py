import cv2
import numpy as np

img1 = np.zeros((512, 512, 3))

# rectangle
cv2.rectangle(img1, pt1=(100, 100), pt2=(300, 300),
              color=(255, 0, 0), thickness=-1)
# thickness = -1 will fill the rectangle , +ve number will give thickness to edges

# circle

cv2.circle(img1, center=(100, 400), radius=50, color=(0, 0, 255), thickness=-1)

# line

cv2.line(img1, pt1=(0, 0), pt2=(512, 512), thickness=2, color=(0, 255, 0))


# text

cv2.putText(img1, org=(100, 100), fontScale=2, color=(0, 255, 255), thickness=3,
            lineType=cv2.LINE_AA, text="This is Dev", fontFace=cv2.FONT_HERSHEY_TRIPLEX)

cv2.imshow("window", img1)  # type: ignore
cv2.waitKey(0)
