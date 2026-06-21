# Write a program to wipe out the   content of a file using python.


import os

folder= os.path.dirname(os.path.abspath(__file__))
filename= os.path.join(folder, "this_copy.txt")

with open (filename, "w") as f:
    content= f.write("")