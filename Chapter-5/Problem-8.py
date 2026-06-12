# If languages of two friends are same; what will happen to the program in prblem 6?

dictionary={}

for i in range(1,5):
    n=input("Enter your name:")
    l=input("Enter your favourit programming Language:")
    dictionary.update({n:l})
    
print(dictionary)