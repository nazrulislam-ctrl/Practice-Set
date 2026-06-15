# Write a program to find the greatest of four numbers entered by the user. 

#we can do this in many ways, here are two ways given below:

#1

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if(a>b and a>c and a>d):
#     print("The greatest number is", a)
# elif(b>a and b>c and b>d):
#     print("The greatest number is", b)
# elif(c>a and c>b and c>d):
#     print("The greatest number is", c)
# else:
#     print("The greatest number is", d)




#2

numbers= []

for i in range (4):
    n= int(input("Enter the number here:"))
    numbers.append(n)

greatest=numbers[0]

for i in range(1, len(numbers)):
    if numbers[i]> greatest:
        greatest= numbers[i]
print("The greatest number is ", greatest)
    