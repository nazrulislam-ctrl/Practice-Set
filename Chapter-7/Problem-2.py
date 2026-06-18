# Write a program to  greet all the person names stored in a list 'l' and which starts with R.
# l=["Nazrul", "Raju", "Rubel", "Washim"]

l=["Nazrul", "Raju", "Rubel", "Washim"]

for name in l:
    if (name.startswith("R")):
        print(f"Hello, {name}")