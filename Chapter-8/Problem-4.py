# Write a recursive function to calculate the sum of first n natural numbers.


def n_natural_numbers(n):
    if(n==1):
        return 1
    else:
        return n_natural_numbers(n-1)+n
    
n= int(input("Enter the number: "))
print(n_natural_numbers(n))    