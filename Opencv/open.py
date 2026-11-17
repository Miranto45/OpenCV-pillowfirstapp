import cv2 as cv
import sys

img = cv.imread("chat.jpg")

if img is None:
    sys.exit("Impossible de lire l'image. Verifiez le nom du fichier.")

cv.imshow("Display window", img)

k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("chat_sauvegarde.png", img)

cv.destroyAllWindows()
