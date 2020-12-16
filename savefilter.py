import cv2

image = cv2.imread('data/montagne.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('log/montains_gray.jpg', image_gray)




