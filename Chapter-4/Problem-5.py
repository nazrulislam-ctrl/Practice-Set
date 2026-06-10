# Write a program to count the number of Zeros in the following tuple.
# a =(7, 0, 8, 0, 0, 9)

a =(7, 0, 8, 0, 0, 9)

count=0
for i in range (len(a)):
    if (a[i]==0):
        count=count+1
print(count)