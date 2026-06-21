# Write a program to find out whether a file is identical & matches the content of another file.


import os

folder= os.path.dirname(os.path.abspath(__file__))
filename= os.path.join(folder, "this.txt")
copyfile= os.path.join(folder, "this_copy.txt")

with open (filename) as f:
    lines= f.read()
    
with open (copyfile) as file:
    copy=file.read()
   
if(copy==lines):
    print("Files are identical & matche the content.")
else:
    print("Files are different and do not match the content.")