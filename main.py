import cv2
import numpy as np

image = cv2.imread('data/dunkey.jpg') #Reference our image, then set it to gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', image) #Create two images, one gray and one classic
cv2.imshow('Gray image', gray)

blur_image = cv2.GaussianBlur(image, (3, 33), 0)
cv2.imshow('Blurred Image', blur_image)

cv2.waitKey(0) #destroy images when closing program
cv2.destroyAllWindows()