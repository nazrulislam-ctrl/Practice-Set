# Lebel the program written in problem 4 wiht comments.

import os

#Specify the the directory you want to list
directory_path="F:\My Projects\Python\Practice Set\Chapter-1"

#List all files and directories in the specified path
contents = os.listdir(directory_path)
    
#print the contents of directory path
print(f"Contents of '{directory_path}':")

#print each file and directory name
for item in contents:
    print(item)