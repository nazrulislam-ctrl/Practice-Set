# Write a program to generate multiplication tables from 1 to 20 and write it to the different files. Place these files in a folder for a 13 - year old.

import os

# Directory containing the current Python script
script_dir= os.path.dirname(os.path.abspath(__file__))

# Path to the tables folder inside the script directory
folder= os.path.join(script_dir, "Multiplication Tables") 


if not os.path.exists(folder):
    os.mkdir(folder)

for i in range(1,21):
    filename=os.path.join(folder, f"Table for {i}.txt")
    
    if not os.path.exists(filename):
        with open (filename, "w") as file:
            for j in range(1,11):
                file.write(str(f"{i} X {j} = {i*j}\n"))
                
                
print("Script location:", os.path.dirname(os.path.abspath(__file__)))
print("Current working directory:", os.getcwd())
                