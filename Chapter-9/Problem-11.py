# Write a pyton  program to rename a file to "renamed_by_python.txt"

import os

folder= os.path.dirname(os.path.abspath(__file__))
filename= os.path.join(folder, "old_file.txt")
rename= os.path.join(folder, "renamed_by_python.txt")
    
os.rename(filename, rename)