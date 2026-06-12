# Can we have a set with 18(int) and '18' (str) as a value in it?


# we can directly create set as s={18,'18'} but not as s= (18, '18') or s=() or s={}
s=set()
s.add(18)
s.add('18')
print(type(s))
print(s)