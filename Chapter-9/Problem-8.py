# Write a program to make a copy of a text file "this.txt"


import os


folder= os.path.dirname(os.path.abspath(__file__))
filename= os.path.join(folder, "this.txt")

with open (filename, "r") as f:
    content=f.read()
    
copy_file= os.path.join(folder, "this_copy.txt")


copy= open(copy_file, "w")
copy.write(content)
copy.close()