import os

path = 'd:\\' #'Add path where you want to search your file'
find = '.png' #'name of file you want to search'
files = []
for r, d, f in os.walk(path):
    for file in f:
        if find in file:
            files.append(os.path.join(r, file))

# to print all files names if found
for f in files:
    print(f)
