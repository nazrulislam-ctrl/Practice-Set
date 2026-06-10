# Write a program to sum a list with 4 numbers entered by users


lists=[]

for i in range(4):
    a= int(input("Enter Numbers:"))
    lists.append(a)
    
print("The List=",lists)
s=0
for i in range(4):
    s= s+lists[i]
    
print(f"Sum of the list is {s}.")