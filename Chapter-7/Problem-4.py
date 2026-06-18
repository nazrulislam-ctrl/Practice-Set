# Write a program to find whether a given number is prime or not.


n=int(input("Enter a  number: "))

count=0
for i in range(1,n+1):
    if(n%i)==0:
        count=count+1
if(count>2):
    print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")
    
print("Printing the result of a different way code...\n")

for i in range(2,n):
    if(n%i)==0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")