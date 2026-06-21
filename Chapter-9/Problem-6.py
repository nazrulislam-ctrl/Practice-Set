# Write a program to mine a log file and find out whether it contains 'python'.


import os

log_file='''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.
python
In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.'''

folder= os.path.dirname(os.path.abspath(__file__))
filename=os.path.join(folder, "log.txt")

if not os.path.exists(filename):
    f= open(filename, "w")
    file= f.write(log_file)
    f.close()

with open (filename) as file:
    content= file.read()
    
if("python" in content):
    print("Python is present")
else:
    print("Python is not present")