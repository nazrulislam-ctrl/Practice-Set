# Write a python program to create files in the current directory.

import os

folder= os.path.dirname(os.path.abspath(__file__))


for i in range(1,12):
    filename=os.path.join(folder, f"Problem-{i}.py")
    if not os.path.exists(filename):
        with open (filename,"w") as file:
            pass
print("Files created successfully!!!")