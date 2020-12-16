import cv2
import numpy as np

def turn_gray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original image', image) #Create two images, one gray and one classic
    cv2.imshow('Gray image', gray)


def turn_blur(image):
    blur_degree = 9

    if blur_degree % 2 !=0:
        blur_image = cv2.GaussianBlur(image, (blur_degree, blur_degree), blur_degree) #Creating blurred image
        cv2.imshow('Blurred Image', blur_image)

def turn_dilated(image):
    kernel = np.ones((5,5),np.uint8)
    dilation_image = cv2.dilate(image,kernel,iterations = 1 )
    cv2.imshow('Dilated Imagee', dilation_image)