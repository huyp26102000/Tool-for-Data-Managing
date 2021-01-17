import numpy as np
import os
import time
# from distutils.dir_util import copy_tree
import shutil

def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()
# A Nicer, Single-Call Usage

path = []
newFileNameCount = 0
os.system('cls')
print("******************* [BTEK] - Anti Duplicated file Toolkit *******************\n")
print("Enter contain directory: ")
inputPath = input()
os.chdir(inputPath)
print("Enter maxRange: ")
max_range = input()
path = os.listdir()
name_path = path
# for i in range(0, len(name_path)):
#     name = name_path[i].split(".")
#     name_path[i] = name[0]
for i in range(0, int(max_range)+1):
    jpg = str(i)+".jpg"
    xml = str(i)+".xml"
    # check 
    for tmp in path:
        if(tmp == jpg):
            check = 0
            for tmp_2 in path:
                if(tmp_2==xml):
                    check = 1
                    break
            if(check == 0):
                print("Lack of " + xml)
                os.remove(jpg)
print("\nDone!\n")
input()