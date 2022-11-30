import cv2
from client import DISCONNECT_MESSAGE, send

# Enable camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 420)

# importing cascades
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

def Calc_Center_int(ex, ey):               #Calculates the Rectangle Center Coordinates 
    res1 = (ex + (0.5 * (ew)))
    res2 = (ey + (0.5 * (eh)))
    return (int(res1), int(res2))

def Calc_Center(ex, ey):               #Calculates the Rectangle Center Coordinates 
    res1 = (ex + (0.5 * (ew)))
    res2 = (ey + (0.5 * (eh)))
    return (str(res1), str(res2))

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Getting corners around the face
    faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)  # 1.3 = scale factor, 5 = minimum neighbor
    # drawing bounding box around face
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

   
    # detecting eyes
    eyes = eyeCascade.detectMultiScale(imgGray)
    # drawing bounding box for eyes
    for (ex, ey, ew, eh) in eyes:
        img = cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 3)
        calc = Calc_Center(ex, ey)
        print("Rectangle Center: ", calc)
        send(calc)
        erst = Calc_Center_int(ex,ey)
        img = cv2.circle(img,erst,1,(0,0,255), 3)

    cv2.imshow('face_detect', img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        send(DISCONNECT_MESSAGE)
        break
cap.release()
cv2.destroyWindow('face_detect')
