import cv2
import numpy as np

# this is the cascade we just made. Call what you want
# watch_cascade = cv2.CascadeClassifier(
#     '/home/porteon/Documents/Tez/opencv-haar-classifier-training-master/trained_classifiers/cascade.xml')

faceCascade = cv2.CascadeClassifier('/home/porteon/Documents/Tez/cascade.xml')

img = cv2.imread('/home/porteon/Documents/Tez/Images/cones/img04.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# deneme = faceCascade.detectMultiScale(gray, 1.3, 5)
deneme = faceCascade.detectMultiScale(gray, 1.0005)

for (x, y, w, h) in deneme:
	cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('img', img)
# cv2.imshow('gray', gray)
cv2.waitKey()

