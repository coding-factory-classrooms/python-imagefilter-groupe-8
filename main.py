import sys
from effects import *
import core as core
import os
from logger import *

# if a config.ini file in here, then we read it instead of the parameters in the console
try :
    with open('config.ini','r') as f:
        args = f.read().replace('"','').split()
        print("Reading config.ini")
except FileNotFoundError:
    args = sys.argv

print(f'args={args}') # the brut args
args_dict = {}        # the true args, the user gives

try:
    if args[1] == '-h':  # The help message
        log("Print the help")
        print('\nAvailable argument:\n '
              '-> -i <FilePath>  -A directory where the picture come from\n '
              '-> -o <FilePath>  -A directory where the picture will be\n '
              '-> --filters "filterA|filterB|..." -to apply to the picture \n'
              'Filters: blur:<an odd number> | dilate:<a number> | grayscale | authors')
    else:
        for i in range(len(args) - 1):
            if args[i] == '-i' or args[i] == 'input:':  # -i is used to define the directory where the picture is come from
                args_dict['entry'] = f'{args[i + 1]}'
                log(f'Directory Input={args_dict["entry"]}')

            elif args[i] == '-o' or args[i] == 'output:':  # -o is the output where the transformed image will be put
                args_dict['output'] = f'{args[i + 1]}'
                log(f'Directory Output={args_dict["output"]}')

            elif args[i] == '--filters' or args[i] == 'Filters:':  # --filters to select the filter for the picture
                args_dict["filter_to_apply"] = args[i + 1].split("|")  # .split(), split the string into a list with the given separator

                for a in range(len(args_dict["filter_to_apply"])):
                    # If a blur filter want to be applied, it will change the string to a dict which indicate the blur value

                    if args_dict["filter_to_apply"][a].find("blur:") != -1:
                        args_dict["filter_to_apply"][a] = core.transform_filter(args_dict["filter_to_apply"][a])

                    elif args_dict["filter_to_apply"][a].find("dilate:") != -1:
                        args_dict["filter_to_apply"][a] = core.transform_filter(args_dict["filter_to_apply"][a])

                    elif args_dict["filter_to_apply"][a].find("blur") != -1 or args_dict["filter_to_apply"][a].find("dilate") != -1:
                        print(f"You need to define a value for the {args_dict['filter_to_apply']} filter")
                log(f"FILTERS TO USE - {args_dict['filter_to_apply']}")

        try: # Because 'entry' and 'filter_to_apply' can not be define, there an except
            with os.scandir(args_dict['entry']) as entries:  # Open the directory as a list
                for file in entries:  # file represent a picture
                    path = f'{args_dict["output"]}{file.name}'
                    image = cv2.imread(f'{args_dict["entry"]}{file.name}')  # Reference our image
                    image = core.modify_img(image, args_dict["filter_to_apply"])
                    core.save_image(image,path)
                    core.image_nbr += 1
        except NameError:
            print("No entry for a directory or no filters found")

except IndexError :
    print("No parameter founds")

cv2.waitKey(0)  # destroy images when closing program
cv2.destroyAllWindows()
