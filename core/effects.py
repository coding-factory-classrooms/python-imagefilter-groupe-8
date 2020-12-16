import cv2

blur_degree = 9


def turn_gray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original image', image) #Create two images, one gray and one classic
    cv2.imshow('Gray image', gray)


def turn_blur(image):
    if blur_degree % 2 !=0:
        blur_image = cv2.GaussianBlur(image, (blur_degree, blur_degree), blur_degree) #Creating blurred image
        cv2.imshow('Blurred Image', blur_image)