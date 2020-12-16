import cv2
import numpy as np
import effects as ef

image = cv2.imread('data/dunkey.jpg') #Reference our image

ef.turn_gray(image)

ef.turn_blur(image)

cv2.waitKey(0) #destroy images when closing program
cv2.destroyAllWindows()