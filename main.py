#Write a python program to create Folders/Directories


# import os

# for i in range(1,7):
#     if not os.path.exists(f"Chapter-{i}"):
#         os.mkdir(f"Chapter-{i}")
        
# print("Folder Created Successfully!!!")


import os

for i in range(1,10):
    if not os.path.exists(f"Chapter-{i}"):
        os.mkdir(f"Chapter-{i}")
        
print("Folder Created Successfully!!!")