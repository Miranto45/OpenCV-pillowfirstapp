import numpy as np
import cv2 as cv

def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 50, (255, 0, 0), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow("Souris Officielle")
cv.setMouseCallback("Souris Officielle", draw_circle)

while True:
    cv.imshow("Souris Officielle", img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()
