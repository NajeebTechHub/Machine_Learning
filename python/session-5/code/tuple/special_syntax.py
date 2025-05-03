# tuple unpacking
t1,t2,t3 = (3,4,5)
print(t1)
print(t2)
print(t3)

# swap
a = 2
b = 4
a,b = b,a
print(a)
print(b)

# others
c, d , *others = (1,2,3,4,5) 
print(c,d)
print(others)

# zipping tuple
t1 = (5,7,8)
t2 = (7,8,0)
print(tuple(zip(t1,t2)))