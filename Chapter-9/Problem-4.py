# A file contains a word "Donkey" multiple times. You need to write a program which replace this word with ###### by updating the same file.

import os

texts= '''A donkey is a hardworking animal that has helped humans for thousands of years. In many villages around the world, a donkey is used to carry goods, pull carts, and transport supplies across rough terrain where vehicles cannot easily travel. Although some people think a donkey is stubborn, it is actually an intelligent and cautious animal that often avoids dangerous situations. A healthy donkey can carry heavy loads and travel long distances while requiring relatively little food and water. Because of its strength, endurance, and gentle nature, the donkey remains an important companion for farmers and workers in many rural communities.
'''

folder= os.path.dirname(os.path.abspath(__file__))
filename= os.path.join(folder,"donkey_file.txt")

if not os.path.exists(filename):
    with open (filename, "w") as f:
        f.write(texts)
        
f= open(filename)
file=f.read()
f.close()

if("donkey" in file):
    rem_donkey_file= file.replace("donkey", "######")
    with open(filename, "w") as f:
        f.write(rem_donkey_file)
        print("Donkey word has been censored")