# Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
# Input:
# Dimensions of the milk tank
# H = 20cm, L = 20cm, B = 20cm

# Dimensions of the glass
# h = 3cm, r = 1cm


th = int(input('Enter tank hieght = ')) 
tl = int(input('Enter tank length = ')) 
tb = int(input('Enter tank breadth = ')) 

gh = int(input('Enter glass hieght = ')) 
gr = int(input('Enter glass radius = ')) 

dim_t = th * tl * tb

dim_g = 3.14 * gr**2 * gh

number_g = dim_t / dim_g

print(number_g)