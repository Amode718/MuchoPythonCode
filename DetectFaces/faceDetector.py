import cv2
import os

from matplotlib.pyplot import gray


faceCascade = cv2.CascadeClassifier("DetectFaces/Files/haarcascade_frontalface_default.xml")

img = cv2.imread("DetectFaces/Files/photo.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Script will run quicker with 1.05
faces = faceCascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

cv2.imshow("Gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()