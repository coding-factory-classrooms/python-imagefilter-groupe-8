import cv2
import numpy as np
from logger import *

def turn_gray(image):
    """
    Function to turn an image in B&W, getting rid of the classic RGB
    :param image: the first image chosen in our directory
    :return: an image witha gray filter
    """
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_img

def turn_blur(image, blur_degree):
    """
    Function to apply a blur filter on the picture
    :param image: Same picture if it passed throught turn_gray
    :param blur_degree: int to know how myuch we need to blur the picture, it HAS to be an odd number, else it won't apply the filter
    :return: an image with a blur filter
    """

    if blur_degree % 2 !=0:
        blur_image = cv2.GaussianBlur(image, (blur_degree, blur_degree), blur_degree) #Creating blurred image
        return blur_image
    else:
        log("Wrong degree given")

def turn_dilated(image,pixel_value):
    """
    Function to apply a dilation filter on the image
    :param image: Same picture if it passed by by the other filters
    :param pixel_value: a value to know how much we'l$iml dilate the picture
    :return: a dilated picture
    """
    kernel = np.ones((pixel_value,pixel_value),np.uint8)
    dilation_image = cv2.dilate(image,kernel,iterations = 1 )
    return dilation_image