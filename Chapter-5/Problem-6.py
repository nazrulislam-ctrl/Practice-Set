# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

dictionary={}

for i in range(1,5):
    n=input("Enter your name:")
    l=input("Enter your favourit programming Language:")
    dictionary.update({n:l})
    
print(dictionary)