import numpy as np
from effects import *

image = cv2.imread('data/montagne.jpg') #Reference our image

turn_gray(image)

turn_blur(image)

turn_dilated(image)

cv2.waitKey(0) #destroy images when closing program
cv2.destroyAllWindows()