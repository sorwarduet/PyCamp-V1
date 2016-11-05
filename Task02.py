folder = r"C:\Users\isCoding\Desktop\Add"

import os, glob

count=0
for root, dirs, filenames in os.walk(folder):
    for filename in filenames:
        count=count+1
        filename_split = os.path.splitext(filename) # filename and extensionname (extension in [1])
        filename_zero = filename_split[0]
        os.rename(os.path.join(root, filename), os.path.join(root, filename_zero + "_"+str(count) + filename_split[1]))
        