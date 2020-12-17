import cv2
import numpy as np
from logger import *

def turn_gray(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_img

def turn_blur(image, blur_degree):

    if blur_degree % 2 !=0:
        blur_image = cv2.GaussianBlur(image, (blur_degree, blur_degree), blur_degree) #Creating blurred image
        return blur_image
    else:
        log("Wrong degree given")

def turn_dilated(image,pixel_value):
    kernel = np.ones((pixel_value,pixel_value),np.uint8)
    dilation_image = cv2.dilate(image,kernel,iterations = 1 )
    return dilation_image