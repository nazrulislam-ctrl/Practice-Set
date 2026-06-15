# Write a program which finds out whether a gien name is present in a list or not.

# names=["Nazrul", "Raju", "Shopon", "Rubel", "Hridoy", "Helal", "Sayem", "Babu", "Washim", "Joshim"]

# n=input("Enter the name:")

# found= False

# for name in names:
#     if name.lower()== n.lower():
#         found= True
        
# if found:
#     print("name found")
# else:
#     print("name not found")


# Or in other Way

names=["Nazrul", "Raju", "Shopon", "Rubel", "Hridoy", "Helal", "Sayem", "Babu", "Washim", "Joshim"]

n=input("Enter the name:")

if(n in names):
    print("Name found")
else:
    print("Name is not present")