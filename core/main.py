import sys
from effects import *

args = sys.argv
print(args)

for i in range (args.len):

image = cv2.imread('data/dunkey.jpg') #Reference our image

turn_gray(image)
turn_blur(image)

cv2.waitKey(0) #destroy images when closing program
cv2.destroyAllWindows()