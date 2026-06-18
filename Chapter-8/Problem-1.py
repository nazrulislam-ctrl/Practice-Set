# Write a program using functions to find greatest of three numbers.

a=34
b=333
c=76
def find_greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
print(find_greatest(a,b,c))        