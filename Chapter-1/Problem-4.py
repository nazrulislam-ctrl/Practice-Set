# Write a python program to print the contents of the directory using the OS module. 
import os

directory_path="F:\My Projects\Python\Practice Set\Chapter-1"

contents = os.listdir(directory_path)
    
print(f"Contents of '{directory_path}':")
for item in contents:
    print(item)