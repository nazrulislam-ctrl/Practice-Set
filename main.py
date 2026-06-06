#Write a python program to create Folders/Directories

import os

for i in range (1,11):
    if not os.path.exists(f"Chapter-{i}"):
        os.mkdir(f"Chapter-{i}")
        
print("Folder Created Successfully!")