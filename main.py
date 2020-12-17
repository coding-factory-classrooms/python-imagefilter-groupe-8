import sys
from effects import *
import core as core
import os
from logger import *

try :
    with open('config.txt','r') as f:
        args = f.read().replace('"','').split()
        print("reading...")
except FileNotFoundError:
    args = sys.argv

print(args)


try:
    if args[1] == '-h':  # The help message
        log("Print the help")
        print('\nAvailable argument:\n '
              '-> -i <FilePath>  -A directory where the picture come from\n '
              '-> -o <FilePath>  -A directory where the picture will be\n '
              '-> --filters "filterA|filterB|..." -to apply to the picture \n'
              'Filters: blur:<an odd number> | dilate:<a number> | grayscale')
    else:
        for i in range(len(args) - 1):
            if args[i] == '-i':  # -i is used to define the directory where the picture is come from
                entry = f'{args[i + 1]}/'
                log(f'Directory Input={entry}')

            elif args[i] == '-o':  # -o is the output where the transformed image will be put
                output = f'{args[i + 1]}/'
                log(f'Directory Output={output}')

            elif args[i] == '--filters':  # --filters to select the filter for the picture
                filter_to_apply = args[i + 1].split(
                    "|")  # .split(), split the string into a list with the given separator

                for a in range(len(filter_to_apply) - 1):
                    # If a blur filter want to be applied, it will change the string to a dict which indicate the blur value
                    if filter_to_apply[a].find("blur:") != -1 or filter_to_apply[a].find("dilate:") != -1:
                        filter = filter_to_apply[a].split(":")
                        new_filter = {filter[0]: int(filter[1])}
                        filter_to_apply[a] = new_filter
                    elif filter_to_apply[a].find("blur") != -1 or filter_to_apply[a].find("dilate") != -1:
                        print(f"You need to define a value for the {filter_to_apply[a]} filter")
                log(f"FILTERS TO USE - {filter_to_apply}")

        try: # Because 'entry' and 'filter_to_apply' can not be define, there an except
            with os.scandir(entry) as entries:  # Open the directory as a list
                for file in entries:  # file represent a picture
                    image = cv2.imread(f'{entry}{file.name}')  # Reference our image
                    core.modify_img(image, filter_to_apply)
                    # core.save(image, output)
                    core.image_nbr += 1
        except NameError:
            print("No entry for a directory or no filters found")

except IndexError :
    print("No parameter founds")

cv2.waitKey(0)  # destroy images when closing program
cv2.destroyAllWindows()
