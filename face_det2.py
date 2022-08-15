print("please wait...")
import winsound
duration = 200  
freq = 2000 
import cv2
patht = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(patht)
cap = cv2.VideoCapture(0)

if cap.isOpened():
    cap.set(3,700) 
    cap.set(4,500) 
    print("camera is on")
    print("press ESC to Exit")
    winsound.Beep(freq, duration)
    while True:
        ret, img = cap.read()
        img = cv2.flip(img,1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(20, 20))
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,500),3)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        cv2.imshow('video',img)
        key = cv2.waitKey(1)

        if key == 27:
            winsound.Beep(freq, duration)
            break
else:
    freq = 500
    winsound.Beep(freq, duration)
    print("camera is off")
cap.release()
cv2.destroyAllWindows()