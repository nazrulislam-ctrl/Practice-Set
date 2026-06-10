# Write a program to fill in a letter template given below with name and date.
'''
letter= \'''
Dear <|Name|>,
You are selected!
<|Date|>
\'''
'''

a= input("Enter name here:")
b= input("Enter date here:")
letter= f'''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", f"{a}").replace("<|Date|>", f"{b}"))