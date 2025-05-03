s1 = {1,2,3,4,5}

# not give error when value not exist
s1.discard(4)
print(s1)

# give error when value not exist
s1.remove(2)
print(s1)

# remove random value
s1.pop()
print(s1)

# clear all set to empty
s1.clear()
print(s1)

# delete all set
del s1