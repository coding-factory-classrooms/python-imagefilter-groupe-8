from effects import *

image_nbr = 0

def transform_filter(old_filter):
    """
    To transform the string filter to a dict filter
    :param old_filter: the string
    :return: the dict
    """
    filter = old_filter.split(":")
    new_filter = {filter[0]: int(filter[1])}
    return new_filter

def modify_img(image, filter):
    """
    Apply the filter to the picture
    :param image: the image to modify
    :param filter: the list of filter to apply
    :return: the new picture
    """
    try:
        for i in range(len(filter)):
            #Filter gray, blur and dilate
            if filter[i] == 'grayscale':
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
    """
    To save the transformed picture
    :param image: transformed
    :param output: the path to save the file
    """
    try:
        try :
            cv2.imwrite(f'{output}', image)
        except FileNotFoundError:
            print("Output not available")
    except cv2.error:
        print(f"Not a valid file, failed to save")