# The game() function in a program lets a user play a game and returns the score as an integer. Your need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-sore. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.


import random
import os

folder=os.path.dirname(os.path.abspath(__file__))
filename=os.path.join(folder, "hiscore.txt")
if not os.path.exists(filename):
    with open (filename, "w") as file:
        pass
    
def game():
        
    print("You are playing the game...")
    score= int(input("Enter Your Score: "))
    # score= random.randint(1,100)
    
    f= open(filename) 
    hiscore= f.read()
    if(hiscore!=""):
        hiscore= int(hiscore) 
    else:
        hiscore=0
    f.close()
    
    print(f"Your Score: {score}")
    print(f"Previous High Score was: {hiscore}")
    if(score>hiscore):
        with open (filename, "w") as file:
            file.write(str(score))
            
        print("You Won!!!")
    else:
        print("You Lost😥")
            
    return score

game()