# Write a program to find out whether a given post is talking about "money" or not.

post=input("Enter the post here :")

if("money" in post.lower()):
    print("This post is talking about money")
else:
    print("This post is not talking about money")