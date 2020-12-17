from effects import *
import sys


args = sys.argv
print(args)

image_nbr = 0

def modify_img(image, filters):
    try:
        image = turn_gray(image)
        image = turn_blur(image)
        image = turn_dilated(image)
        cv2.imshow(f'{image_nbr}', image)
    except cv2.error:
        print(f"Not a valid file")

def modify_img(image, filtre):
    try:
        for i in range(len(filtre) - 1):
            #Filter gray, blur and dilate
            if filtre[i] == 'gray':
                filtre = f'{filtre[i + 1]}/'
                image = turn_gray(image)
            if str(filtre[i]).find('blur')!= -1:
                filtre = f'{filtre[i + 1]}/'
                image = turn_blur(image,filtre[i]['blur'])
            if str(filtre[i]).find('dilate')!= -1:
                filtre = f'{filtre[i + 1]}/'
                image = turn_dilated(image,filtre[i]['dilate'])
        cv2.imshow(f'{image_nbr}', image)

    except cv2.error:
            print(f"Not a valid file")


def save_image(image):
    image = cv2.imread(image)
    image_filter = cv2.cvtColor(modify_img(image))
    cv2.imwrite(f'output/{image_filter}', image_filter)

