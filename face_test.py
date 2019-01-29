import cv2
filename='img/face_test.jpg'

def detect(filename):
    face_cascade=cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')

img=cv2.imread(filename)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.3,5)
