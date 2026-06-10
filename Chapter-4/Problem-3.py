# Check that a Tuple type cannot be changed in python.

a=(2,5, "Naz", 5.3)
print(type(a))


a[2]="Change?"
