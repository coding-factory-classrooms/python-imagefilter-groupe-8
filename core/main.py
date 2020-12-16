import sys
from effects import *

args = sys.argv
print(args)

for i in range (len(args)-1):
    if args[i] == '-i':             # -i is used to define the directory where the picture is come from
        entry = f'{args[i + 1]}/'
        print(f'input={entry}')
    elif args[i] == '-o':           # -o is the output where the transformed image will be put
        output = f'{args[i + 1]}/'
        print(f'output={output}')
    elif args[i] == '--filters':
        print("FILTERS")


image = cv2.imread('data/dunkey.jpg') #Reference our image

turn_gray(image)
turn_blur(image)
turn_dilated(image)

cv2.waitKey(0) #destroy images when closing program
cv2.destroyAllWindows()