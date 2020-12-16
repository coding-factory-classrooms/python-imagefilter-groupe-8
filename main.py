import sys
from effects import *

args = sys.argv
print(args)
print(len(args))

for i in range(len(args) - 1):
    if args[i] == '-i':  # -i is used to define the directory where the picture is come from
        entry = f'{args[i + 1]}/'
        print(f'input={entry}')

    elif args[i] == '-o':  # -o is the output where the transformed image will be put
        try:
            output = f'{entry}/{args[i + 1]}/'
            print(f'output={output}')
        except NameError:
            print("No entry Found")

    elif args[i] == '--filters':  # --filters to select the filter for the picture
        print("FILTERS")
        filter_to_apply = args[i + 1].split("|")  #.split(), split the string into a list with the given separator

        for a in range(len(filter_to_apply)-1):
            # If a blur filter want to be applied, it will change the string to a dict which indicate the blur value
            if filter_to_apply[a].find("blur:") != -1 or filter_to_apply[a].find("dilate:") != -1:
                filter = filter_to_apply[a].split(":")
                new_filter = {filter[0]: int(filter[1])}
                filter_to_apply[a] = new_filter
            elif filter_to_apply[a].find("blur") != -1 or filter_to_apply[a].find("dilate") != -1:
                print(f"You need to define a value for the {filter_to_apply[a]} filter")

        print(filter_to_apply)

try :
    image = cv2.imread(f'{entry}montagne.jpg')  # Reference our image
    turn_gray(image)
    turn_blur(image)
    turn_dilated(image)
except NameError:
    print("No entry found")

cv2.waitKey(0)  # destroy images when closing program
cv2.destroyAllWindows()
