import cv2
import numpy as np

#_____imgOriginal
imgOriginal = cv2.imread('/home/porteon/Documents/Tez/Images/image1.png')

#_____imgHSV
imgHSV = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV)

#_____imgThreshLow
lowerRed = np.array([0, 135, 135])
upperRed = np.array([15, 255, 255])
imgThreshLow = cv2.inRange(imgHSV, lowerRed, upperRed)

#_____imgThreshHigh
lowerRed = np.array([159, 135, 135])
upperRed = np.array([179, 255, 255])
imgThreshHigh = cv2.inRange(imgHSV, lowerRed, upperRed)

#_____imgThresh
imgThresh = cv2.add(imgThreshLow, imgThreshHigh)

#_____imgThreshSmoothed
#Erode(), Dilate(), SmoothGaussian()
kernel = np.ones((3, 3), np.uint8)
imgEroded = cv2.erode(imgThresh, kernel, iterations=1)
imgDilated = cv2.dilate(imgEroded, kernel, iterations=1)
imgThreshSmoothed = cv2.GaussianBlur(imgDilated, (3, 3), 0)

#_____imgCanny
imgCanny = cv2.Canny(imgThreshSmoothed, 80, 160)

#_____imgContours
_, contours, _ = cv2.findContours(np.array(imgCanny), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
imgContours = np.zeros_like(imgCanny)
cv2.drawContours(imgContours, contours, -1, (255, 255, 255), 1)

#_____imgAllConvexHulls


#Image scaling
imgOriginalSmall = cv2.resize(imgOriginal, (0, 0), fx=0.5, fy=0.5)
imgHSVSmall = cv2.resize(imgHSV, (0, 0), fx=0.5, fy=0.5)
imgThreshLowSmall = cv2.resize(imgThreshLow, (0, 0), fx=0.5, fy=0.5)
imgThreshHighSmall = cv2.resize(imgThreshHigh, (0, 0), fx=0.5, fy=0.5)
imgThreshSmall = cv2.resize(imgThresh, (0, 0), fx=0.5, fy=0.5)
imgThreshSmoothedSmall = cv2.resize(imgThreshSmoothed, (0, 0), fx=0.5, fy=0.5)
imgCannySmall = cv2.resize(imgCanny, (0, 0), fx=0.5, fy=0.5)
imgContoursSmall = cv2.resize(imgContours, (0, 0), fx=0.5, fy=0.5)

#Image displaying
cv2.imshow('imgOriginal', imgOriginalSmall)
cv2.imshow('imgHSV', imgHSVSmall)
cv2.imshow('imgThreshLow', imgThreshLowSmall)
cv2.imshow('imgThreshHigh', imgThreshHighSmall)
cv2.imshow('imgThresh', imgThreshSmall)
cv2.imshow('imgThreshSmoothed', imgThreshSmoothedSmall)
cv2.imshow('imgCanny', imgCannySmall)
cv2.imshow('imgContours', imgContoursSmall)

cv2.waitKey()

#2. GitHub/PyCharm Entegrasyon Denemesi