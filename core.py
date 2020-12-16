from effects import *

image_nbr = 0

def modify_img(image):
    try:
        image = turn_gray(image)
        image = turn_blur(image)
        image = turn_dilated(image)
        cv2.imshow(f'{image_nbr}', image)
    except NameError:
        print("No entry found")

# image = cv2.imread('data/montagne.jpg')
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# cv2.imwrite('log/montains_gray.jpg', image_gray)