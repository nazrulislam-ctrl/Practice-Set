# Write a program to find out the line  number where python is present from ques 6.

import os

folder= os.path.dirname(os.path.abspath(__file__))
filename= os.path.join(folder, "log.txt")

with open (filename) as f:
    lines= f.readlines()
    
lineno=1
for line in lines:
    if("python" in line):
        print(f"Yes, python is present in line no- {lineno}")
        break
    lineno+=1 
else:
    print("Python is not present")