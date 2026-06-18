# Write a program to print multiplication table of a given number using for loop.


n=int(input("Enter a number: "))

for i in range(1,11):
    multiply= i*n
    print(f"The multiplication of {i}X{n}= {multiply}")

