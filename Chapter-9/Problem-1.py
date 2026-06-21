# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.


import os
folder=os.path.dirname(os.path.abspath(__file__))
filename=os.path.join(folder, "poems.txt")

f= open(filename)
content=f.read()
if("twinkle" in content):
    print("Twinkle is present in the content")
else:
    print("Twinkle is not present in the content")
f.close()
