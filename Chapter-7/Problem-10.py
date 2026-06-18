# Write a program to print multiplication table of n using for loops in reversed order.

n=int(input("Enter a number: "))

for i in range(1,11):
    multiply= (11-i)*n
    print(f"{11-i}X{n}= {multiply}")