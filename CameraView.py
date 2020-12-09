import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
cap.set(20,200)

while True:
    success, cam = cap.read()
    cv2.imshow("Camera",cam)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break