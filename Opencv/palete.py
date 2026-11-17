import numpy as np
import cv2 as cv

def nothing(x):
    pass

img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow("Palette RGB")

cv.createTrackbar("R", "Palette RGB", 0, 255, nothing)
cv.createTrackbar("G", "Palette RGB", 0, 255, nothing)
cv.createTrackbar("B", "Palette RGB", 0, 255, nothing)
cv.createTrackbar("0 : OFF \n1 : ON", "Palette RGB", 0, 1, nothing)

while True:
    cv.imshow("Palette RGB", img)
    if cv.waitKey(1) & 0xFF == 27:
        break

    r = cv.getTrackbarPos("R", "Palette RGB")
    g = cv.getTrackbarPos("G", "Palette RGB")
    b = cv.getTrackbarPos("B", "Palette RGB")
    s = cv.getTrackbarPos("0 : OFF \n1 : ON", "Palette RGB")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()
