# Write a program to input eight numbers from the user and display all the unique numbers(once).

numbers= set()

for i in range (8):
    n= int(input("Enter the numbers:"))
    numbers.add(n)
    
print(numbers)
    