import cv2 as cv

cap = cv.VideoCapture("video.avi")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Fin de la video.")
        break
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Video Officielle", gray)

    if cv.waitKey(30) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
