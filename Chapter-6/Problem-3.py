# A spam comment is defined as a text containing following keywords:
''' "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.'''

keywords= ["Make a lot of money", "buy now", "subscribe this", "click this"]


message=input("Enter Your Comment:")
spam= False

for keyword in keywords:
    if keyword.lower() in message.lower():
        spam=True
        break
if spam:
    print("Spam detected")
else:
    print("Spam not detected")
    

