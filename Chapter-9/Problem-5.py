# Repeat program 4 for a list of such words to be censored.


import os

bad_words = ["idiot","stupid","fool","jerk","moron","dumb","loser", "donkey"]

bad_words_file= '''Yesterday, two classmates got into an argument. One called the other an idiot and a fool, while the other responded by saying that he was a stupid jerk. Their friends told them to stop using such rude language because calling people a moron, dumb, donkey, or loser can hurt feelings and make the situation worse. By the end of the day, they apologized to each other and agreed to be more respectful.'''


folder= os.path.dirname(os.path.abspath(__file__))
filename=os.path.join(folder, "bad_words_Paragraph.txt")

if not os.path.exists(filename):
    f= open(filename, "w")
    content=f.write(bad_words_file)
    f.close()

f=open(filename, "r")
content_read= f.read()
f.close()

for word in bad_words:
    if(word in content_read):
        content_read=content_read.replace(word, "#"*len(word))
    
with open(filename, "w") as file:
    file.write(content_read)

print("Bad words censored successfully!!!")