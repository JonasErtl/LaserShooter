import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Can't retrieve video stream")
    exit()

while True: 
    ret, frame = cap.read()

    if not ret:
        print("Failed to retrieve frame, stream might have ended")
        break

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
