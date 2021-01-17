import csv
import numpy as np
from distutils.dir_util import copy_tree

path = []
print("Enter csv path: ")
csvFilePath = input()
with open(csvFilePath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    for string in csvReader:
        pos = 0
        for i in range(len(string[0]) - 1):
            if (string[0][i] == "/" and string[0][i + 1] == "s"): pos = i
        path.append(string[0][0 : pos])
# print(np.unique(np.array(path)))
print("Import path successfully!\n")
print("Enter input directory: ")
inputPath = input()
print("Enter output directory: ")
outputPath = input()
for inPath in path:
    outPath = inPath
    inPath = inputPath+inPath
    outPath = outputPath+outPath
    print("copy: " + inPath)
    copy_tree(inPath,outPath)
    
print("\nDone!\n")
input('Press any key to end...')
