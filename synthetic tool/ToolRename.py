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
print("******************* [BTEK] - Synthetic Toolkit *******************\n")
print("Enter contain directory: ")
inputPath = input()
print("Enter file type (.jpg : .xml : .png): ")
filetype = input()
os.chdir(inputPath)
path = os.listdir()
l = len(path)

# for tmp in progressBar(path, prefix = 'Progress:', suffix = 'Complete', length = 50):
#     # print(tmp+'\n')
#     os.chdir(inputPath+'\\'+tmp)
#     tmpPath = []
#     tmpPath = os.listdir()
#     for tmpInPath in tmpPath:
#         # print(tmpInPath)
#         os.chdir(inputPath+'\\'+tmp+'\\'+tmpInPath)
#         tmpStudyPath = []
#         tmpStudyPath = os.listdir()
#         for tmpInStudyPath in tmpStudyPath:
#             tmpFileName = str(newFileNameCount)+filetype
#             tmpFilePath = inputPath+'\\'+tmp+'\\'+tmpInPath+'\\'+tmpFileName
#             os.rename(str(tmpInStudyPath), tmpFileName)
#             # copy_tree(,outputPath)
#             # print(inputPath+'\\'+tmp+'\\'+tmpInPath+'\\'+tmpFileName)
#             shutil.copyfile(tmpFilePath, outputPath+tmpFileName)
#             newFileNameCount+=1
#             time.sleep(0.01)
for tmp in progressBar(path, prefix = 'Progress:', suffix = 'Complete', length = 50):
    # print(tmp+'\n')
    tmpFileName = str(newFileNameCount)+filetype
    os.rename(str(tmp), tmpFileName)
    newFileNameCount+=1
    time.sleep(0.01)
print("\nDone!\n")
input()