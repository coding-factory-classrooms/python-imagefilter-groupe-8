from effects import *
import sys


args = sys.argv
print(args)

image_nbr = 0

def transform_filter(old_filter):
    filter = old_filter.split(":")
    new_filter = {filter[0]: int(filter[1])}
    return new_filter

def modify_img(image, filter):
    try:
        for i in range(len(filter)):
            #Filter gray, blur and dilate
            print(filter[i])
            if filter[i] == 'grayscale':
                print("     Apply")
                image = turn_gray(image)
            if str(filter[i]).find('blur')!= -1:
                image = turn_blur(image, filter[i]['blur'])
            if str(filter[i]).find('dilate')!= -1:
                image = turn_dilated(image, filter[i]['dilate'])
        cv2.imshow(f'{image_nbr}', image)
        return image

    except cv2.error:
            print(f"Not a valid file")

def save_image(image, output):
    try:
        cv2.imwrite(f'{output}', image)
    except cv2.error:
            print(f"Not a valid file, failed to save")