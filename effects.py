import cv2
import numpy as np

def turn_gray(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_img

def turn_blur(image):
    blur_degree = 9

    if blur_degree % 2 !=0:
        blur_image = cv2.GaussianBlur(image, (blur_degree, blur_degree), blur_degree) #Creating blurred image
        return blur_image

def turn_dilated(image):
    kernel = np.ones((5,5),np.uint8)
    dilation_image = cv2.dilate(image,kernel,iterations = 1 )
    return dilation_image