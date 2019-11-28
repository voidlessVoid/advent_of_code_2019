import sys
import os
from shutil import copyfile

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

for day in range(1,26):
    folder_name = f'day_{str(day).zfill(2)}'
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print(f'{folder_name} already existed')

    subfoldername = f'{folder_name}{os.sep}mischa'

    try:
        os.mkdir(subfoldername)
    except FileExistsError:
        print(f'{subfoldername} already existed')

    copyfile('michael_template.py',f'{subfoldername}{os.sep}solution.py')

